# RiskLens — 30-Day Growth Plan

One achievable milestone per day, building only on what actually exists today (real XGBoost model, real SHAP explainer, real FastAPI backend, real deployed frontend on Render, no database). Each week has a theme; each day is small enough to fit a real evening, not a rewrite.

## Week 1: Prove the Model on More Data (Days 1-7)

1. Download the full multi-year LendingClub dataset (2007-2018) from Kaggle.
2. Run src/clean_data.py against it; compare row count, class balance, and null rates against the 2007-only run.
3. Re-validate the feature list from docs/feature_spec.md against the full dataset, confirm no new leakage columns exist in later years.
4. Retrain the Logistic Regression baseline on the full dataset; save as metrics_baseline_v2.json.
5. Retrain XGBoost on the full dataset with the same hyperparameter search process.
6. Add a DeLong's test (or bootstrap CI) to docs/model_comparison.md to properly answer whether the AUC gap is statistically real.
7. Write docs/model_comparison_v2.md documenting the full-data results side by side with the original 2007-only results.

## Week 2: Batch Scoring (Days 8-14)

8. Design the batch endpoint contract: POST /predict-batch, accepting a CSV upload, returning a CSV/JSON of results.
9. Write api/batch_schemas.py, validation for a batch request (row limits, same per-row rules as ApplicantInput).
10. Implement POST /predict-batch in api/main.py, reusing encode_applicant and the explainer per-row.
11. Add rate limiting specifically for the batch endpoint (lower per-minute limit, since each call does more work).
12. Build the frontend batch upload UI: file picker, progress state, downloadable results.
13. Test with a real 100-row CSV; verify total latency and memory behavior on Render's free tier.
14. Update docs/API.md and README.md with the new endpoint.

## Week 3: Persistence and a Real Dashboard (Days 15-21)

15. Stand up a free-tier Postgres instance (Render offers one) and connect it, first real database in the project.
16. Implement the scored_applications table from docs/SCHEMA.md's already-written future schema.
17. Write to the table on every /predict and /predict-batch call (with a clear opt-out/anonymization note, since the PRD's privacy stance needs to hold even with persistence added).
18. Build GET /stats, aggregate score distribution, risk tier breakdown over time.
19. Build the dashboard frontend page: score distribution chart, recent predictions table.
20. Add navigation between the predictor and the dashboard (the project's first real multi-page moment).
21. Load-test the dashboard against a few hundred synthetic historical rows to confirm it stays responsive.

## Week 4: Governance, Fairness, and Polish (Days 22-30)

22. Run a formal fairness check: compare predicted risk distributions across home_ownership and verification_status as rough proxies, documenting findings honestly either way.
23. Write docs/fairness_review.md with the methodology and results, modeled on the same evidence-first tone as docs/feature_spec.md.
24. Consolidate the project's existing manual test scripts into a real tests/ folder using pytest.
25. Add a GitHub Actions workflow that runs the pytest suite on every push.
26. Add model versioning: tag final_model.pkl with a version string, log it in every prediction response.
27. Write a lightweight retraining runbook, the exact steps to retrain and redeploy when new data arrives.
28. Full accessibility pass on the frontend: screen-reader labels, color contrast check on the risk tier badges specifically.
29. Write CASE_STUDY_v2.md incorporating everything built this month, the actual update to the Day 10 case study.
30. Tag v1.1.0, write real release notes, and publish an update post, closing the loop the same way Day 10 did.
