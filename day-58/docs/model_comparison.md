# RiskLens — Model Comparison & Selection

**Capstone content step: XGBoost + Model Selection.** Both models trained and evaluated on the identical stratified 80/20 split (`random_state=42`) of the real 39,252-loan dataset, using the shared `src/evaluate.py` module — no metric is computed differently between them.

## Results

| Metric | Logistic Regression (baseline) | XGBoost |
|---|---|---|
| AUC | 0.6998 | 0.7057 |
| KS-statistic | 0.297 | 0.3037 |
| Precision (at 0.5) | 0.2356 | 0.2414 |
| Recall (at 0.5) | 0.639 | 0.6452 |
| Train/test AUC gap | -0.0035 | 0.0469 |

**AUC improvement: +0.0059**
**KS improvement: +0.0067**

## Selected Model: `xgboost` — with an honest caveat

**The improvement is real but modest, and worth being precise about rather than oversold.** XGBoost improved AUC by +0.0059 and KS-statistic by +0.0067 over the Logistic Regression baseline — both deltas are small enough that a stricter statistical test (e.g. DeLong's test for AUC comparison) would be needed to fully rule out sampling noise on a 7,851-row test set, which this comparison does not perform.

**Why XGBoost is still selected, despite the marginal margin:**
1. The improvement is consistently positive across *both* independent metrics (AUC and KS), not just one — a coincidental noise pattern is less likely to move both in the same direction.
2. The train/test AUC gap (0.0469) is larger than the baseline's (-0.0035) but still within a normal, non-alarming range for a boosted tree model on ~15 features — there's headroom before this would read as overfitting.
3. XGBoost pairs naturally with SHAP's `TreeExplainer`, which is faster and more exact than `LinearExplainer` would be for the baseline — a genuine practical advantage for Day 7, independent of the raw metric gap.

**Why a reasonable reviewer could disagree:** if interpretability matters more than a ~0.6-point AUC gain — for instance, in a setting with strict model-governance requirements — the Logistic Regression baseline remains a fully defensible choice, and its coefficients are directly interpretable in a way XGBoost's aren't. This project selects XGBoost primarily for the SHAP/TreeExplainer synergy with Day 7's core deliverable, not because the margin alone is decisive.

## Best Hyperparameters (XGBoost, via RandomizedSearchCV)

```
{
  "subsample": 1.0,
  "n_estimators": 200,
  "min_child_weight": 5,
  "max_depth": 4,
  "learning_rate": 0.05
}
```

## What This Means for Day 7 (SHAP Explainability)

`models/final_model.pkl` is the canonical artifact the SHAP explainer and the deployed API will both load — it is a copy of `xgboost`, saved under one stable filename so nothing downstream needs to know which model type won.
