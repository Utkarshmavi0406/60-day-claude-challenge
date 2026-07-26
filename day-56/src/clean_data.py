"""
RiskLens — Data Cleaning Pipeline

Loads the raw LendingClub loan data, defines the target variable, selects
and validates the feature set proposed in docs/API.md against real data,
handles nulls, and writes a clean, model-ready dataset.

This is an offline script — it runs once, locally, and is never called by
the deployed API. See docs/ARCHITECTURE.md for the offline vs. online data
flow diagrams.

Usage:
    python src/clean_data.py
"""
import pandas as pd
import numpy as np
from pathlib import Path

RAW_PATH = Path("data/raw/accepted_loans.csv")
OUT_PATH = Path("data/processed/clean_loans.csv")

# Columns confirmed, via real data analysis, to be dangerous or redundant.
# Documented in full in docs/feature_spec.md — not excluded on assumption.
LEAKAGE_COLUMNS = [
    "last_fico_range_high",  # post-origination — correlates 0.495 with target
                              # vs. 0.130 for origination-time FICO. Confirmed leakage.
]
FAIRNESS_EXCLUDED_COLUMNS = [
    "zip_code",  # geographic proxy risk — excluded on fair-lending grounds,
                 # not a data-quality issue. See docs/feature_spec.md.
]
REDUNDANT_COLUMNS = [
    "installment",  # r=0.93 with loan_amnt — near-collinear, redundant signal
]

NUMERIC_FEATURES = [
    "loan_amnt", "int_rate", "fico_range_high", "annual_inc", "dti",
    "emp_length", "open_acc", "total_acc", "revol_util", "delinq_2yrs", "pub_rec",
]
# Already one-hot encoded in the source data — passed through as-is.
CATEGORICAL_ONEHOT_PREFIXES = ["home_ownership_", "purpose_", "verification_status_"]
TERM_COLUMN = "term_ 60 months"  # binary: 1 = 60-month term, 0 = 36-month term


def load_raw(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(
            f"Raw data not found at {path}. See data/README.md for download instructions."
        )
    return pd.read_csv(path)


def define_target(df: pd.DataFrame) -> pd.DataFrame:
    """loan_status in the source is already binary: 1 = Fully Paid, 0 = Charged Off.
    Confirmed via correlation check (loan_status=0 has higher int_rate, lower FICO,
    higher DTI — all consistent with worse credit outcomes). We flip it so our
    target follows the convention default=1 (bad), matching docs/API.md.
    """
    df = df.copy()
    df["default"] = 1 - df["loan_status"]
    return df


def select_and_validate_features(df: pd.DataFrame) -> pd.DataFrame:
    missing_numeric = [c for c in NUMERIC_FEATURES if c not in df.columns]
    if missing_numeric:
        raise ValueError(f"Expected numeric features missing from raw data: {missing_numeric}")

    onehot_cols = [
        c for c in df.columns
        if any(c.startswith(p) for p in CATEGORICAL_ONEHOT_PREFIXES)
    ]
    if not onehot_cols:
        raise ValueError("Expected one-hot categorical columns not found — check source data format.")

    keep_cols = NUMERIC_FEATURES + onehot_cols + [TERM_COLUMN, "default"]
    keep_cols = [c for c in keep_cols if c in df.columns]
    return df[keep_cols].copy()


def handle_nulls(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    null_report = {}
    for col in NUMERIC_FEATURES:
        n_null = df[col].isnull().sum()
        if n_null > 0:
            median_val = df[col].median()
            df[col] = df[col].fillna(median_val)
            null_report[col] = {"nulls_found": int(n_null), "filled_with_median": float(median_val)}
    return df, null_report


def main():
    print("=" * 60)
    print("RiskLens — Data Cleaning Pipeline")
    print("=" * 60)

    print(f"\nLoading raw data from {RAW_PATH}...")
    df = load_raw(RAW_PATH)
    print(f"  Raw shape: {df.shape}")

    print("\nExcluding leakage / fairness / redundant columns...")
    excluded = LEAKAGE_COLUMNS + FAIRNESS_EXCLUDED_COLUMNS + REDUNDANT_COLUMNS
    for col in excluded:
        if col in df.columns:
            reason = (
                "data leakage" if col in LEAKAGE_COLUMNS
                else "fair-lending exclusion" if col in FAIRNESS_EXCLUDED_COLUMNS
                else "redundant/collinear"
            )
            print(f"  Excluding '{col}' — {reason}")

    print("\nDefining target variable...")
    df = define_target(df)
    balance = df["default"].value_counts(normalize=True)
    print(f"  Target balance — default=1: {balance.get(1, 0):.1%}, default=0: {balance.get(0, 0):.1%}")

    print("\nSelecting and validating feature set against docs/API.md...")
    df = select_and_validate_features(df)
    print(f"  Selected shape: {df.shape}")

    print("\nHandling nulls...")
    df, null_report = handle_nulls(df)
    if null_report:
        for col, info in null_report.items():
            print(f"  {col}: {info['nulls_found']} nulls filled with median {info['filled_with_median']:.2f}")
    else:
        print("  No nulls found in numeric features.")

    remaining_nulls = df.isnull().sum().sum()
    assert remaining_nulls == 0, f"Unexpected nulls remain: {remaining_nulls}"
    assert set(df["default"].unique()).issubset({0, 1}), "Target is not strictly binary."

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)

    print(f"\nSaved clean dataset to {OUT_PATH}")
    print(f"  Final shape: {df.shape}")
    print(f"  Final class balance: {df['default'].value_counts(normalize=True).to_dict()}")
    print("\nDone.")


if __name__ == "__main__":
    main()
