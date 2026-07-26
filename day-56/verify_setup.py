"""
RiskLens — Environment Verification Script

Run this after creating the conda environment to confirm every dependency
installed correctly and can actually be imported. This is a setup smoke
test, not application code — it does nothing with data or models.

Usage:
    conda activate risklens
    python verify_setup.py
"""
import sys

REQUIRED_PACKAGES = [
    "pandas",
    "numpy",
    "sklearn",
    "xgboost",
    "shap",
    "fastapi",
    "uvicorn",
    "pydantic",
    "joblib",
]

def main():
    print(f"Python version: {sys.version}\n")
    print("Checking required packages...\n")

    failures = []
    for pkg_name in REQUIRED_PACKAGES:
        try:
            module = __import__(pkg_name)
            version = getattr(module, "__version__", "unknown")
            print(f"  [OK]   {pkg_name:<12} {version}")
        except ImportError as e:
            print(f"  [FAIL] {pkg_name:<12} could not be imported: {e}")
            failures.append(pkg_name)

    print()
    if failures:
        print(f"Setup INCOMPLETE — {len(failures)} package(s) failed to import: {', '.join(failures)}")
        print("Fix: conda env update -f environment.yml --prune, then rerun this script.")
        sys.exit(1)
    else:
        print("Setup COMPLETE — all required packages import successfully.")
        print("Environment is ready for Day 4 onward.")
        sys.exit(0)

if __name__ == "__main__":
    main()
