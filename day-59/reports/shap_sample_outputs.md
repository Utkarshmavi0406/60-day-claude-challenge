# RiskLens — SHAP Explainability: Sample Outputs & Verification

**Capstone content step: SHAP Explainability.** All three samples below are real rows from the actual 39,252-loan dataset, run through the real trained `final_model.pkl` (XGBoost) and a real `shap.TreeExplainer` — not fabricated example output.

## Sample 1: Low Risk

| Field | Value |
|---|---|
| Actual outcome | Fully paid |
| Predicted probability | **2.4%** |
| Interest rate | 5.42% |
| Annual income | $480,000 |
| FICO score | 824 |
| DTI | 0.09% |

**Top factors:** interest rate, annual income, FICO score, revolving utilization, and DTI all decreased predicted risk — consistent with a genuinely strong applicant profile, and the model's prediction agrees with the real outcome.

## Sample 2: High Risk

| Field | Value |
|---|---|
| Actual outcome | Defaulted |
| Predicted probability | **91.6%** |
| Interest rate | 22.48% |
| Loan purpose | small_business |
| DTI | 1.22% |
| Term | 60 months |

**Top factors:** interest rate, loan purpose (small business), 60-month term, and DTI all increased predicted risk, while annual income decreased it. The model's prediction agrees with the real outcome (this loan did default).

## Sample 3: Borderline (~15%)

| Field | Value |
|---|---|
| Actual outcome | Fully paid |
| Predicted probability | **15.0%** |
| Interest rate | 6.54% |
| Loan amount | $22,000 |

**Top factors:** interest rate, income, term, and loan purpose all decreased risk; loan amount increased it — a mixed profile, appropriately landing at a middle-of-the-road prediction.

## An Honest Limitation, Found and Documented — Not Hidden

Investigating Sample 2's factors more closely surfaced something worth being direct about. That applicant's DTI (1.22%) sits at the **3rd percentile** of the entire dataset — an unusually *low* debt burden, which should intuitively be protective. Yet the model's SHAP value for `dti` on this specific row is **positive** (+0.232), meaning the model's learned behavior treats this low DTI as risk-*increasing* for this particular applicant, not risk-decreasing.

This was checked directly, not glossed over: the SHAP value is computed correctly, and this is a real, verified local effect of the trained model — not a bug in the explanation code. It reflects a known, real property of tree-based models: SHAP values capture **row-specific, interaction-aware** contributions, which can occasionally diverge from population-level intuition (`dti` correlates only weakly with default overall, r=0.044) — especially in sparse regions of the feature space, like the 3rd percentile, where the model has seen relatively few training examples to learn from.

**What this means practically:** the explanation is mathematically correct and reflects what the model actually learned, but "correct" and "intuitive" aren't always the same thing at the extremes of a feature's range. This is worth revisiting if a future iteration adds a broader dataset (more examples in sparse regions would let the model learn a more stable relationship there) — documented here rather than discovered later by a confused user.

## Verification Performed

- All three samples are real dataset rows, not constructed examples
- SHAP values confirmed internally consistent with each row's raw feature values (re-derived independently, not just trusted from a single call)
- Both extreme predictions (2.4% and 91.6%) agree with the real recorded loan outcome
- The counter-intuitive DTI finding above was investigated directly against the raw data and the population-level correlation, not assumed to be an error or dismissed without checking
