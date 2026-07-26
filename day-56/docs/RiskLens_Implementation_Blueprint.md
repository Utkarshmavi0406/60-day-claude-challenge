# RiskLens — Implementation Blueprint (Days 2–10)

**Project:** RiskLens — Explainable Loan Default Predictor
**Capstone Day 1 output, updated Day 2.** This is the single source of truth for building v1.0. Each day below is written so a **fresh AI conversation** can pick it up with zero re-planning — paste that day's section (plus the "carry forward" files noted in the previous day's Handoff Notes) into a new chat and start building.

> **Changelog — Day 2 update:** The original "Day 2 — Data Exploration & Architecture" plan has been superseded. Actual Day 2 became a full System Design session (tech stack, architecture, DB, API, UI, project structure) — see `docs/ARCHITECTURE.md`, `docs/SCHEMA.md`, `docs/API.md`, `docs/UI-WIREFRAMES.md`, `docs/PROJECT-STRUCTURE.md`. The lightweight data-exploration tasks originally planned for Day 2 are now folded into Day 3 below, alongside environment/pipeline setup. **Day 10 deployment date is unaffected.**

> **Changelog — Day 4 update:** Actual capstone Day 3 turned out to be environment/repository setup *only* — the data-exploration and cleaning-pipeline work merged into "Day 3" above didn't happen until today (capstone Day 4). Rather than continue renumbering every subsequent day each time the calendar and content drift apart, **calendar day labels below are now treated as "when this stage was actually completed," not a fixed prediction.** The content *sequence* (data cleaning → baseline model → XGBoost → SHAP → API → frontend → testing → deployment) remains the real source of truth for order and dependencies — that hasn't changed and won't. "Day 3" below is now fully complete (data cleaning ran successfully against real data today); the next content step is the baseline model.

**Finalized tech stack** (confirmed Day 2 — see `docs/ARCHITECTURE.md` for full rationale):
- **Data/ML:** Python, pandas, scikit-learn, XGBoost, SHAP, joblib
- **API:** FastAPI + uvicorn, Pydantic for validation
- **Frontend:** a single self-contained HTML/CSS/JS file, served as static files from the FastAPI app
- **Database:** None in v1.0 (confirmed — validated against every PRD user story in `docs/SCHEMA.md`)
- **Authentication:** None in v1.0 (confirmed, per PRD Section 5.2)
- **Hosting:** Render.com free tier for the backend + frontend together
- **Data source:** Kaggle "Lending Club Loan Data" (Accepted Loans), filtered to a manageable subset

**Non-negotiable scope guardrails** (from the PRD — repeat this to yourself every day): single-applicant scoring only, no batch upload, no portfolio dashboard, no auth, no auto-retraining. If a day's work starts drifting toward any of these, stop and refer back to the PRD Section 5.2.

---

## Day 2 — System Design (Complete)

Full technical blueprint completed: finalized tech stack, Mermaid architecture diagrams, database schema decision (none, validated), full API contract for `/predict` and `/health`, user flow + wireframes, and project folder structure. See `docs/ARCHITECTURE.md`, `docs/SCHEMA.md`, `docs/API.md`, `docs/UI-WIREFRAMES.md`, `docs/PROJECT-STRUCTURE.md` for the complete documents.

**Handoff notes for Day 3:** Paste `docs/API.md` (for the exact feature list) and `docs/PROJECT-STRUCTURE.md` into tomorrow's fresh chat, along with this Blueprint.

---

## Day 3 — Design + Setup: Data Exploration & Pipeline (Complete)

