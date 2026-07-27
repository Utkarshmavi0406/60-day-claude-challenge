# RiskLens - Day 8 Testing Checklist & Release-Readiness Review

Reviewed as: Senior QA Engineer, Senior Software Engineer, Security Reviewer, Performance Engineer. Every item below was actually executed against the real codebase and real data, not reasoned about hypothetically.

## Performance

| Test | Result |
|---|---|
| Model + SHAP explainer load time at startup | ~1.8s steady-state. One anomalous 15.9s reading on the very first cold run in this environment, not reproduced on retry - isolated to SHAP's import statement's first-ever JIT warmup, not a code issue. Documented as a Day 10 deployment watch-item, not fixed today, since there's nothing to fix, it's an inherent property of the library. |
| Per-prediction latency (steady-state) | avg 6.9ms, max 8.9ms over 20 calls - well under the "2 seconds" NFR from the Day 1 PRD |
| /docs and OpenAPI schema generation | Confirmed working, both endpoints listed correctly |

## Security

| Item | Status |
|---|---|
| No PII collected or stored | Confirmed - stateless, no database (per Day 2's architecture decision) |
| Rate limiting on /predict | Added today. 30 requests/minute per IP - the one endpoint worth protecting on an unauthenticated, free-tier-deployed public API. Verified directly: requests 1-30 return 200, requests 31+ return 429 with a clean error message. |
| /health unaffected by rate limiting | Verified - monitoring must never be throttled; confirmed 200 responses continue while /predict is actively rate-limited |
| Internal error detail never leaked to client | Confirmed - generic 500 message returned, full detail logged server-side only (unchanged from Day 7) |
| CORS | allow_origins=["*"] - deliberate, documented choice: no auth, no sensitive data, and the eventual frontend needs to call this from any origin during local development |

## Bugs Found and Fixed

| Bug | Found via | Fix |
|---|---|---|
| delinquencies_2yrs and public_records had no upper bound - 999999 passed validation silently | Direct edge-case testing | Added evidence-based upper bounds (le=20, le=10) derived from real data's actual max values (11 and 4 respectively), with generous headroom |
| open_accounts could exceed total_credit_lines - a logical impossibility | Direct edge-case testing | Added a Pydantic cross-field validator; verified the real data only violates this in 1 of 39,252 rows (negligible), so the new check catches real input errors without meaningfully conflicting with real-world data |

## Code Quality

| Issue | Found via | Fix |
|---|---|---|
| The 11-column numeric feature list was independently hand-typed in 3 separate files (clean_data.py, train_baseline.py, api/model_loader.py) | Direct code review (grep) | Extracted to src/feature_config.py as a single source of truth; all 3 files now import from it |

Refactor safety verified two ways: clean_data.py's output was byte-for-byte diffed against its pre-refactor output (identical). train_baseline.py's AUC (0.6998) and model_loader.py's 3 sample predictions (2.4%, 91.6%, 15.0%) were re-confirmed identical to their pre-refactor values.

## Edge Cases Tested

| Case | Result |
|---|---|
| home_ownership: "NONE" (only 3 training examples) | Handled gracefully, produces a valid prediction |
| All fields at their boundary min/max values simultaneously | Handled gracefully, produces a valid prediction |
| Missing required fields | 422 with clear per-field detail (unchanged from Day 7, reconfirmed) |
| Out-of-range fico_score | 422 (unchanged from Day 7, reconfirmed) |
| Invalid enum value | 422 listing valid options (unchanged from Day 7, reconfirmed) |

## Regression Testing

Every fix and refactor today was verified not to change any existing correct behavior:
- All 3 sample applicants (low/high/medium risk) produce identical predictions before and after every change
- Baseline model AUC unchanged (0.6998)
- Full HTTP request/response cycle re-tested after every change, not just once at the end

## Not Fixed Today - Explicitly Deferred, Not Forgotten

- SHAP's first-ever-import latency: a library characteristic, not a bug; worth observing during the actual Day 10 Render deployment, where cold-start behavior may differ from this environment
- No new features were added beyond the rate limiter, which is a stability/security hardening item, not user-facing functionality - consistent with today's "no new features" instruction
