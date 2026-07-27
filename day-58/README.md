# RiskLens

**Explainable Loan Default Predictor** — a real, deployed machine learning system trained on public LendingClub data. Submit an applicant's financial profile and get back a default risk prediction with a plain-English, SHAP-based explanation of exactly what drove the score.

Built as a 10-day capstone project.

🔗 **Live Demo:** _coming Day 10_
📄 **Case Study:** _coming Day 10_

---

## Status

🚧 In active development — **Day 3 of 10: Environment & Repository Setup**

| Day | Focus | Status |
|---|---|---|
| 1 | Product Discovery — PRD, Blueprint, Pitch Deck | ✅ Done |
| 2 | System Design — architecture, schema, API contract, UI wireframes | ✅ Done |
| 3 | Environment & Repository Setup | ✅ Done |
| 4 | Data Exploration & Cleaning Pipeline | ⏳ Next |
| 5 | Baseline Model (Logistic Regression) + Evaluation Framework | ⏳ |
| 6 | XGBoost Model + Model Selection | ⏳ |
| 7 | SHAP Explainability | ⏳ |
| 8 | FastAPI Backend | ⏳ |
| 9 | Frontend | ⏳ |
| 10 | Testing, Deployment & Case Study | ⏳ |

## What This Is

A prediction without an explanation isn't a credit decision — it's a guess with a number attached. RiskLens takes an applicant's financial profile (income, DTI, credit history, loan purpose) and returns:

- A calibrated default probability, trained on real LendingClub loan outcomes
- A clear risk tier (Low / Medium / High)
- A ranked, plain-English explanation of exactly which factors drove that score, powered by SHAP

## Tech Stack

| Layer | Choice |
|---|---|
| Data/ML | Python, pandas, scikit-learn, XGBoost, SHAP |
| API | FastAPI + Uvicorn |
| Frontend | Single self-contained HTML/CSS/JS file |
| Database | None — v1.0 is a stateless prediction API (see `docs/SCHEMA.md`) |
| Hosting | Render.com |

Full rationale in [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

## Local Setup

```bash
git clone https://github.com/Utkarshmavi0406/risklens.git
cd risklens

conda env create -f environment.yml
conda activate risklens
python verify_setup.py
```

`verify_setup.py` should report every dependency imports successfully before continuing.

## Documentation

- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — tech stack, system diagrams, data flow
- [`docs/SCHEMA.md`](docs/SCHEMA.md) — database design decision (none, validated)
- [`docs/API.md`](docs/API.md) — full API contract
- [`docs/UI-WIREFRAMES.md`](docs/UI-WIREFRAMES.md) — user flow and wireframes
- [`docs/PROJECT-STRUCTURE.md`](docs/PROJECT-STRUCTURE.md) — repository layout and rationale

## Scope

**In scope for v1.0:** single-applicant scoring, SHAP explainability on every prediction, a documented baseline-vs-XGBoost model comparison, live deployment.

**Explicitly out of scope for v1.0** (see the PRD for full rationale): batch CSV scoring, a portfolio-level dashboard, user accounts, automated retraining.

---

Built as part of the [60-Day Claude AI Challenge](https://github.com/UtkarshMavi0406/60-day-claude-challenge) · Utkarsh Mavi · 2026