**Completed today (capstone Day 4).** Real LendingClub data (39,252 loans, 2007 vintage) was downloaded, the target variable direction was confirmed via correlation analysis (not assumed), and the proposed 16-field feature list from Day 2 was validated against actual data — 14 fields matched directly, 1 was substituted (`grade` → `fico_score`, since letter grade wasn't in this data source), and 1 was dropped (`earliest_credit_line_years`, not available). Three additional columns were found and excluded for specific, evidence-backed reasons: `last_fico_range_high` (confirmed data leakage via correlation comparison), `zip_code` (fair-lending exclusion), and `installment` (collinear with loan amount). Full detail in `docs/feature_spec.md`. `src/clean_data.py` ran successfully end-to-end, producing a zero-null, 39,252-row, 35-column dataset with a 14.4% default rate — inside the range the Day 1 PRD anticipated.

**Handoff to the next content step (baseline model):** `data/processed/clean_loans.csv` is model-ready. Paste `docs/feature_spec.md` and the printed pipeline output into the next session — the cleaning step is done, don't redo it.

<details>
<summary>Original Day 3 plan (for reference — superseded by the results above)</summary>

**Objective:** Explore the LendingClub dataset, confirm the target variable and feature list against real data (proposed yesterday in `docs/API.md`), set up the project environment, and build a repeatable data-cleaning pipeline.

**What I'll learn:** How to validate a proposed feature list against messy real data; how to translate a business question ("will this loan default?") into a supervised learning target without leaking the answer into the features; structuring a real ML project repo instead of one giant notebook.

**Features to build:** `clean_data.py` — a script that loads the raw CSV, applies the target definition, selects and validates the finalized features from `docs/API.md`, handles nulls, encodes categoricals, and writes a clean output file.

**Step-by-step plan:**
1. Download the Kaggle "Lending Club Loan Data" dataset (`accepted_2007_to_2018Q4.csv` or an equivalent pre-filtered subset).
2. Load a sample into pandas; inspect columns, null rates, and `loan_status` value counts.
3. Define the target: `default = 1` if `loan_status` is "Charged Off" or "Default"; `default = 0` if "Fully Paid"; drop every other status (Current, Late, In Grace Period, etc.) from the modeling set entirely — they're not resolved outcomes yet.
4. Validate the 16-field feature list proposed in `docs/API.md` against the real dataset: confirm every field exists (or find its real LendingClub column name), check null rates, and confirm none are post-origination (`total_pymnt`, `recoveries`, `last_pymnt_amnt`, `collection_recovery_fee`, etc. must stay excluded). Adjust the list only if a field turns out to be unavailable or unreliable — document any change.
5. Initialize the Python virtual environment and repo structure per `docs/PROJECT-STRUCTURE.md`.
6. `pip install pandas scikit-learn xgboost shap fastapi uvicorn joblib` — freeze to `requirements.txt`.
7. Write `src/clean_data.py`: load raw CSV -> apply target definition -> select the validated feature list -> impute/handle nulls per column (document the choice — median for numeric, explicit "Unknown" category for categorical) -> encode categoricals -> write to `data/processed/clean_loans.csv`.
8. Run it. Print and eyeball: final row count, class balance, column list, null count (should be zero).
9. Write `docs/feature_spec.md` documenting the final, validated feature list and target definition.
10. Add `.gitignore` (exclude `/data/raw`, `/data/processed`, the venv) and a `README.md` stub.

**Files/folders:**
```
requirements.txt
src/clean_data.py
data/processed/clean_loans.csv   (gitignored)
data/README.md
docs/feature_spec.md
.gitignore
README.md
```

**Tools/libs:** Kaggle (manual download), pandas, scikit-learn (for imputers/encoders if used here).

**Testing tasks:** Sanity-check class balance (% of loans that defaulted — should be a clear minority, roughly 10-20%, not near 50%); assert zero nulls remain in the final output; assert the target column is strictly binary.

**Common issues & debugging tips:**
- The full Kaggle file is large (1-2GB) — download only the accepted-loans file, and use `usecols=` when reading so you're not loading every column into memory.
- LendingClub's real column names don't always match the friendly names used in `docs/API.md` — expect to map 1-2 fields to their actual CSV column names.
- Categorical encoding done here must exactly match what the API does at inference time later — write down the exact encoding scheme in a code comment now, so Day 7 doesn't have to reverse-engineer it.

**End-of-day checklist:**
- [ ] Dataset downloaded and loads in pandas
- [ ] Target variable defined and documented
- [ ] Feature list from `docs/API.md` validated against real data (adjusted if needed, documented if so)
- [ ] Virtual environment + `requirements.txt` working
- [ ] `clean_data.py` runs start to finish, producing a zero-null, binary-target dataset
- [ ] `docs/feature_spec.md` written
- [ ] Repo pushed to GitHub

**Expected project state / screenshots to capture:** Terminal output showing the cleaning script run successfully with row count + class balance printed; the `loan_status` value counts output.

**Handoff notes for Day 4:** Paste `clean_data.py`, `docs/feature_spec.md`, and the printed output summary (row count, class balance, column list) into tomorrow's chat. Day 4 starts model training directly from `data/processed/clean_loans.csv` — the cleaning step is done, don't redo it.

</details>

---


## Day 4 — Implementation: Baseline Model + Evaluation Framework (Complete)

**Completed today.** `src/evaluate.py` was built first as a shared module (AUC, KS-statistic, confusion matrix, precision/recall) so the baseline and the XGBoost model (next content step) are judged identically. `src/train_baseline.py` trained a `LogisticRegression(class_weight='balanced')` on the real 39,252-row dataset from the previous session, using a stratified 80/20 split and a `StandardScaler` fit on train only.

**Real results:** AUC 0.6998, KS-statistic 0.297 on the held-out test set — a credible, realistic baseline for a ~15-feature credit model (not suspiciously perfect, which would suggest leftover leakage; not near-random, which would suggest a broken pipeline). Train AUC (0.6963) and test AUC (0.6998) are essentially identical — no overfitting. Every artifact was independently verified: the saved model and scaler were reloaded fresh (simulating a new process, the same way the API will load them later) and produced a sensible, correctly-ordered prediction on a real row.

**This is the number XGBoost needs to beat, or justify not beating,** in `docs/model_comparison.md` during the next content step.

**Handoff to the next content step (XGBoost + model selection):** `models/baseline_logreg.pkl`, `models/preprocessor.pkl`, `reports/metrics_baseline.json`, and `src/evaluate.py` all carry forward unchanged. `src/train_xgboost.py` will reuse `evaluate.py` directly.

<details>
<summary>Original Day 4 plan (for reference — superseded by the results above)</summary>

**Objective:** Train a Logistic Regression baseline and build the shared evaluation framework both models will be judged against.

**What I'll learn:** Credit-risk-standard model evaluation (AUC, KS-statistic); why establishing a simple baseline before a more complex model is standard practice, not a wasted step.

**Features to build:** train_baseline.py, evaluate.py (a shared, reusable metrics module).

**Step-by-step plan:**
1. Stratified train/test split (e.g. 80/20) on clean_loans.csv.
2. Fit preprocessing (scale numeric, one-hot encode categorical) on the training set only, then transform both sets.
3. Train sklearn.linear_model.LogisticRegression(class_weight='balanced').
4. Build evaluate.py with functions for: AUC, KS-statistic (max separation between the good/bad score distributions), confusion matrix at 0.5, and precision/recall.
5. Run evaluation on the held-out test set; save results to reports/metrics_baseline.json.
6. Save the fitted preprocessor and model with joblib.

**Files/folders:**
```
src/train_baseline.py
src/evaluate.py
models/baseline_logreg.pkl
models/preprocessor.pkl
reports/metrics_baseline.json
```

**Tools/libs:** scikit-learn, joblib.

**Testing tasks:** Confirm AUC > 0.5 (sanity floor — better than random); confirm train and test class balance are similar (rules out an accidental data leak in the split).

**Common issues & debugging tips:**
- Forgetting class_weight='balanced' on an imbalanced target will bias the model toward always predicting "no default."
- Fitting the scaler/encoder on the full dataset instead of train-only is a subtle leakage bug — fit on train, transform both.

**End-of-day checklist:**
- [ ] Baseline model trained
- [ ] evaluate.py returns AUC, KS-statistic, and a confusion matrix
- [ ] metrics_baseline.json saved
- [ ] Model + preprocessor artifacts saved to models/

**Expected project state / screenshots:** Console output showing baseline AUC and KS-statistic — this is the number Day 5's XGBoost model needs to beat (or justify not beating).

**Handoff notes for Day 5:** Paste metrics_baseline.json and evaluate.py into tomorrow's chat. Day 5 trains XGBoost using these exact same evaluation functions for a fair, apples-to-apples comparison.

</details>

---

## Day 5 — Implementation: XGBoost Model + Model Selection (Complete)

**Completed today.** XGBoost trained on the identical stratified split used for the Logistic Regression baseline, evaluated with the same shared `evaluate.py` functions, and compared honestly rather than automatically favoring the higher number.

**Real results:** AUC 0.7057 vs. baseline's 0.6998 (+0.0059), KS-statistic 0.3037 vs. 0.297 (+0.0067). **This is a real but modest improvement** — small enough that a stricter statistical test would be needed to fully rule out sampling noise on a 7,851-row test set. XGBoost was selected primarily because the improvement is consistently positive across both independent metrics, and because it pairs naturally with SHAP's faster, exact `TreeExplainer` for the next content step — not because the margin alone was decisive. `docs/model_comparison.md` documents explicitly that a reviewer prioritizing interpretability over a ~0.6-point AUC gain could reasonably choose the baseline instead, and that would be a defensible, different call.

`models/final_model.pkl` was independently verified to be a correct, working copy of the selected XGBoost model — reloaded fresh and confirmed to produce identical predictions to `xgboost_model.pkl` directly.

**Handoff to the next content step (SHAP explainability):** `models/final_model.pkl` is the canonical artifact. SHAP's `TreeExplainer` will be built against this exact file.

<details>
<summary>Original Day 5 plan (for reference — superseded by the results above)</summary>

**Objective:** Train an XGBoost model, compare it against Day 4's baseline on identical metrics, and select the final model with a documented, defensible rationale.

**What I'll learn:** Gradient boosting fundamentals; how to build a genuine "why this model" interview story instead of blindly picking whichever number is higher.

**Features to build:** train_xgboost.py, docs/model_comparison.md.

**Step-by-step plan:**
1. Train XGBClassifier on the identical train split, using scale_pos_weight to handle class imbalance.
2. Light hyperparameter tuning — a small manual grid or a quick RandomizedSearchCV over max_depth, n_estimators, learning_rate. Keep this fast; this is not the day to chase a leaderboard.
3. Evaluate with the same evaluate.py from Day 4 on the same test set.
4. Write model_comparison.md: both models' metrics side by side, plus a one-paragraph justification for the final choice (e.g., "XGBoost improved AUC by X points and KS by Y points, justifying the added complexity over the simpler baseline" — or the reverse, if interpretability wins out).
5. Save the chosen model as models/final_model.pkl — a single canonical artifact the API will load, regardless of which model won.

**Files/folders:**
```
src/train_xgboost.py
models/xgboost_model.pkl
models/final_model.pkl
reports/metrics_xgboost.json
docs/model_comparison.md
```

**Tools/libs:** xgboost, scikit-learn (RandomizedSearchCV).

**Testing tasks:** Re-run evaluate.py on both models against the identical test set; load final_model.pkl fresh and confirm it predicts correctly on one sample row (catches a serialization mistake early).

**Common issues & debugging tips:**
- Watch the train-vs-test AUC gap — a large gap means overfitting, likely from too many estimators or too much depth for a ~15-20 feature dataset.
- XGBoost's categorical handling differs from what was used for the Logistic Regression preprocessor — make sure final_model.pkl's expected input format is documented clearly, since Day 6 and Day 7 both depend on it.

**End-of-day checklist:**
- [ ] XGBoost trained and evaluated on identical metrics to baseline
- [ ] model_comparison.md written with a clear final decision
- [ ] final_model.pkl saved and sanity-tested on one row

**Expected project state / screenshots:** model_comparison.md rendered, showing both models' AUC/KS side by side and the final decision.

**Handoff notes for Day 6:** Paste model_comparison.md and confirm the exact path/format of final_model.pkl into tomorrow's chat. Day 6 adds SHAP explainability on top of this exact final model — no retraining.

</details>

---

## Day 6 — Implementation: SHAP Explainability

**Objective:** Add SHAP-based explainability so every prediction comes with a ranked, plain-English list of what drove the score.

**What I'll learn:** How SHAP values work conceptually (attributing a prediction to individual features); how to translate a technical explanation into language a non-technical interviewer or stakeholder can actually follow.

**Features to build:** src/explain.py — a function that takes one applicant's feature row and returns the predicted probability plus the top 5 contributing factors, each with direction (increased/decreased risk).

**Step-by-step plan:**
1. Build a SHAP explainer against final_model.pkl (TreeExplainer if XGBoost was chosen, LinearExplainer if Logistic Regression was chosen).
2. Write explain_prediction(applicant_features) -> returns {probability, top_factors: [{feature, direction, magnitude, plain_english_sentence}, ...]}.
3. Test on 3-4 hand-picked sample applicants: one clearly low-risk, one clearly high-risk, one borderline. Sanity-check that the explanations make real-world business sense (e.g., high DTI should push risk up, not down).
4. Save these as data/sample_applicants.json — Day 8's frontend will reuse these exact profiles as quick-select demo buttons.

**Files/folders:**
```
src/explain.py
data/sample_applicants.json
reports/shap_sample_outputs.md
```

**Tools/libs:** shap.

**Testing tasks:** Confirm SHAP values are internally consistent with the model's raw prediction (a basic sanity check most SHAP tutorials cover); manually review all 3-4 sample explanations for business plausibility, not just that the code runs.

**Common issues & debugging tips:**
- The explainer needs features in the exact same order and encoding as training — a mismatch produces explanations that run without error but are quietly meaningless.
- SHAP explainer initialization can be slow — build it once and reuse it, don't reconstruct it per prediction (this matters a lot once it's behind an API tomorrow).

