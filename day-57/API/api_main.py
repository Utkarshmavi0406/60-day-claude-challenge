"""
RiskLens API — FastAPI Application

Two endpoints, per docs/API.md:
  GET  /health   — deployment monitoring
  POST /predict  — score one applicant, with SHAP explanation

Run locally:
    uvicorn api.main:app --reload --port 8000
Then visit http://127.0.0.1:8000/docs for the interactive test UI.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from schemas import ApplicantInput, PredictionResponse, HealthResponse, RiskFactor
from model_loader import get_explainer, encode_applicant, risk_tier

app = FastAPI(
    title="RiskLens API",
    description="Explainable loan default risk prediction - trained on real LendingClub data.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

_model_load_error = None


@app.on_event("startup")
def load_model_at_startup():
    global _model_load_error
    try:
        get_explainer()
        print("Model and SHAP explainer loaded successfully at startup.")
    except Exception as e:
        _model_load_error = str(e)
        print(f"MODEL LOAD FAILED AT STARTUP: {e}")


@app.get("/health", response_model=HealthResponse)
def health():
    if _model_load_error:
        raise HTTPException(status_code=503, detail=f"Model failed to load: {_model_load_error}")
    return HealthResponse(status="ok", model_loaded=True)


@app.post("/predict", response_model=PredictionResponse)
def predict(applicant: ApplicantInput):
    if _model_load_error:
        raise HTTPException(status_code=503, detail="Model is not available. Try again shortly.")
    try:
        explainer = get_explainer()
        encoded = encode_applicant(applicant)
        result = explainer.explain(encoded)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception:
        print(f"Prediction error for input {applicant.model_dump()}")
        raise HTTPException(status_code=500, detail="Prediction failed. Please try again.")

    return PredictionResponse(
        probability=result["probability"],
        risk_tier=risk_tier(result["probability"]),
        top_factors=[RiskFactor(**f) for f in result["top_factors"]],
    )

# Frontend (Day 9 content step) will be mounted here once it exists:
# app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
