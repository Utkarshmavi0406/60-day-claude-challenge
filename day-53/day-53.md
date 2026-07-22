# Day 53 of 60 — Capstone Day 3: Environment & Repository Setup

## What Was Built

The actual, working repository scaffold for RiskLens — environment configuration, dependency management, folder structure, and a verification script — built exactly to match yesterday's `docs/PROJECT-STRUCTURE.md`. No feature code yet; today is purely making the repo buildable and provable-correct before any implementation starts tomorrow.

## Decisions Made Today

**Environment manager: Conda**, confirmed directly (the terminal screenshots throughout this capstone consistently show an active `(base)` conda prompt, so a dedicated `risklens` conda environment matches the existing setup rather than introducing a second tool).

**Two dependency files, for two different purposes** — this is worth calling out explicitly:
- `environment.yml` — for local development via conda, core data-science packages from conda-forge, the rest via pip within the same environment
- `requirements.txt` — for Render deployment, which uses pip, not conda. Render has no conda support, so `requirements.txt` is what actually gets installed in production, regardless of what's used locally.

## A Real Bug Caught by Actually Testing

I didn't just write `requirements.txt` and assume it was correct — I installed it and ran the verification script against it. That caught a real problem: my first draft pinned upper bounds like `pandas<3.0` and `numpy<2.0`, but the actual current package ecosystem already has `pandas 3.0` and `numpy 2.4` available. Shipping that file to Render as-is would have caused a real, confusing dependency resolution failure during Day 10's deployment — exactly the kind of bug that's invisible until you actually try to install from the file. Fixed by loosening to minimum-version-only pins, then reran the install and the verification script to confirm the fix actually works, not just that it looks more reasonable.

## Deliverables

- `environment.yml` — the conda environment specification
- `requirements.txt` — pip dependencies for Render deployment (corrected after real testing)
- `.gitignore` — excludes raw/processed data and environments, while deliberately **not** ignoring `models/*.pkl` (those are committed artifacts per yesterday's architecture decision)
- `verify_setup.py` — a real, runnable smoke test that imports every required package and reports pass/fail per package, not just "it didn't crash"
- `README.md` — the actual project README, including a live status table tracking progress against the 10-day plan
- `data/README.md` — data source, manual download instructions, and what happens to the raw file once downloaded
- Full folder scaffold (`data/raw/`, `data/processed/`, `src/`, `models/`, `api/`, `frontend/`, `reports/`, `docs/`) with `.gitkeep` placeholders where folders need to survive git despite being empty today
- `risklens-day3-scaffold.zip` — the entire scaffold packaged for one-step setup

## Key Learnings

1. **A dependency file is a claim, and claims need testing, not just writing.** The pandas/numpy version bug wouldn't have shown up by reading the file — it only surfaced by actually running `pip install -r requirements.txt` and checking what happened. Writing "reasonable-looking" version pins isn't the same as writing correct ones.
2. **Local dev environment and deployment environment are allowed to differ, as long as the difference is explicit.** Conda locally, pip on Render, is a completely normal split — the risk isn't the split itself, it's letting the two dependency files silently drift out of sync. Today's `environment.yml` and `requirements.txt` list the same packages at the same minimum versions specifically to avoid that.
3. **`.gitkeep` placeholders are a small detail that matters for a scaffold day specifically.** Git doesn't track empty directories, so `data/raw/`, `data/processed/`, `models/`, and `reports/` would silently vanish from a fresh clone without them — invisible today, confusing on Day 4 when someone (including future me) wonders why a folder from the architecture doc doesn't exist.
4. **A verification script's value is in what it reports on failure, not just success.** `verify_setup.py` names exactly which package failed and what the fix is, rather than a generic traceback — the whole point of a Day 3 smoke test is catching environment problems in a way that's immediately actionable, not just detectable.

## Deliverables Checklist

- [x] Environment manager decided (Conda) and confirmed with the user
- [x] `environment.yml` created and tested
- [x] `requirements.txt` created, tested, and corrected after a real version-pinning bug was found
- [x] `.gitignore` configured correctly against the approved project structure
- [x] Full folder scaffold created, matching `docs/PROJECT-STRUCTURE.md` exactly
- [x] `verify_setup.py` written and confirmed working
- [x] Project `README.md` written with a live progress table
- [x] `data/README.md` written with real download instructions
- [x] Everything committed to the `risklens` project repository
- [x] Copies uploaded to today's daily challenge folder