**End-of-day checklist:**
- [ ] explain.py returns probability + ranked, human-readable factors
- [ ] Tested and manually reviewed on 3-4 sample applicants
- [ ] sample_applicants.json saved for Day 8 reuse

**Expected project state / screenshots:** Console output showing one sample applicant's full prediction + explanation.

**Handoff notes for Day 7:** Paste explain.py and one full example output into tomorrow's chat. Day 7 wraps this exact function in a FastAPI endpoint — the explanation logic itself is done.

---

## Day 7 — Implementation: FastAPI Backend

**Objective:** Wrap the trained model and explainability function in a FastAPI backend with a clean, validated prediction endpoint.

**What I'll learn:** Building and testing a real ML-serving API; input validation patterns for a model endpoint that will eventually face public traffic.

**Features to build:** api/main.py with a POST /predict endpoint; a Pydantic schema matching the finalized feature list; a GET /health endpoint.

**Step-by-step plan:**
1. Define a Pydantic model, ApplicantInput, with every feature from feature_spec.md, correctly typed (float, int, or a literal/enum for categoricals).
2. Write POST /predict: validate input -> run through the saved preprocessor -> final_model.pkl -> explain.py -> return JSON {probability, risk_tier, top_factors}.
3. Define risk tiers using the test set's score distribution from Day 5 as a guide (e.g., Low < 10%, Medium 10-30%, High > 30% — pick real thresholds, don't guess round numbers).
4. Add GET /health for deployment monitoring.
5. Add CORS middleware (the frontend will call this from a browser tomorrow).
6. Load the model/preprocessor once at app startup, not per-request.
7. Test locally via FastAPI's auto-generated /docs UI using the sample applicants from Day 6.

