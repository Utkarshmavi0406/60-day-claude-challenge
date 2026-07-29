"""
RiskLens — Shared Evaluation Module

Provides consistent evaluation metrics for any classifier trained in this
project, so the baseline (Logistic Regression) and later XGBoost model are
judged on an identical, fair basis. Credit-risk-standard metrics: AUC and
the KS-statistic, alongside a standard confusion matrix and precision/recall.

Used by src/train_baseline.py today, and by src/train_xgboost.py in the
next content step — do not duplicate this logic elsewhere.
"""
import numpy as np
from sklearn.metrics import roc_auc_score, roc_curve, confusion_matrix, precision_score, recall_score


def compute_ks_statistic(y_true, y_proba):
    """KS-statistic: the maximum separation between the cumulative
    distributions of predicted scores for the positive (default) and
    negative (non-default) classes. Standard credit risk model metric —
    higher is better, 0 = no separation, 1 = perfect separation.
    """
    fpr, tpr, _ = roc_curve(y_true, y_proba)
    ks = np.max(np.abs(tpr - fpr))
    return float(ks)


def evaluate_model(y_true, y_proba, threshold=0.5):
    """Compute the full evaluation suite for a binary classifier's
    predicted probabilities against true labels.

    Returns a plain dict — JSON-serializable, meant to be saved directly
    to reports/metrics_*.json for side-by-side comparison across models.
    """
    y_pred = (y_proba >= threshold).astype(int)

    auc = float(roc_auc_score(y_true, y_proba))
    ks = compute_ks_statistic(y_true, y_proba)

    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    precision = float(precision_score(y_true, y_pred, zero_division=0))
    recall = float(recall_score(y_true, y_pred, zero_division=0))

    return {
        "auc": round(auc, 4),
        "ks_statistic": round(ks, 4),
        "threshold": threshold,
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "confusion_matrix": {
            "true_negative": int(tn),
            "false_positive": int(fp),
            "false_negative": int(fn),
            "true_positive": int(tp),
        },
        "n_samples": int(len(y_true)),
        "n_positive": int(np.sum(y_true)),
    }


def print_report(name, metrics):
    print(f"\n{'='*50}")
    print(f"  {name}")
    print(f"{'='*50}")
    print(f"  AUC:          {metrics['auc']}")
    print(f"  KS-statistic: {metrics['ks_statistic']}")
    print(f"  Precision:    {metrics['precision']}  (at threshold {metrics['threshold']})")
    print(f"  Recall:       {metrics['recall']}  (at threshold {metrics['threshold']})")
    cm = metrics["confusion_matrix"]
    print(f"  Confusion matrix: TN={cm['true_negative']} FP={cm['false_positive']} "
          f"FN={cm['false_negative']} TP={cm['true_positive']}")
