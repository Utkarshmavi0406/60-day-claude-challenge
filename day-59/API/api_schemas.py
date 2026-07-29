"""
RiskLens API — Pydantic Schemas

Defines the exact request/response contract from docs/API.md. Validation
happens automatically via these type annotations before the model ever
runs — an invalid request never reaches the prediction logic.
"""
from enum import Enum
from pydantic import BaseModel, Field, model_validator


class HomeOwnership(str, Enum):
    MORTGAGE = "MORTGAGE"
    OWN = "OWN"
    RENT = "RENT"
    OTHER = "OTHER"
    NONE = "NONE"


class Purpose(str, Enum):
    car = "car"
    credit_card = "credit_card"
    debt_consolidation = "debt_consolidation"
    educational = "educational"
    home_improvement = "home_improvement"
    house = "house"
    major_purchase = "major_purchase"
    medical = "medical"
    moving = "moving"
    other = "other"
    renewable_energy = "renewable_energy"
    small_business = "small_business"
    vacation = "vacation"
    wedding = "wedding"


class VerificationStatus(str, Enum):
    verified = "Verified"
    source_verified = "Source Verified"
    not_verified = "Not Verified"


class ApplicantInput(BaseModel):
    loan_amount: float = Field(..., gt=0, description="Requested loan amount, USD")
    term_60_months: bool = Field(..., description="true = 60-month term, false = 36-month term")
    interest_rate: float = Field(..., ge=0, le=40, description="Annual interest rate, %")
    fico_score: int = Field(..., ge=300, le=850, description="Origination-time FICO score")
    annual_income: float = Field(..., gt=0, description="Applicant's stated annual income, USD")
    dti: float = Field(..., ge=0, le=100, description="Debt-to-income ratio, %")
    employment_length_years: int = Field(..., ge=0, le=10, description="10 = '10+ years'")
    home_ownership: HomeOwnership
    purpose: Purpose
    open_accounts: int = Field(..., ge=0, le=60, description="Number of currently open credit lines")
    total_credit_lines: int = Field(..., ge=0, le=120, description="Total credit lines ever opened")
    revolving_utilization: float = Field(..., ge=0, le=100, description="% of revolving credit used")
    delinquencies_2yrs: int = Field(..., ge=0, le=20, description="Delinquencies in the past 2 years")
    public_records: int = Field(..., ge=0, le=10, description="Derogatory public records")
    verification_status: VerificationStatus

    @model_validator(mode="after")
    def check_open_accounts_within_total(self):
        # Logical constraint: you can't have more currently-open accounts
        # than total accounts ever opened. Found during Day 8 QA review —
        # violated in only 1 of 39,252 real training rows (a rare data
        # quirk, not a real pattern), so this catches obvious bad input
        # (e.g. a typo) without meaningfully conflicting with real data.
        if self.open_accounts > self.total_credit_lines:
            raise ValueError(
                "open_accounts cannot exceed total_credit_lines "
                f"(got open_accounts={self.open_accounts}, total_credit_lines={self.total_credit_lines})"
            )
        return self

    class Config:
        json_schema_extra = {
            "example": {
                "loan_amount": 5000,
                "term_60_months": False,
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
                "verification_status": "Verified",
            }
        }


class RiskFactor(BaseModel):
    feature: str
    direction: str
    explanation: str


class PredictionResponse(BaseModel):
    probability: float
    risk_tier: str
    top_factors: list[RiskFactor]


class HealthResponse(BaseModel):
    status: str
    model_loaded: bool
