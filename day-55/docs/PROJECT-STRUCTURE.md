# RiskLens — Project Structure

```
risklens/
├── README.md                      Project overview, live link (added Day 10), local setup instructions
├── .gitignore                     Excludes venv, raw/processed data, __pycache__
├── requirements.txt                Pinned Python dependencies (Day 3)
├── Procfile                       Render start command (Day 10)
├── CASE_STUDY.md                  Portfolio write-up: problem, approach, results (Day 10)
│
├── data/
│   ├── README.md                  Data source + manual download instructions
│   ├── raw/                       Gitignored — the downloaded LendingClub CSV lives here locally only
│   ├── processed/                 Gitignored — clean_loans.csv, the model-ready dataset
│   └── sample_applicants.json     Committed — 3-4 preset profiles used by both the frontend and testing
│
├── src/                           Offline pipeline — runs on your laptop, never on the deployed server
│   ├── clean_data.py              Raw CSV -> clean, leakage-free, encoded dataset (Day 3)
│   ├── train_baseline.py          Logistic Regression training (Day 4)
│   ├── train_xgboost.py           XGBoost training (Day 5)
│   ├── evaluate.py                Shared metrics module: AUC, KS-statistic, confusion matrix (Day 4)
│   └── explain.py                 SHAP explainer wrapper (Day 6)
│
├── models/                        Trained artifacts — committed to the repo, loaded by the API at startup
│   ├── preprocessor.pkl           Fitted scaler/encoder (Day 4)
│   ├── baseline_logreg.pkl        Logistic Regression artifact (Day 4)
│   ├── xgboost_model.pkl          XGBoost artifact (Day 5)
│   └── final_model.pkl            Whichever model was selected — this is what the API actually loads (Day 5)
│
├── api/                           The live backend — this is what Render deploys and runs
│   ├── main.py                    FastAPI app: POST /predict, GET /health (Day 7)
│   ├── schemas.py                 Pydantic request/response models (Day 7)
│   └── model_loader.py            Loads model + preprocessor once at startup, not per-request (Day 7)
│
├── frontend/                      Served as static files by the same FastAPI app (Day 8, deployed Day 10)
│   ├── index.html                 The entire UI — form, results, error states
│   └── README.md                  Notes the API base URL configuration point
│
├── reports/                       Generated outputs, not hand-written — evidence for the case study
│   ├── metrics_baseline.json      (Day 4)
│   ├── metrics_xgboost.json       (Day 5)
│   └── shap_sample_outputs.md     (Day 6)
│
└── docs/                          Design and process documentation — this folder
    ├── architecture.md            = ARCHITECTURE.md (today)
    ├── feature_spec.md            Finalized Day 3, validated against real data
    ├── model_comparison.md        Written Day 5
    ├── testing_checklist.md       Written Day 9
    ├── SCHEMA.md                  Today
    ├── API.md                     Today
    ├── UI-WIREFRAMES.md           Today
    └── PROJECT-STRUCTURE.md       Today (this file)
```

## Why This Structure

- **`src/` vs `api/` is the most important split in this project.** `src/` is the offline, one-time model-training pipeline that runs on a laptop and produces files. `api/` is the always-running deployed service that only ever *reads* those files. Keeping them in separate folders makes it visually obvious that training and serving are different concerns with different lifecycles — the API never re-trains anything.
- **`models/` holds committed artifacts, not gitignored ones.** Unlike raw/processed data (which is large and regenerable, so it's gitignored), the trained `.pkl` files are small, are the actual product being deployed, and need to travel with the repo to Render.
- **`docs/` is where every planning document lives, dated by which capstone day produced it** — this mirrors the actual build process and makes the repo self-documenting for anyone (including future you) picking the project back up.
- **`frontend/` is deliberately not a separate deployment** — serving it as static files from the FastAPI app (decided in today's Architecture) means one Render service, not two, and no CORS configuration to maintain.
