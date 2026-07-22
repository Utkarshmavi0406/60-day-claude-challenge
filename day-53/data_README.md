# Data

## Source

**Lending Club Loan Data** (Accepted Loans), 2007–2018 vintage.
Available on Kaggle: search "Lending Club Loan Data" or use the dataset commonly distributed as `accepted_2007_to_2018Q4.csv`.

## How to Get It (Manual Download — No Kaggle API Needed)

1. Go to Kaggle and search for "Lending Club Loan Data."
2. Download the accepted-loans file (commonly named `accepted_2007_to_2018Q4.csv` or similar — filenames vary slightly by upload).
3. Place it at: `data/raw/accepted_loans.csv`

This file is **not committed to the repository** (see `.gitignore`) — it's large (1–2GB) and freely re-downloadable from the source, so there's no reason to store it in git history.

## What Happens To It

`src/clean_data.py` (Day 4) reads this raw file and produces `data/processed/clean_loans.csv` — the actual model-ready dataset. That processed file is also gitignored; it's fully regenerable by rerunning the cleaning script against the raw download.

## Folders

- `data/raw/` — the untouched downloaded CSV goes here (gitignored)
- `data/processed/` — cleaning script output goes here (gitignored)
- `data/sample_applicants.json` — 3–4 preset applicant profiles used by both the frontend and manual testing (committed — this one's small and is a real part of the product, not raw data)

## Target Variable (confirmed Day 2, validated against real data Day 4)

`default = 1` if `loan_status` is "Charged Off" or "Default"; `default = 0` if "Fully Paid." All other statuses (Current, Late, In Grace Period, etc.) are excluded from the modeling set — they're not resolved outcomes yet.

See `docs/API.md` for the full proposed feature list, and `docs/feature_spec.md` (Day 4) for the version validated against the actual dataset.
