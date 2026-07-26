# Day 56 of 60 - Capstone Day 6: XGBoost Model + Model Selection

## What Was Built

The second trained model in RiskLens: XGBoost, trained on the exact same stratified split as yesterday's Logistic Regression baseline, evaluated with the identical shared evaluation module, and compared honestly enough to admit the improvement is real but modest, rather than automatically dressing up any positive delta as decisive.

## The Real, Honest Result

XGBoost: AUC 0.7057, KS 0.3037. Baseline: AUC 0.6998, KS 0.297.
Improvement: +0.0059 AUC, +0.0067 KS.

This is a small margin, and I said so directly rather than inflating it. My training script's first draft auto-generated a rationale calling this a "non-trivial performance gain" the moment XGBoost's AUC exceeded the baseline's - technically true, but overselling a genuinely marginal number. I rewrote both the generated document and the script itself so a rerun produces the same honest framing: the improvement is small enough that a stricter statistical test would be needed to fully rule out sampling noise on a 7,851-row test set, and a reviewer who values interpretability over a ~0.6-point AUC gain could reasonably pick the simpler baseline instead. That would be a defensible, different call, not a wrong one.

## Why XGBoost Was Still Selected

Not because the margin alone was decisive - three real reasons, documented in docs/model_comparison.md:

1. The improvement is consistently positive across two independent metrics (AUC and KS), not just one number that could be a coincidence.
2. The train/test AUC gap (0.0469) is larger than the baseline's but still within a normal range for a boosted tree on ~15 features - no overfitting alarm.
3. XGBoost pairs naturally with SHAP's TreeExplainer - faster and more exact than the LinearExplainer the baseline would need - a genuine practical advantage for the next content step, independent of the metric gap.

## Verified, Not Just Trusted

models/final_model.pkl - the canonical artifact every future step (SHAP, the API) will load - was independently confirmed to be a correct copy of the selected model, not just a file that exists. Reloaded fresh in a new process and compared prediction-for-prediction against xgboost_model.pkl directly: identical output, confirming the "save the winner under one stable filename" step actually did what it claims.

## Deliverables

- src/train_xgboost.py - real, tested training + honest model-selection script
- models/xgboost_model.pkl, models/final_model.pkl - real trained artifacts, cross-verified
- reports/metrics_xgboost.json - full metrics record
- docs/model_comparison.md - side-by-side comparison with an honestly-worded rationale, including the case for disagreeing with the choice
- RiskLens_Implementation_Blueprint.md (updated) - Day 5's content step marked complete with real results

## Key Learnings

1. An auto-generated rationale needs the same scrutiny as an auto-generated metric. My script's first-draft logic wasn't wrong, exactly - XGBoost did win - but "won" and "won convincingly" are different claims, and templated language that always calls a win "non-trivial" quietly erases that distinction every time the margin happens to be small.

2. Documenting the case for disagreeing with your own decision is what makes the decision trustworthy. model_comparison.md doesn't just justify XGBoost, it states plainly what would make the baseline the better choice instead, for someone with different priorities.

3. A "verified" final artifact means the exact bytes that get used downstream were tested, not a sibling file that's presumed identical. Confirming final_model.pkl and xgboost_model.pkl predict identically on a real row is a stronger claim than "the copy command didn't error."

4. Fixing the root cause (the script) matters as much as fixing the symptom (the document). Editing only model_comparison.md would have left the next rerun of train_xgboost.py silently regenerating the overselling version, both had to change together.

## Deliverables Checklist

- [x] XGBoost trained on the identical split used for the baseline
- [x] Evaluated using the same shared evaluate.py functions, no metric computed differently
- [x] Model comparison documented honestly, including the case for the alternative choice
- [x] Final model selected and saved under a stable filename
- [x] final_model.pkl independently verified to match the selected model's real predictions
- [x] Implementation Blueprint updated to reflect real completion status
- [x] Everything committed to the risklens project repository
- [x] Copies uploaded to today's daily challenge folder