**Files/folders:**
```
api/main.py
api/schemas.py
api/model_loader.py
```

**Tools/libs:** fastapi, uvicorn, pydantic.

**Testing tasks:** Hit /predict with all sample applicants via /docs; confirm /health returns 200; test one deliberately invalid input (a missing required field) and confirm a clean 422 response, not a server crash.

**Common issues & debugging tips:**
- Loading the model fresh on every request is slow and wasteful — load once at startup and keep it in memory.
- CORS errors will surface tomorrow if allow_origins isn't set correctly today — configure it now even though there's no frontend yet.

**End-of-day checklist:**
- [ ] /predict works end-to-end for all sample applicants
- [ ] /health returns 200
- [ ] Invalid input handled gracefully (422, not a crash)
- [ ] CORS configured

**Expected project state / screenshots:** Screenshot of the FastAPI /docs page showing a successful /predict call and its JSON response.

**Handoff notes for Day 8:** Paste api/main.py and one sample request/response pair into tomorrow's chat. Day 8 builds the frontend that calls this exact endpoint — the backend contract is now fixed.

---

## Day 8 — Implementation: Frontend

**Objective:** Build a polished single-page HTML/CSS/JS form that collects applicant details and displays the prediction and explanation live.

**What I'll learn:** Connecting a static frontend to a real backend API; presenting a model's probability + SHAP output in a way a non-technical visitor understands in seconds.

