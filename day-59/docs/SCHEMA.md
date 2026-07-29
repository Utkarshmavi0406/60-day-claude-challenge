# RiskLens — Database Schema

## v1.0 Decision: No Database

RiskLens v1.0 uses no database. This is a deliberate architecture decision confirmed today, not an oversight — validated below against every user-facing story in the Day 1 PRD.

## Validation Against PRD User Stories

| PRD User Story / Requirement | Needs Persistent Storage? | Why |
|---|---|---|
| Visitor submits an applicant's details and gets a prediction | No | Single stateless request/response — nothing needs to be remembered after the response is sent |
| Visitor can adjust inputs and resubmit to see how the prediction changes | No | Handled entirely in frontend memory (the form's current values); each resubmit is an independent API call |
| Visitor clicks a "sample applicant" preset | No | Sample applicants are a static JSON file (data/sample_applicants.json) shipped with the frontend, not stored per-user |
| Model artifacts (trained model, preprocessor) must be available to the API | No, file storage not a database | These are static files (.pkl) loaded into memory once at server startup, not queried per-request |
| PRD 5.2: Batch CSV scoring | Explicitly out of scope for v1.0 | Would need storage for uploaded files/results — deferred |
| PRD 5.2: Portfolio-level dashboard (score distributions over time) | Explicitly out of scope for v1.0 | Would need a table of historical scored applications — deferred |
| PRD 5.2: User accounts / saved history | Explicitly out of scope for v1.0 | Would need a users table and per-user records — deferred |

Conclusion: every v1.0 user story is satisfiable with zero persistent storage. Adding a database now would be scope creep the PRD itself already ruled out.

## What "Data" Actually Exists in v1.0

| Data | Where it lives | Persistent? |
|---|---|---|
| Raw LendingClub training data | data/raw/ (gitignored, local only) | Only during model training (Day 3-6), not shipped or served |
| Cleaned training dataset | data/processed/clean_loans.csv (gitignored) | Same as above |
| Trained model + preprocessor | models/*.pkl (committed to repo) | Yes, as static files — not a database |
| Sample applicant presets | data/sample_applicants.json (committed to repo) | Yes, as a static file |
| A single prediction request/response | In-memory only, for the duration of one HTTP request | No — never written to disk or a database |

## Future Scope: Proposed Schema (Not Built in v1.0)

Documented here so a future iteration doesn't have to design this from scratch — explicitly not part of this capstone's v1.0 build.

Table: scored_applications  (Future Scope, supports the Portfolio Dashboard)
- id: UUID PRIMARY KEY
- submitted_at: TIMESTAMP
- input_features: JSONB, the applicant fields submitted
- predicted_probability: FLOAT
- risk_tier: VARCHAR(10)
- model_version: VARCHAR(20), which model artifact scored this

Table: users  (Future Scope, supports accounts/history)
- id: UUID PRIMARY KEY
- email: VARCHAR UNIQUE
- created_at: TIMESTAMP

Relationship: scored_applications.user_id references users.id (nullable, so anonymous v1.0-style use still works even after accounts exist)

This sketch would only get built alongside the Future Scope items already listed in the PRD (batch scoring, portfolio dashboard, user accounts) — not before.
