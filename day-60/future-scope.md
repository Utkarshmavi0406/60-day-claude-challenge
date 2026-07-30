# RiskLens — Future Scope

How this specific project could evolve, grounded in what v1.0 actually is: a stateless, single-applicant, explainable default-risk API with no auth and no database — not a generic "add more features" list, but the concrete next steps from exactly where this build stopped.

## 3 Months: Prove the Model Deserves More Data

The single highest-leverage next step isn't a new feature — it's more data. v1.0 trained on 39,252 loans from the 2007 vintage only, obtained from a GitHub mirror since Kaggle wasn't reachable in the build environment. The full LendingClub dataset spans 2007-2018 with millions of loans.

- **Retrain on the full multi-year dataset.** Re-run `src/clean_data.py` against the complete Kaggle download, re-validate the feature list (some fields may behave differently at scale), and re-run the baseline-vs-XGBoost comparison. A larger, more recent dataset is likely to close — or definitively confirm — the modest 0.006 AUC gap between the two models found in `docs/model_comparison.md`.
- **Add a proper statistical test (DeLong's test) to the model comparison**, instead of eyeballing whether a metric delta is "real." `docs/model_comparison.md` already flags this as an open question — this is where it gets answered.
- **Batch CSV scoring** (explicitly deferred in the PRD) — the natural first "real feature" addition, since the modeling and API layers already exist and don't need to change, only a new endpoint and a CSV-parsing frontend flow.

## 6 Months: From Demo to Decision-Support Tool

- **A lightweight database and the portfolio dashboard** (deferred in `docs/SCHEMA.md`'s proposed future schema) — score history, aggregate risk distributions, model drift over time. This is the point where the "no database" architecture decision gets deliberately revisited, not accidentally violated.
- **A formal fairness/disparate-impact audit** — genuinely relevant given this project already made one fair-lending exclusion (`zip_code`) on principle during Day 4. A real audit across the features that remain (e.g., checking whether `home_ownership` or `verification_status` create disparate outcomes across proxies for protected classes) would be the natural, credible extension of that same judgment.
- **Automated CI with a real pytest suite**, replacing the manual/scripted verification this build relied on throughout. Every existing test (encoding correctness, HTTP-level validation, regression checks) already exists as working code in various test scripts from Days 5-9 — the work here is consolidating them into a checked-in, automatically-run suite, not inventing new tests.

## 12 Months: A Credible, Governed Model

- **Model versioning and a real retraining cadence.** Right now, `final_model.pkl` is a single static artifact. A year in, this becomes: scheduled retraining as new loan outcome data becomes available, a version history, and rollback capability if a new model underperforms the one it replaces.
- **User accounts and saved history** (deferred in the PRD) — only worth building once there's a real reason for a specific user to return, which the portfolio-dashboard and batch-scoring features from the 3-6 month milestones would create.
- **A second model family comparison** — e.g., testing whether a more modern gradient boosting library or a calibrated ensemble meaningfully beats the current XGBoost model, using the same honest, margin-aware comparison discipline established in `docs/model_comparison.md` from day one.

## What Deliberately Doesn't Change

No matter which of the above gets built, two Day 1 decisions should hold: **explainability stays a core, always-on feature** (not something that can be toggled off for speed), and **every new metric or claim gets checked against real data before it ships** — the discipline that caught the data leakage on Day 4 and the interaction bug on Day 9 is the actual reason this project is trustworthy, and it shouldn't be the first thing cut under future time pressure.
