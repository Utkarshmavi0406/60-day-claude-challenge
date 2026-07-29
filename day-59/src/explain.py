"""
RiskLens — SHAP Explainability

Wraps the final trained model (models/final_model.pkl, an XGBoost
classifier) with a SHAP TreeExplainer, producing not just a probability
but a ranked, plain-English explanation of what drove each prediction.

Builds the explainer once (slow) and reuses it for every prediction
(fast) — this module is imported by the API, never re-initialized per
request.

Usage (standalone test):
    python src/explain.py
"""
import joblib
import pandas as pd
import shap

MODEL_PATH = "models/final_model.pkl"

# Human-readable labels for the plain-English explanation sentences.
# Only covers features that can realistically land in the top-5 — the
# one-hot categorical columns get a generic fallback.
FEATURE_LABELS = {
    "loan_amnt": "loan amount",
    "int_rate": "interest rate",
    "fico_range_high": "FICO score",
    "annual_inc": "annual income",
    "dti": "debt-to-income ratio",
    "emp_length": "employment history length",
    "open_acc": "number of open credit accounts",
    "total_acc": "total credit accounts",
    "revol_util": "revolving credit utilization",
    "delinq_2yrs": "delinquencies in the past 2 years",
    "pub_rec": "public records",
    "term_ 60 months": "60-month loan term",
}


class RiskExplainer:
    """Loads the model once, builds the SHAP explainer once, and reuses
    both for every subsequent call to explain(). This class is meant to
    be instantiated a single time at API startup (see api/model_loader.py).
    """

    def __init__(self, model_path: str = MODEL_PATH):
        self.model = joblib.load(model_path)
        self.explainer = shap.TreeExplainer(self.model)
        self.feature_names = list(self.model.feature_names_in_) if hasattr(
            self.model, "feature_names_in_"
        ) else None

    def _label(self, feature: str) -> str:
        if feature in FEATURE_LABELS:
            return FEATURE_LABELS[feature]
        if feature.startswith("home_ownership_"):
            return f"home ownership status ({feature.replace('home_ownership_', '')})"
        if feature.startswith("purpose_"):
            return f"loan purpose ({feature.replace('purpose_', '').replace('_', ' ')})"
        if feature.startswith("verification_status_"):
            return f"income verification status ({feature.replace('verification_status_', '')})"
        return feature

    def explain(self, applicant_df: pd.DataFrame, top_n: int = 5) -> dict:
        """applicant_df: a single-row DataFrame with columns in the exact
        order the model was trained on. Returns probability + ranked factors.
        """
        probability = float(self.model.predict_proba(applicant_df)[:, 1][0])
        shap_values = self.explainer.shap_values(applicant_df)

        # shap_values shape: (1, n_features) for a single row
        row_shap = shap_values[0]
        contributions = list(zip(applicant_df.columns, row_shap))
        # Rank by absolute impact, most influential first
        contributions.sort(key=lambda x: abs(x[1]), reverse=True)

        top_factors = []
        for feature, shap_val in contributions[:top_n]:
            direction = "increased_risk" if shap_val > 0 else "decreased_risk"
            label = self._label(feature)
            value = applicant_df[feature].iloc[0]
            verb = "increased" if shap_val > 0 else "decreased"
            explanation = f"{label.capitalize()} ({value}) {verb} predicted risk."
            top_factors.append({
                "feature": feature,
                "direction": direction,
                "shap_value": round(float(shap_val), 4),
                "explanation": explanation,
            })

        return {"probability": round(probability, 4), "top_factors": top_factors}


def _self_test():
    """Run when this file is executed directly — not used by the API.
    Loads the model, explains 3 real rows from the dataset (spanning a
    range of predicted risk), and prints the results for manual review.
    """
    print("=" * 60)
    print("RiskLens - SHAP Explainability Self-Test")
    print("=" * 60)

    explainer = RiskExplainer()
    df = pd.read_csv("data/processed/clean_loans.csv")
    X = df.drop(columns=["default"])

    all_proba = explainer.model.predict_proba(X)[:, 1]
    df_with_proba = X.copy()
    df_with_proba["_proba"] = all_proba
    df_with_proba["_actual"] = df["default"]

    low = df_with_proba.sort_values("_proba").iloc[0]
    high = df_with_proba.sort_values("_proba", ascending=False).iloc[0]
    mid = df_with_proba.iloc[(df_with_proba["_proba"] - 0.15).abs().argsort()[:1]].iloc[0]

    for label, row in [("LOW RISK sample", low), ("HIGH RISK sample", high), ("BORDERLINE (~15%) sample", mid)]:
        applicant = pd.DataFrame([row.drop(["_proba", "_actual"])])[X.columns]
        result = explainer.explain(applicant)
        print(f"\n{'-'*60}")
        print(f"{label}")
        print(f"  Actual outcome: {'defaulted' if row['_actual']==1 else 'fully paid'}")
        print(f"  Predicted probability: {result['probability']:.1%}")
        print(f"  Top factors:")
        for f in result["top_factors"]:
            arrow = "^" if f["direction"] == "increased_risk" else "v"
            print(f"    [{arrow}] {f['explanation']}")

    print(f"\n{'='*60}")
    print("Self-test complete.")


if __name__ == "__main__":
    _self_test()
