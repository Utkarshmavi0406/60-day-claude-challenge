# RiskLens — API Design

Two endpoints for v1.0, matching the PRD's single-applicant-scoring scope exactly. No implementation code here — contract only.

> **Updated Day 4:** The feature list below reflects the version validated against real LendingClub data (see `docs/feature_spec.md` for the full validation, including two substitutions and the reasoning for three additional exclusions found during real-data testing). This supersedes the proposed list from Day 2.

## Feature List (validated against real data — see docs/feature_spec.md)

| Field | Type | Notes |
|---|---|---|
| loan_amount | float | Requested loan amount, USD |
| term_60_months | bool | true = 60-month term, false = 36-month term |
| interest_rate | float | Annual interest rate, % |
| fico_score | int | Origination-time FICO score (replaces "grade" — not available in the validated data source; FICO is an equally legitimate, more granular origination-time signal) |
| annual_income | float | Applicant's stated annual income, USD |
| dti | float | Debt-to-income ratio, % |
| employment_length_years | int, 0-10 | 10 = "10+ years" |
| home_ownership | enum: MORTGAGE, OWN, RENT, OTHER, NONE | |
| purpose | enum: car, credit_card, debt_consolidation, educational, home_improvement, house, major_purchase, medical, moving, other, renewable_energy, small_business, vacation, wedding | |
| open_accounts | int | Number of currently open credit lines |
| total_credit_lines | int | Total credit lines ever opened |
| revolving_utilization | float | % of revolving credit currently used |
| delinquencies_2yrs | int | Count of delinquencies in the past 2 years (bureau data pulled at origination — legitimate, not leakage) |
| public_records | int | Count of derogatory public records |
| verification_status | enum: Verified, Source Verified, Not Verified | Income verification status |

**Dropped from the Day 2 proposal:** `earliest_credit_line_years` — not present in the validated real data source.
**Excluded on discovery (see docs/feature_spec.md for evidence):** `last_fico_range_high` (confirmed data leakage), `zip_code` (fair-lending exclusion), `installment` (collinear with loan_amount).

Risk tiers (from Day 1 Blueprint, to be confirmed against the real test-set score distribution on Day 5): **Low** < 10%, **Medium** 10-30%, **High** > 30%.

---

## `GET /health`

**Purpose:** Deployment/uptime monitoring — confirms the service is running and the model loaded successfully.

**Request:** None.

**Response (200):**
```json
{ "status": "ok", "model_loaded": true }
```

**Validation:** None (no input).

**Authentication:** None.

**Error cases:** None expected under normal operation. If the model failed to load at startup, this should return 503 with `{"status": "degraded", "model_loaded": false}` rather than crashing silently.

---

## `POST /predict`

**Purpose:** Score a single applicant's default risk and return an explanation.

**Request body:** JSON object with every field from the Feature List above, correctly typed.

```json
{
  "loan_amount": 5000,
  "term_60_months": false,
  "interest_rate": 10.65,
  "fico_score": 739,
  "annual_income": 24000,
  "dti": 27.65,
  "employment_length_years": 10,
  "home_ownership": "RENT",
  "purpose": "credit_card",
  "open_accounts": 3,
  "total_credit_lines": 9,
  "revolving_utilization": 83.7,
  "delinquencies_2yrs": 0,
  "public_records": 0,
  "verification_status": "Verified"
}
```

**Response (200):**
```json
{
  "probability": 0.22,
  "risk_tier": "Medium",
  "top_factors": [
    { "feature": "revolving_utilization", "direction": "increased_risk", "explanation": "High revolving utilization (84%) increased predicted risk." },
    { "feature": "dti", "direction": "increased_risk", "explanation": "A relatively high DTI (27.65%) increased predicted risk." },
    { "feature": "employment_length_years", "direction": "decreased_risk", "explanation": "10 years of employment history decreased predicted risk." }
  ]
}
```

**Validation (via Pydantic, enforced before the model ever runs):**
- All 15 fields required, no optional fields in v1.0
- `fico_score` bounded to a realistic range (roughly 300-850)
- `dti`, `revolving_utilization` bounded 0-100
- `annual_income`, `loan_amount` must be positive
- `employment_length_years` bounded 0-10
- `delinquencies_2yrs`, `public_records`, `open_accounts`, `total_credit_lines` must be non-negative integers
- Enum fields (`home_ownership`, `purpose`, `verification_status`) restricted to the exact allowed values listed above

**Authentication:** None — public endpoint by design, no PII collected or stored (consistent with PRD's data privacy requirement).

**Error cases:**
| Status | When | Response body |
|---|---|---|
| 422 | Any field missing, wrong type, or out of allowed range | Pydantic's automatic field-level error detail (which field, what's wrong) |
| 500 | Model/preprocessor fails to run on otherwise-valid input (unexpected internal error) | Generic `{"error": "Prediction failed. Please try again."}` — full detail logged server-side only, never exposed to the client |

No 401/403 cases — there is no authentication layer in v1.0.
