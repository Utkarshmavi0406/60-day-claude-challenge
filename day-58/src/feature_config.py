"""
RiskLens — Shared Feature Configuration

Single source of truth for the model's feature set. Previously, the same
column lists were independently hand-typed in src/clean_data.py,
src/train_baseline.py, and api/model_loader.py — a real duplication risk
found during the Day 8 QA review: a future feature change forgotten in
even one of those three places would silently reintroduce a column-order
or encoding mismatch bug.

Every script in this project should import from here instead of
hand-typing these lists.
"""

NUMERIC_FEATURES = [
    "loan_amnt", "int_rate", "fico_range_high", "annual_inc", "dti",
    "emp_length", "open_acc", "total_acc", "revol_util", "delinq_2yrs", "pub_rec",
]

TERM_COLUMN = "term_ 60 months"

CATEGORICAL_ONEHOT_PREFIXES = ["home_ownership_", "purpose_", "verification_status_"]

TARGET_COL = "default"

# The exact column order the model is trained on and expects at inference
# time. Numeric features first, then the term flag, then each one-hot
# categorical group — this must match clean_data.py's actual output
# column order exactly (verified by the assertion in model_loader.py's
# self-test, which checks this against a real encoded row).
MODEL_FEATURE_ORDER = NUMERIC_FEATURES + [
    "home_ownership_MORTGAGE", "home_ownership_NONE", "home_ownership_OTHER",
    "home_ownership_OWN", "home_ownership_RENT",
    "verification_status_Not Verified", "verification_status_Source Verified",
    "verification_status_Verified",
    "purpose_car", "purpose_credit_card", "purpose_debt_consolidation",
    "purpose_educational", "purpose_home_improvement", "purpose_house",
    "purpose_major_purchase", "purpose_medical", "purpose_moving", "purpose_other",
    "purpose_renewable_energy", "purpose_small_business", "purpose_vacation",
    "purpose_wedding", TERM_COLUMN,
]
