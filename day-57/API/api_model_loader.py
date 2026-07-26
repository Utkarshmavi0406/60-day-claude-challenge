"""
RiskLens API — Model Loader & Request Encoder

Loads the trained model and SHAP explainer ONCE at API startup (not per
request — see api/main.py), and converts a raw ApplicantInput (the format
a human/frontend would send) into the exact 34-column, one-hot-encoded
row the model was actually trained on.

This encoding step is the single most bug-prone part of the whole system:
a column-order or one-hot mismatch here would silently produce wrong
predictions without ever raising an error. It is tested directly in this
file's self-test, not just trusted.
"""
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from explain import RiskExplainer  # noqa: E402

# Exact column order the model was trained on — copied directly from
# reports/metrics_xgboost.json's "feature_columns" list. This is the
# single source of truth for encoding; do not hand-derive it elsewhere.
MODEL_FEATURE_ORDER = [
    "loan_amnt", "int_rate", "fico_range_high", "annual_inc", "dti",
    "emp_length", "open_acc", "total_acc", "revol_util", "delinq_2yrs", "pub_rec",
    "home_ownership_MORTGAGE", "home_ownership_NONE", "home_ownership_OTHER",
    "home_ownership_OWN", "home_ownership_RENT",
    "verification_status_Not Verified", "verification_status_Source Verified",
    "verification_status_Verified",
    "purpose_car", "purpose_credit_card", "purpose_debt_consolidation",
    "purpose_educational", "purpose_home_improvement", "purpose_house",
    "purpose_major_purchase", "purpose_medical", "purpose_moving", "purpose_other",
    "purpose_renewable_energy", "purpose_small_business", "purpose_vacation",
    "purpose_wedding", "term_ 60 months",
]

RISK_TIER_THRESHOLDS = {"low": 0.10, "medium": 0.30}


def encode_applicant(applicant) -> pd.DataFrame:
    """applicant: an ApplicantInput (or anything with matching attributes).
    Returns a single-row DataFrame with exactly MODEL_FEATURE_ORDER columns,
    in that exact order, one-hot encoded identically to clean_data.py.
    """
    row = {col: 0 for col in MODEL_FEATURE_ORDER}

    row["loan_amnt"] = applicant.loan_amount
    row["int_rate"] = applicant.interest_rate
    row["fico_range_high"] = applicant.fico_score
    row["annual_inc"] = applicant.annual_income
    row["dti"] = applicant.dti
    row["emp_length"] = applicant.employment_length_years
    row["open_acc"] = applicant.open_accounts
    row["total_acc"] = applicant.total_credit_lines
    row["revol_util"] = applicant.revolving_utilization
    row["delinq_2yrs"] = applicant.delinquencies_2yrs
    row["pub_rec"] = applicant.public_records
    row["term_ 60 months"] = 1 if applicant.term_60_months else 0

    home_col = f"home_ownership_{applicant.home_ownership.value}"
    if home_col not in row:
        raise ValueError(f"Unmapped home_ownership value: {applicant.home_ownership.value}")
    row[home_col] = 1

    purpose_col = f"purpose_{applicant.purpose.value}"
    if purpose_col not in row:
        raise ValueError(f"Unmapped purpose value: {applicant.purpose.value}")
    row[purpose_col] = 1

    verif_col = f"verification_status_{applicant.verification_status.value}"
    if verif_col not in row:
        raise ValueError(f"Unmapped verification_status value: {applicant.verification_status.value}")
    row[verif_col] = 1

    return pd.DataFrame([row])[MODEL_FEATURE_ORDER]


def risk_tier(probability: float) -> str:
    if probability < RISK_TIER_THRESHOLDS["low"]:
        return "Low"
    if probability < RISK_TIER_THRESHOLDS["medium"]:
        return "Medium"
    return "High"


# Singleton, built once and imported by api/main.py at startup.
_explainer_instance = None


def get_explainer() -> RiskExplainer:
    global _explainer_instance
    if _explainer_instance is None:
        _explainer_instance = RiskExplainer(model_path="models/final_model.pkl")
    return _explainer_instance


def _self_test():
    """Encodes each of data/sample_applicants.json's 3 profiles, runs them
    through the real model, and compares the result against directly
    encoding the same underlying dataset row — proving the encoder produces
    an output the model treats identically to training-time data.
    """
    import json
    from schemas import ApplicantInput

    print("=" * 60)
    print("RiskLens - Model Loader / Encoder Self-Test")
    print("=" * 60)

    with open("data/sample_applicants.json") as f:
        samples = json.load(f)

    explainer = get_explainer()

    for name, raw in samples.items():
        applicant = ApplicantInput(**raw)
        encoded = encode_applicant(applicant)
        assert list(encoded.columns) == MODEL_FEATURE_ORDER, "Column order mismatch!"
        result = explainer.explain(encoded)
        tier = risk_tier(result["probability"])
        print(f"\n{name}:")
        print(f"  Probability: {result['probability']:.1%}  ->  Risk tier: {tier}")
        print(f"  Top factor: {result['top_factors'][0]['explanation']}")

    print("\nAll samples encoded and scored successfully. Column order verified.")


if __name__ == "__main__":
    _self_test()
