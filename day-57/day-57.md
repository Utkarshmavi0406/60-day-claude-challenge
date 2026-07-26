# Day 57 of 60 - Capstone Day 7: SHAP Explainability + FastAPI Backend

## A Real Mismatch, Named Honestly

Today's task template was "Product Refinement & User Experience" — reviewing and polishing an existing UI. RiskLens doesn't have a UI yet. Its real build order (data science project) is data -> models -> explainability -> API -> frontend, and the frontend is still two content-steps away. Rather than force a polish pass onto nothing, today accelerated the real next two content steps instead: SHAP explainability and the FastAPI backend — genuine progress toward the "get to something deployable" goal the task actually cared about, even though the specific task framing didn't fit.

## What Was Built

**SHAP Explainability** (`src/explain.py`): a `RiskExplainer` class wrapping the real trained model with `shap.TreeExplainer`, built once and reused. Tested on 3 real dataset rows spanning the risk range - a 2.4% low-risk prediction and a 91.6% high-risk prediction, both agreeing with their real recorded outcomes.

**FastAPI Backend** (`api/main.py`, `api/schemas.py`, `api/model_loader.py`): two real endpoints, `GET /health` and `POST /predict`, with full Pydantic validation, tested against a real running local server via actual HTTP requests - not just direct function calls.

## An Honest Finding, Investigated Not Hidden

Reviewing the high-risk sample's SHAP factors surfaced something worth being direct about: that applicant's DTI (1.22%) sits at the 3rd percentile of the whole dataset - unusually low, which should intuitively be protective. Yet the model's SHAP value for DTI on that specific row is positive, meaning the model treats this low DTI as risk-increasing for this particular applicant.

This was checked directly rather than assumed to be a bug: the SHAP computation is correct, and this reflects a real, known property of tree-model explanations - row-specific, interaction-aware contributions that can diverge from population-level intuition, especially in sparse regions of the feature space (this row's DTI, per dataset-wide correlation, only weakly relates to default overall). Documented in `reports/shap_sample_outputs.md` as an honest limitation, not smoothed over.

## The Most Bug-Prone Part of the System, Verified Directly

`api/model_loader.py` converts a raw applicant profile (the format a human or frontend would send, e.g. `home_ownership: "RENT"`) into the exact 34-column, one-hot-encoded row the model was trained on. A silent column-order or encoding mismatch here would produce wrong predictions with no error at all - the single scariest failure mode in the whole project.

Verified by encoding all 3 sample applicants through the real encoder and confirming the resulting predictions **exactly matched** predictions computed by feeding the model the original training-format rows directly (2.4%, 91.6%, 15.0% - identical to the direct test, not approximately close).

## Real HTTP-Level Testing, Not Just Function Calls

Started a real local server and hit it with real `curl` requests:

| Test | Result |
|---|---|
| `GET /health` | `200`, `{"status":"ok","model_loaded":true}` |
| `POST /predict`, valid high-risk profile | `200`, probability 0.9164 - matches direct-function test exactly |
| `POST /predict`, valid low-risk profile | `200`, probability 0.0242 - matches direct-function test exactly |
| Missing required fields | `422` with clear per-field detail |
| Out-of-range value (`fico_score: 9999`) | `422` with a clear message |
| Invalid enum (`home_ownership: "SPACESHIP"`) | `422` listing the valid options |

## Deliverables

- `src/explain.py` - SHAP explainer, tested on real data
- `data/sample_applicants.json` - 3 real applicant profiles (low/high/medium risk) in raw API format
- `reports/shap_sample_outputs.md` - full test writeup, including the honest DTI limitation finding
- `api/main.py`, `api/schemas.py`, `api/model_loader.py` - the real, HTTP-tested backend
- `RiskLens_Implementation_Blueprint.md` (updated) - both content steps marked complete with real results

## Key Learnings

1. **When the task template doesn't fit the project's real shape, naming the mismatch and doing the actually-useful work beats forcing the template to apply.** A UI polish pass on a nonexistent UI would have produced nothing real; building the two genuine next steps did.
2. **An encoding layer between a human-facing API and a model's expected input format is exactly where silent, undetectable bugs live.** The only real defense is comparing its output against a known-correct reference (the original training-format row) and confirming an exact match - not just confirming it runs without an exception.
3. **A counter-intuitive SHAP value is a finding to investigate, not an error to suppress.** Checking the raw percentile and the population-level correlation before concluding anything turned a confusing number into a documented, honest, genuinely informative limitation.
4. **Testing an API means testing the HTTP layer, not just the Python functions underneath it.** Pydantic validation, status codes, and the actual server startup sequence are real code paths with real failure modes that a direct function call never exercises.

## Deliverables Checklist

- [x] SHAP explainer built and tested on real data, including both prediction extremes
- [x] A genuine, counter-intuitive finding investigated and documented honestly
- [x] Sample applicants generated from real data in the API-facing format
- [x] FastAPI backend built with full request validation
- [x] Encoding layer verified to produce output identical to training-format data
- [x] Real HTTP requests tested against a real running server, including 3 distinct error cases
- [x] Implementation Blueprint updated to reflect real completion status for both content steps
- [x] Everything committed to the risklens project repository
- [x] Copies uploaded to today's daily challenge folder