**Features to build:** frontend/index.html — form matching the feature list, sample-applicant quick-select buttons, and a results panel.

**Step-by-step plan:**
1. Build the form with one input per feature in feature_spec.md (numeric inputs, dropdowns for categoricals).
2. Add 3-4 "Load Sample Applicant" buttons using sample_applicants.json from Day 6 — this is what makes the live demo actually usable by a recruiter with zero domain knowledge.
3. On submit: fetch() a POST to /predict, show a loading state while waiting.
4. Render the response: a color-coded risk tier badge, the probability as a simple bar/gauge, and the ranked factors list with clear up/down direction icons.
5. Style it to read as a real credit tool — clean and professional, not playful.
6. Handle API errors (network failure, validation error) with a visible, specific message — never a silent failure.

**Files/folders:**
```
frontend/index.html
frontend/README.md   (notes the API base URL config point)
```

**Tools/libs:** Vanilla HTML/CSS/JS, fetch.

**Testing tasks:** Every sample-applicant button produces a sensible result; a manually-entered edge case (very high income + very high DTI) behaves reasonably; stop the backend and confirm the error state displays properly instead of hanging silently.

**Common issues & debugging tips:**
- A wrong API base URL is the most common CORS-looking bug that's actually just a typo.
- Skipping the loading state makes the UI feel broken during the ~1 second the API call takes — don't skip it.

