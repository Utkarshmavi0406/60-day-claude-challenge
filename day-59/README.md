# RiskLens

**Explainable Loan Default Predictor** — a real, deployed machine learning system trained on public LendingClub data. Submit an applicant's financial profile and get back a default risk prediction with a plain-English, SHAP-based explanation of exactly what drove the score.

Built as a 10-day capstone project.

Live Demo: added after Day 10 deployment - see below for local instructions in the meantime
Case Study: coming Day 10

---

## Status

In active development - Day 9 of 10: Launch & Production Readiness

| Day | Focus | Status |
|---|---|---|
| 1 | Product Discovery - PRD, Blueprint, Pitch Deck | Done |
| 2 | System Design - architecture, schema, API contract, UI wireframes | Done |
| 3 | Environment & Repository Setup | Done |
| 4 | Data Exploration & Cleaning Pipeline (real LendingClub data) | Done |
| 5 | Baseline Model - Logistic Regression (AUC 0.6998) | Done |
| 6 | XGBoost Model + Model Selection (AUC 0.7057) | Done |
| 7 | SHAP Explainability + FastAPI Backend | Done |
| 8 | Testing, Debugging & Production Optimization | Done |
| 9 | Frontend + Launch Readiness | Done |
| 10 | Final Deployment & Case Study | Next |

## What This Is

A prediction without an explanation isn't a credit decision - it's a guess with a number attached. RiskLens takes an applicant's financial profile (income, DTI, credit history, loan purpose) and returns:

- A calibrated default probability, trained on real LendingClub loan outcomes
- A clear risk tier (Low / Medium / High)
- A ranked, plain-English explanation of exactly which factors drove that score, powered by SHAP

## Tech Stack

| Layer | Choice |
|---|---|
| Data/ML | Python, pandas, scikit-learn, XGBoost, SHAP |
| API | FastAPI + Uvicorn, rate-limited via slowapi |
| Frontend | Single self-contained HTML/CSS/JS file, served as static files from the same FastAPI app |
| Database | None - v1.0 is a stateless prediction API (see docs/SCHEMA.md) |
| Hosting | Render.com |

Full rationale in [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Local Setup

```bash
git clone https://github.com/Utkarshmavi0406/risklens.git
cd risklens

conda env create -f environment.yml
conda activate risklens
python verify_setup.py

uvicorn api.main:app --reload --port 8000
```

Open http://127.0.0.1:8000 in your browser - the full app (form + live predictions) runs from that one URL. Interactive API docs are at http://127.0.0.1:8000/docs.

## Documentation

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) - tech stack, system diagrams, data flow
- [docs/SCHEMA.md](docs/SCHEMA.md) - database design decision (none, validated)
- [docs/API.md](docs/API.md) - full API contract
- [docs/UI-WIREFRAMES.md](docs/UI-WIREFRAMES.md) - user flow and wireframes
- [docs/PROJECT-STRUCTURE.md](docs/PROJECT-STRUCTURE.md) - repository layout and rationale
- [docs/feature_spec.md](docs/feature_spec.md) - feature validation against real data
- [docs/model_comparison.md](docs/model_comparison.md) - baseline vs. XGBoost, with an honest margin analysis
- [docs/testing_checklist.md](docs/testing_checklist.md) - Day 8 release-readiness review

## Scope

In scope for v1.0: single-applicant scoring, SHAP explainability on every prediction, a documented baseline-vs-XGBoost model comparison, live deployment.

Explicitly out of scope for v1.0 (see the PRD for full rationale): batch CSV scoring, a portfolio-level dashboard, user accounts, automated retraining.

## License

MIT - see [LICENSE](LICENSE).

---

Built as part of the [60-Day Claude AI Challenge](https://github.com/UtkarshMavi0406/60-day-claude-challenge) - Utkarsh Mavi - 2026
