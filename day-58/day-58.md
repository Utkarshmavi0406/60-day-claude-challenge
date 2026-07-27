# Day 58 of 60 - Capstone Day 8: Testing, Debugging & Production Optimization

## A Task That Actually Fit, Unlike Recent Days

Previous mismatches (Day 7's "UI polish" on a nonexistent UI) required accelerating to different work. Today's task, a rigorous QA, security, and performance review, genuinely applied to what already exists: the full data pipeline, both trained models, SHAP explainability, and the FastAPI backend. No mismatch to navigate today, just real, hands-on review work.

## Performance: A Real Number That Turned Out to Be an Artifact

First measurement: model + SHAP explainer startup took 15.9 seconds. Investigated properly rather than either panicking or ignoring it, isolated joblib.load (32ms) and shap.TreeExplainer construction (40ms) individually, both fast. Reran the full startup sequence: 1.778 seconds. The original 15.9s reading was a one-time cache-warming artifact in this sandbox (almost certainly SHAP's underlying numba library JIT-compiling for the first time ever), not a reproducible property of the code. Documented as a Day 10 deployment watch-item rather than something to fix, since there's no actual bug, just a first-run cost worth knowing about before it looks alarming during a real deploy. Per-prediction latency, the number that actually matters for user experience, is excellent: 6.9ms average.

## Two Real Bugs Found Through Actual Edge-Case Testing

Missing upper bounds. delinquencies_2yrs and public_records had no maximum in the Pydantic schema, 999999 passed validation silently and produced a confident-looking but nonsensical prediction. Fixed with evidence-based bounds, not arbitrary ones: checked the real training data's actual maximums (11 and 4, respectively) and set generous but sane limits (20 and 10).

A missing logical constraint. open_accounts could exceed total_credit_lines, impossible in reality (you can't have more currently-open accounts than accounts ever opened). Checked how often real data violates this before adding a strict check: 1 row out of 39,252 (0.0025%, functionally noise). Added a cross-field validator that catches an obvious input error (like a typo) without meaningfully conflicting with real-world data.

## A Real Code Quality Issue, Found by Actually Grep-ing the Codebase

The same 11-column numeric feature list was independently hand-typed in three separate files: clean_data.py, train_baseline.py, and api/model_loader.py. This is exactly the kind of duplication that causes silent, hard-to-find bugs later, a future feature change remembered in two of three places would reintroduce a column-order mismatch with no error message at all. Extracted to src/feature_config.py as a single source of truth.

The refactor's safety was proven, not assumed: clean_data.py's output was byte-for-byte diffed against its pre-refactor output (identical). The baseline model's AUC (0.6998) and all 3 sample applicant predictions were reconfirmed identical after the refactor.

## Security Hardening: Rate Limiting, Added and Verified

/predict has no authentication by design (the PRD explicitly excludes it), which makes it the one endpoint worth protecting from casual abuse once it's live on a free-tier public deploy. Added a 30-requests-per-minute-per-IP limit and verified it directly: fired 35 rapid requests, confirmed the first 30 returned 200 and requests 31-35 returned 429 with a clean error message. Separately confirmed /health stays fully available even while /predict is actively rate-limited, monitoring must never be throttled.

## Deliverables

- src/feature_config.py - new shared single source of truth for feature lists
- src/clean_data.py, src/train_baseline.py, api/model_loader.py - refactored to import from it, zero behavior change (verified)
- api/schemas.py - two real validation bugs fixed
- api/main.py - rate limiting added and tested
- requirements.txt - updated with the new dependency, reinstall-tested
- docs/testing_checklist.md - the complete release-readiness review writeup
- RiskLens_Implementation_Blueprint.md (updated) - notes connecting today's backend QA to the still-pending frontend QA

## Key Learnings

1. A scary-looking performance number deserves investigation before either panic or a workaround. 15.9 seconds looked like a real problem; breaking it into isolated pieces and rerunning revealed it was a one-time artifact. Fixing a phantom problem would have wasted effort; ignoring an unverified scary number would have been irresponsible. Investigating first was the only correct move.

2. Edge-case bugs hide in what a schema doesn't say, not just what it says wrong. Both real bugs found today were sins of omission, a missing upper bound, a missing cross-field check, not incorrect logic. Reviewing "what's the worst input someone could submit" surfaces a different class of bug than reviewing "does the happy path work."

3. A logical constraint's real-data violation rate should inform how strictly to enforce it, not just whether the constraint is theoretically true. Checking that only 1 of 39,252 real rows violated the open-accounts constraint was what made adding a strict check a safe, confident decision rather than a guess.

4. Refactoring for code quality needs the exact same verification rigor as fixing a bug. "It looks cleaner" is not evidence. A byte-for-byte diff and exact-match predictions before and after are.

## Deliverables Checklist

- [x] Performance investigated with real timing, not assumed
- [x] Two real validation bugs found via active edge-case testing and fixed
- [x] Real data checked before adding a strict cross-field constraint
- [x] Code duplication found via direct code review and consolidated
- [x] Refactor safety proven via byte-for-byte diff and exact-match regression testing
- [x] Rate limiting added and verified directly (30 allowed, 31+ blocked)
- [x] Health endpoint confirmed unaffected by rate limiting
- [x] Full HTTP-level regression suite rerun after every change
- [x] Implementation Blueprint updated
- [x] Everything committed to the risklens project repository
- [x] Copies uploaded to today's daily challenge folder
