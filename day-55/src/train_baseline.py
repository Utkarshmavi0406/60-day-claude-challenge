"""
RiskLens — Baseline Model Training (Logistic Regression)

Trains the baseline classifier against data/processed/clean_loans.csv,
establishing the number the XGBoost model (next content step) needs to
beat, or justify not beating, in docs/model_comparison.md.

Offline script — runs once locally, never called by the deployed API.

Usage:
    python src/train_baseline.py
"""
import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from evaluate import evaluate_model, print_report

DATA_PATH = Path("data/processed/clean_loans.csv")
MODEL_DIR = Path("models")
REPORTS_DIR = Path("reports")

NUMERIC_COLS = [
    "loan_amnt", "int_rate", "fico_range_high", "annual_inc", "dti",
    "emp_length", "open_acc", "total_acc", "revol_util", "delinq_2yrs", "pub_rec",
]
TARGET_COL = "default"


def main():
    print("=" * 60)
    print("RiskLens - Baseline Model Training (Logistic Regression)")
    print("=" * 60)

    print(f"\nLoading {DATA_PATH}...")
    df = pd.read_csv(DATA_PATH)
    print(f"  Shape: {df.shape}")

    X = df.drop(columns=[TARGET_COL])
    y = df[TARGET_COL]
    feature_columns = list(X.columns)

    print("\nStratified train/test split (80/20)...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )
    print(f"  Train: {X_train.shape[0]} rows, default rate {y_train.mean():.1%}")
    print(f"  Test:  {X_test.shape[0]} rows, default rate {y_test.mean():.1%}")

    print("\nFitting preprocessor (StandardScaler on numeric columns only, fit on TRAIN only)...")
    scaler = StandardScaler()
    X_train_scaled = X_train.copy()
    X_test_scaled = X_test.copy()
    X_train_scaled[NUMERIC_COLS] = scaler.fit_transform(X_train[NUMERIC_COLS])
    X_test_scaled[NUMERIC_COLS] = scaler.transform(X_test[NUMERIC_COLS])

    print("\nTraining LogisticRegression(class_weight='balanced')...")
    model = LogisticRegression(class_weight="balanced", max_iter=2000, random_state=42)
    model.fit(X_train_scaled, y_train)

    print("\nEvaluating on held-out test set...")
    y_proba = model.predict_proba(X_test_scaled)[:, 1]
    metrics = evaluate_model(y_test.values, y_proba)
    print_report("Baseline - Logistic Regression", metrics)

    assert metrics["auc"] > 0.5, "AUC below random-chance floor - something is broken."
    train_proba = model.predict_proba(X_train_scaled)[:, 1]
    train_auc = evaluate_model(y_train.values, train_proba)["auc"]
    auc_gap = train_auc - metrics["auc"]
    print(f"\n  Train AUC: {train_auc:.4f} | Test AUC: {metrics['auc']:.4f} | Gap: {auc_gap:.4f}")
    if auc_gap > 0.05:
        print("  WARNING: train/test AUC gap exceeds 0.05 - possible overfitting.")
    else:
        print("  Train/test gap is small - no overfitting concern for this simple model.")

    metrics["train_auc"] = round(train_auc, 4)
    metrics["train_test_auc_gap"] = round(auc_gap, 4)
    metrics["feature_columns"] = feature_columns
    metrics["model_type"] = "LogisticRegression"

    MODEL_DIR.mkdir(exist_ok=True)
    REPORTS_DIR.mkdir(exist_ok=True)

    joblib.dump(model, MODEL_DIR / "baseline_logreg.pkl")
    joblib.dump(scaler, MODEL_DIR / "preprocessor.pkl")
    with open(REPORTS_DIR / "metrics_baseline.json", "w") as f:
        json.dump(metrics, f, indent=2)

    print(f"\nSaved model to {MODEL_DIR / 'baseline_logreg.pkl'}")
    print(f"Saved preprocessor to {MODEL_DIR / 'preprocessor.pkl'}")
    print(f"Saved metrics to {REPORTS_DIR / 'metrics_baseline.json'}")
    print("\nDone.")


if __name__ == "__main__":
    main()
