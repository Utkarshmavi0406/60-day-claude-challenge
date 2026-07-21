# RiskLens — API Design

Two endpoints for v1.0, matching the PRD's single-applicant-scoring scope exactly. No implementation code here — contract only, per today's rules.

## Feature List (proposed today, validated against real data on Day 3)

Based on standard LendingClub origination-time fields (no post-origination/leakage fields, consistent with PRD Section 9):

| Field | Type | Notes |
|---|---|---|
| loan_amount | float | Requested loan amount, USD |
| term_months | enum: 36, 60 | Loan term |
| interest_rate | float | Annual interest rate, % |
| grade | enum: A-G | LendingClub's own origination-time risk grade |
| annual_income | float | Applicant's stated annual income, USD |
| dti | float | Debt-to-income ratio, % |
| employment_length_years | int, 0-10 | 10 = "10+ years" |
| home_ownership | enum: RENT, OWN, MORTGAGE, OTHER | |
| purpose | enum: debt_consolidation, credit_card, home_improvement, major_purchase, small_business, other | |
| earliest_credit_line_years | float | Years since first credit line opened |
| open_accounts | int | Number of currently open credit lines |
| total_credit_lines | int | Total credit lines ever opened |
| revolving_utilization | float | % of revolving credit currently used |
| delinquencies_2yrs | int | Count of delinquencies in the past 2 years (bureau data pulled at origination — legitimate, not leakage) |
| public_records | int | Count of derogatory public records |
| verification_status | enum: Verified, Source Verified, Not Verified | Income verification status |

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
  "loan_amount": 15000,
  "term_months": 36,
  "interest_rate": 12.5,
  "grade": "B",
  "annual_income": 65000,
  "dti": 18.4,
  "employment_length_years": 6,
  "home_ownership": "MORTGAGE",
  "purpose": "debt_consolidation",
  "earliest_credit_line_years": 11,
  "open_accounts": 8,
  "total_credit_lines": 22,
  "revolving_utilization": 42.1,
  "delinquencies_2yrs": 0,
  "public_records": 0,
  "verification_status": "Source Verified"
}
```

**Response (200):**
```json
{
  "probability": 0.14,
  "risk_tier": "Medium",
  "top_factors": [
    { "feature": "revolving_utilization", "direction": "increased_risk", "explanation": "High revolving utilization (42%) increased predicted risk." },
    { "feature": "dti", "direction": "decreased_risk", "explanation": "A relatively low DTI (18.4%) decreased predicted risk." },
    { "feature": "employment_length_years", "direction": "decreased_risk", "explanation": "6 years of employment history decreased predicted risk." }
  ]
}
```

**Validation (via Pydantic, enforced before the model ever runs):**
- All 16 fields required, no optional fields in v1.0
- `term_months` must be exactly 36 or 60
- `grade` must be one of A-G
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