**End-of-day checklist:**
- [ ] Form built with every required field
- [ ] Sample applicant quick-select working
- [ ] Live prediction + explanation rendering correctly
- [ ] Error state tested and working

**Expected project state / screenshots:** The full form plus a rendered prediction result (with SHAP factors visible) for at least one sample applicant.

**Handoff notes for Day 9:** Paste frontend/index.html and a screenshot into tomorrow's chat. Day 9 is systematic testing and polish — no new features are planned.

---

## Day 9 — Testing: End-to-End QA & Polish

**Objective:** Systematically test the full pipeline end-to-end, fix what's broken, and polish the UI. No new features today.

**What I'll learn:** What "production-ready" actually means for a small deployed tool; systematic QA habits instead of ad hoc clicking around.

**Features to build:** None — bug fixes and polish only.

**Step-by-step plan:**
1. Write a short testing_checklist.md: all sample applicants, edge-case inputs (min/max values, an unusual combination), mobile responsiveness, and slow-network behavior (throttle in devtools).
2. Execute the checklist; fix every bug found.
3. Add basic frontend-side input validation for a smoother experience, on top of the API's existing validation.
4. Polish visual details: consistent spacing, color contrast, loading/error states, and a short "About this tool" blurb noting it's a portfolio project trained on public data — this sets correct expectations for a recruiter visiting cold.
5. Finalize the top-level README.md: what this is, how it works, the tech stack, how to run it locally, and a placeholder for the live demo link (filled in tomorrow).

