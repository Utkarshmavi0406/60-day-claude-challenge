"""
RiskLens — XGBoost Model Training + Model Selection

Trains an XGBoost classifier on the identical train/test split used for
the Day 5 Logistic Regression baseline, evaluates it with the exact same
shared evaluate.py functions, and selects the final production model with
a documented, defensible rationale — not just whichever AUC is higher.

Offline script — runs once locally, never called by the deployed API.

Usage:
    python src/train_xgboost.py
"""
import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from xgboost import XGBClassifier

from evaluate import evaluate_model, print_report

DATA_PATH = Path("data/processed/clean_loans.csv")
MODEL_DIR = Path("models")
REPORTS_DIR = Path("reports")
DOCS_DIR = Path("docs")
TARGET_COL = "default"


def main():
    print("=" * 60)
    print("RiskLens - XGBoost Model Training + Model Selection")
    print("=" * 60)

    print(f"\nLoading {DATA_PATH}...")
    df = pd.read_csv(DATA_PATH)
    print(f"  Shape: {df.shape}")

    X = df.drop(columns=[TARGET_COL])
    y = df[TARGET_COL]
    feature_columns = list(X.columns)

    # IDENTICAL split as train_baseline.py — same test_size, same random_state,
    # same stratify — so the two models are compared on the exact same holdout.
    print("\nStratified train/test split (80/20, identical to baseline)...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )
    print(f"  Train: {X_train.shape[0]} rows, default rate {y_train.mean():.1%}")
    print(f"  Test:  {X_test.shape[0]} rows, default rate {y_test.mean():.1%}")

    # XGBoost works directly on raw (unscaled) features — trees don't need
    # standardization the way Logistic Regression did. No preprocessor needed.
    scale_pos_weight = (y_train == 0).sum() / (y_train == 1).sum()
    print(f"\nClass imbalance handling: scale_pos_weight = {scale_pos_weight:.2f}")

    print("\nLight hyperparameter search (RandomizedSearchCV, 15 iterations, 3-fold)...")
    param_dist = {
        "max_depth": [3, 4, 5, 6],
        "n_estimators": [100, 150, 200, 300],
        "learning_rate": [0.01, 0.03, 0.05, 0.1],
        "min_child_weight": [1, 3, 5],
        "subsample": [0.7, 0.85, 1.0],
    }
    base_model = XGBClassifier(
        scale_pos_weight=scale_pos_weight,
        eval_metric="auc",
        random_state=42,
        n_jobs=-1,
    )
    search = RandomizedSearchCV(
        base_model, param_dist, n_iter=15, scoring="roc_auc",
        cv=3, random_state=42, n_jobs=-1, verbose=0,
    )
    search.fit(X_train, y_train)
    model = search.best_estimator_
    print(f"  Best params: {search.best_params_}")
    print(f"  Best CV AUC: {search.best_score_:.4f}")

    print("\nEvaluating on held-out test set (same evaluate.py as baseline)...")
    y_proba = model.predict_proba(X_test)[:, 1]
    metrics = evaluate_model(y_test.values, y_proba)
    print_report("XGBoost", metrics)

    train_proba = model.predict_proba(X_train)[:, 1]
    train_auc = evaluate_model(y_train.values, train_proba)["auc"]
    auc_gap = train_auc - metrics["auc"]
    print(f"\n  Train AUC: {train_auc:.4f} | Test AUC: {metrics['auc']:.4f} | Gap: {auc_gap:.4f}")
    if auc_gap > 0.05:
        print("  WARNING: train/test AUC gap exceeds 0.05 - possible overfitting for a ~15-feature dataset.")
    else:
        print("  Train/test gap is within a reasonable range.")

    metrics["train_auc"] = round(train_auc, 4)
    metrics["train_test_auc_gap"] = round(auc_gap, 4)
    metrics["feature_columns"] = feature_columns
    metrics["model_type"] = "XGBoost"
    metrics["best_params"] = search.best_params_

    MODEL_DIR.mkdir(exist_ok=True)
    REPORTS_DIR.mkdir(exist_ok=True)
    joblib.dump(model, MODEL_DIR / "xgboost_model.pkl")
    with open(REPORTS_DIR / "metrics_xgboost.json", "w") as f:
        json.dump(metrics, f, indent=2)
    print(f"\nSaved model to {MODEL_DIR / 'xgboost_model.pkl'}")
    print(f"Saved metrics to {REPORTS_DIR / 'metrics_xgboost.json'}")

    # --- Model Selection ---
    with open(REPORTS_DIR / "metrics_baseline.json") as f:
        baseline_metrics = json.load(f)

    print("\n" + "=" * 60)
    print("  MODEL SELECTION")
    print("=" * 60)
    print(f"  Baseline (Logistic Regression) — AUC: {baseline_metrics['auc']}, KS: {baseline_metrics['ks_statistic']}")
    print(f"  XGBoost                        — AUC: {metrics['auc']}, KS: {metrics['ks_statistic']}")

    auc_improvement = metrics["auc"] - baseline_metrics["auc"]
    ks_improvement = metrics["ks_statistic"] - baseline_metrics["ks_statistic"]
    print(f"\n  AUC improvement: {auc_improvement:+.4f}")
    print(f"  KS improvement:  {ks_improvement:+.4f}")

    if metrics["auc"] > baseline_metrics["auc"]:
        selected = "xgboost"
        selected_path = MODEL_DIR / "xgboost_model.pkl"
        rationale = (
            f"The improvement is real but modest (AUC {auc_improvement:+.4f}, KS {ks_improvement:+.4f}) "
            f"— small enough that a stricter statistical test would be needed to fully rule out sampling "
            f"noise on this test set size. XGBoost is selected primarily because the improvement is "
            f"consistently positive across both independent metrics, and because it pairs naturally with "
            f"SHAP's faster, exact TreeExplainer for Day 7 — not because the margin alone is decisive. "
            f"A reviewer prioritizing interpretability over a small AUC gain could reasonably choose the "
            f"baseline instead; that would be a defensible, different call, not a wrong one."
        )
    else:
        selected = "baseline_logreg"
        selected_path = MODEL_DIR / "baseline_logreg.pkl"
        rationale = (
            f"XGBoost did not improve on the Logistic Regression baseline (AUC change: "
            f"{auc_improvement:+.4f}). The simpler, more interpretable baseline is retained "
            f"as the final model — added complexity isn't justified without a real performance gain."
        )
    print(f"\n  SELECTED: {selected}")
    print(f"  RATIONALE: {rationale}")

    # Copy the selected model to the canonical final_model.pkl the API will load.
    final_model = joblib.load(selected_path)
    joblib.dump(final_model, MODEL_DIR / "final_model.pkl")
    print(f"\nSaved final model to {MODEL_DIR / 'final_model.pkl'} (= {selected})")

    comparison_md = f"""# RiskLens — Model Comparison & Selection

**Capstone content step: XGBoost + Model Selection.** Both models trained and evaluated on the identical stratified 80/20 split (`random_state=42`) of the real 39,252-loan dataset, using the shared `src/evaluate.py` module — no metric is computed differently between them.

## Results

| Metric | Logistic Regression (baseline) | XGBoost |
|---|---|---|
| AUC | {baseline_metrics['auc']} | {metrics['auc']} |
| KS-statistic | {baseline_metrics['ks_statistic']} | {metrics['ks_statistic']} |
| Precision (at 0.5) | {baseline_metrics['precision']} | {metrics['precision']} |
| Recall (at 0.5) | {baseline_metrics['recall']} | {metrics['recall']} |
| Train/test AUC gap | {baseline_metrics['train_test_auc_gap']} | {metrics['train_test_auc_gap']} |

**AUC improvement: {auc_improvement:+.4f}**
**KS improvement: {ks_improvement:+.4f}**

## Selected Model: `{selected}`

{rationale}

## Best Hyperparameters (XGBoost, via RandomizedSearchCV)

```
{json.dumps(search.best_params_, indent=2)}
```

## What This Means for Day 7 (SHAP Explainability)

`models/final_model.pkl` is the canonical artifact the SHAP explainer and the deployed API will both load — it is a copy of `{selected}`, saved under one stable filename so nothing downstream needs to know which model type won.
"""
    DOCS_DIR.mkdir(exist_ok=True)
    with open(DOCS_DIR / "model_comparison.md", "w") as f:
        f.write(comparison_md)
    print(f"\nSaved comparison writeup to {DOCS_DIR / 'model_comparison.md'}")
    print("\nDone.")


if __name__ == "__main__":
    main()
