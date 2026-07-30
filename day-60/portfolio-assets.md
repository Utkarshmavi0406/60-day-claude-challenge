# RiskLens — Portfolio Assets

## Project Description (Short — for a portfolio site/LinkedIn "Featured" section)

RiskLens is an explainable loan default risk predictor trained on real LendingClub data. It doesn't just output a probability, every prediction ships with a ranked, plain-English explanation of what drove the score, powered by SHAP. Built and deployed as a full 10-day sprint: real data cleaning with a documented data leakage catch, an honest baseline-vs-XGBoost model comparison, a tested FastAPI backend, and a live frontend, no shortcuts, every claim in the writeups backed by an actual test run.

## Project Description (Long — for a README/case study intro)

A prediction without an explanation isn't a credit decision, it's a guess with a number attached. RiskLens takes a loan applicant's financial profile and returns a calibrated default probability, a risk tier, and a ranked explanation of exactly which factors drove that score, trained on 39,252 real historical LendingClub loans.

The project was built as a 10-day capstone with a genuine software development lifecycle: product discovery and a written PRD, system design with Mermaid architecture diagrams, a validated database-free architecture, real data cleaning that caught a genuine data leakage bug via correlation analysis, a documented (and honestly modest) model comparison between Logistic Regression and XGBoost, SHAP explainability with an investigated counter-intuitive finding, a rate-limited FastAPI backend verified via real HTTP testing, a frontend with a real bug found and fixed through browser testing, and a live Render deployment debugged from raw error tracebacks.

## Resume Bullet Points

- Built and deployed RiskLens, an explainable ML loan default predictor, training XGBoost on 39,252 real LendingClub loans and integrating SHAP to explain every prediction, achieving 0.706 AUC on held-out data
- Identified and eliminated a genuine data leakage vulnerability during feature engineering by quantifying feature-target correlation (0.495 vs. 0.130), preventing an artificially inflated model
- Designed and shipped a production FastAPI backend with rate limiting, full request validation, and evidence-based input constraints derived from real data distributions
- Built a full-stack ML application end-to-end, data pipeline, model training, explainability layer, REST API, and frontend, and deployed it live on Render, debugging real cross-platform (macOS/Linux) deployment issues
- Applied fair-lending principles to feature selection, excluding geographic proxy variables on regulatory/ethical grounds independent of predictive value

## Interview Talking Points

"Tell me about a bug you're proud of finding." The showState() bug on Day 9, a function comparing full element IDs against short state-name strings that could never match, silently breaking both the loading spinner and error state with zero visible symptom. Found by injecting console tracing into the real running page after a first (wrong) hypothesis about test timing was ruled out. Talk about why silent bugs are worse than crashes, and the discipline of tracing actual execution instead of guessing.

"How do you handle data leakage?" Concrete example: found last_fico_range_high in the LendingClub data, correlating 0.495 with the target versus 0.130 for the legitimate origination-time FICO score, a gap large enough to prove it was capturing post-origination information. Talk about checking correlation deltas rather than trusting column names, and the broader discipline of treating every field as guilty until proven origination-time-only.

"Describe a time you had to push back on your own result." The XGBoost vs. baseline comparison, first draft called a +0.006 AUC improvement "non-trivial," which oversold a genuinely marginal number. Rewrote it to state the improvement plainly, including the case for why a reviewer valuing interpretability could reasonably choose the simpler model instead.

"How do you approach deployment issues?" Three sequential Render deployment failures, missing __init__.py, a macOS/Linux case-sensitivity mismatch, and mismatched file names, each diagnosed from the actual traceback rather than guessed, fixed one at a time, and reconfirmed via a fresh build log before moving to the next.

## Short Demo Script (60-90 seconds)

"This is RiskLens, it predicts loan default risk and explains exactly why, not just a number. [Click a sample applicant, e.g. High Risk] I'll load a real applicant profile from the training data. [Click Predict Risk] In about a second, it returns a 92% default probability, tagged High Risk, and, this is the part that matters, a ranked list of the actual factors driving that score: the interest rate, the loan purpose, income, term length, all in plain English, powered by SHAP running against a real XGBoost model trained on 39,000+ real LendingClub loans. The whole thing is open source, including the write-up of a real data leakage bug I found and fixed while building the training pipeline."

## Suggested GitHub Repository Metadata

Description: Explainable loan default risk predictor — real LendingClub data, XGBoost + SHAP, FastAPI backend, live demo.

Topics/tags: machine-learning, explainable-ai, shap, xgboost, fastapi, credit-risk, fintech, python, data-science, render

Website: https://risklens-ki1d.onrender.com

## Suggested Screenshots for the Portfolio

1. The live app's empty state (shows the design/branding cleanly)
2. A High Risk result with the SHAP factor list visible (the actual product differentiator)
3. The docs/model_comparison.md table (shows quantitative rigor)
4. A snippet of the Day 4 data leakage finding from docs/feature_spec.md (shows the debugging story)