**Files/folders:**
```
README.md            (finalized)
docs/testing_checklist.md
```

**Tools/libs:** Browser devtools (responsive mode, network throttling).

**Testing tasks:** Execute the full testing_checklist.md and check off every item — this whole day is the testing task.

**Common issues & debugging tips:**
- Mobile layout breaking on narrow screens is easy to miss if you only ever test at desktop width.
- Error states that were built on Day 8 but never actually triggered until now often have small bugs — this is exactly why today exists.

**End-of-day checklist:**
- [ ] Full testing checklist executed
- [ ] All found bugs fixed
- [ ] README.md finalized
- [ ] UI polish pass complete

**Expected project state / screenshots:** A fully working local app; screenshots of both a successful prediction and a properly-handled error state.

**Handoff notes for Day 10:** Paste the finalized README.md and testing_checklist.md (with results) into tomorrow's chat. Day 10 is deployment only — no further feature or bug work is planned; if something new is found during deployment, fix only what blocks shipping.

---

## Day 10 — Deployment: Ship v1.0 Live

**Objective:** Deploy the backend and frontend to a live public URL, run final smoke tests against production, and publish the portfolio case study.

**What I'll learn:** Deploying a Python ML API to real hosting; writing a case study that communicates a technical project to a non-technical interviewer.

**Features to build:** None — deployment configuration only.

**Step-by-step plan:**
1. Choose hosting (Render.com free tier recommended for FastAPI): create a Web Service, connect the GitHub repo, set the start command (uvicorn api.main:app --host 0.0.0.0 --port $PORT).
2. Serve frontend/index.html as a static file directly from the FastAPI app — this sidesteps CORS entirely and keeps deployment to one service instead of two.
3. Push the final commit, trigger the deploy, and watch build logs for errors (usually a missing entry in requirements.txt).
4. Re-run the exact testing_checklist.md from Day 9 — this time against the live URL, not localhost.
5. Write CASE_STUDY.md (or expand README.md): the problem, the approach, key results (AUC/KS numbers), and what you'd build next. This is the document you actually link from your resume or LinkedIn.
6. Take final screenshots of the live, deployed app for the portfolio.
7. Save the live link somewhere durable — pin it to your GitHub profile, add it to your resume/LinkedIn.

**Files/folders:**
```
Procfile (or render.yaml)
CASE_STUDY.md
README.md   (final version, live link at the top)
```

**Tools/services:** Render.com (or Railway) free tier, Git.

**Testing tasks:** Full smoke test on the live URL — every sample applicant, at least one manual entry, and a check on an actual phone if possible.

**Common issues & debugging tips:**
- Free-tier hosting cold-starts — the first request after inactivity can take 30+ seconds. Document this explicitly in the case study so a visitor doesn't think it's broken.
- A missing dependency in requirements.txt is the most common deploy failure — check it's complete and pinned before pushing.
- Forgetting to update the frontend's API base URL from localhost to the live backend URL is an easy last-minute miss.

**End-of-day checklist:**
- [ ] Backend deployed and live
- [ ] Frontend accessible and working end-to-end on the live URL
- [ ] Full smoke test passed on production
- [ ] CASE_STUDY.md written
- [ ] Live link saved and shared

**Expected project state / screenshots:** The live public URL, working end-to-end — this is the screenshot that goes in the portfolio.

**Handoff notes:** None — this is v1.0, shipped. Future Scope items (batch scoring, portfolio dashboard, drift monitoring, fairness audit) are already documented in the PRD Section 10 for anyone — including future you — picking this project back up.
