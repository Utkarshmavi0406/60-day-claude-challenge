# Day 55 of 60 - Capstone Day 5: Baseline Model + Evaluation Framework

## What Was Built

The first trained model in RiskLens: a Logistic Regression baseline, trained and evaluated against the real 39,252-loan dataset validated in the previous session, plus a shared evaluation module that the next model (XGBoost) will reuse for a fair, apples-to-apples comparison.

## Real Results, Independently Verified

**AUC: 0.6998, KS-statistic: 0.297** on a held-out test set (20% of the real data, stratified split). These numbers matter for what they *aren't*, as much as what they are: not suspiciously close to 1.0 (which would suggest a leakage column survived from yesterday's cleaning), and not close to 0.5 (which would suggest a broken pipeline). This is a credible, realistic result for a ~15-feature linear model on real credit data.

**Train AUC (0.6963) vs. test AUC (0.6998)** are essentially identical — actually slightly higher on test, well within normal noise. No overfitting, which is expected for a linear model with this few features, but confirmed rather than assumed.

**Every saved artifact was independently verified**, not just trusted because training completed without an error. The model and scaler were reloaded in a fresh process — the same way the future API will load them — and produced a sensible, correctly-shaped prediction on a real row from the dataset, with the exact feature column order preserved and confirmed to match training.

## Why the Evaluation Module Came First

`src/evaluate.py` was built and tested before `src/train_baseline.py` used it, specifically so the *next* model (XGBoost) has zero reason to compute its metrics any differently. Both AUC and the KS-statistic (a credit-risk-standard metric measuring the maximum separation between good and bad account score distributions) are implemented once, shared, and will produce numbers directly comparable to today's baseline without any risk of a subtly different calculation method sneaking in later.

## Deliverables

- `src/evaluate.py` — the shared metrics module (AUC, KS-statistic, confusion matrix, precision/recall), used by every model trained in this project from here forward
- `src/train_baseline.py` — the real, tested training script
- `models/baseline_logreg.pkl`, `models/preprocessor.pkl` — real trained artifacts, verified to reload and predict correctly
- `reports/metrics_baseline.json` — the full metrics record, including the feature column order the API will need to replicate later
- `RiskLens_Implementation_Blueprint.md` (updated) — Day 4's content step marked complete with real results

## Key Learnings

1. **A baseline's job is to be a believable number, not an impressive one.** An AUC of 0.70 isn't exciting, but it's exactly the kind of result that earns trust — a suspiciously high number on the first real model would have been a red flag for leftover leakage, not a win.
2. **"The model trained without an error" and "the model artifacts actually work" are different claims.** Only reloading the saved `.pkl` files in a fresh process and generating a real prediction confirms the second one — training completing successfully says nothing about whether `joblib.dump` and `joblib.load` round-trip correctly.
3. **Building the shared evaluation module before the first model, not alongside it, pays off immediately.** Because `evaluate.py` doesn't know or care which model produced the probabilities it's scoring, there's no possibility of the baseline and XGBoost being judged on subtly different math later — a structural guarantee, not a discipline I have to remember to maintain.
4. **The train/test AUC gap is itself a piece of evidence, not just a formality.** A near-zero gap here is expected for a simple linear model and confirms nothing surprising happened in the split or the fit — a small, boring, correct result is still worth actively checking, not just assuming.

## Deliverables Checklist

- [x] Shared evaluation module built and tested (AUC, KS-statistic, confusion matrix, precision/recall)
- [x] Baseline Logistic Regression trained on real data with a stratified train/test split
- [x] Preprocessor fit on train only, applied to both splits correctly
- [x] Metrics computed and sanity-checked (AUC > 0.5 floor, train/test gap reviewed)
- [x] Model and preprocessor artifacts saved via joblib
- [x] Artifacts independently reloaded fresh and verified to predict correctly
- [x] Implementation Blueprint updated to reflect real completion status
- [x] Everything committed to the risklens project repository
- [x] Copies uploaded to today's daily challenge folder
