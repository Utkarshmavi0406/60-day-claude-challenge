# RiskLens — Feature Specification (Validated Against Real Data)

**Capstone Day 4.** This document supersedes the proposed feature list in yesterday's docs/API.md with what was actually validated against real LendingClub data downloaded and processed today. Changes from the proposal are documented explicitly below, not silently applied.

## Data Source Used

Real LendingClub 2007-era accepted loan data (39,252 loans), obtained from a public GitHub mirror of the original Kaggle "Lending Club Loan Data" dataset (d-osei/Lending-Club-Loan-Data, loans_2007.csv). This is genuine historical loan performance data, not synthetic.

Note for local reproduction: data/README.md documents downloading the full multi-year dataset directly from Kaggle. The 2007-vintage subset used for today's validation is smaller and faster to iterate on locally; either source works with this same cleaning script, since both share LendingClub's standard column structure.

## Target Variable — Confirmed

The source data's loan_status column was already binary-encoded (1/0) rather than a text status. Direction was not assumed — it was confirmed by checking whether loan_status=0 correlates with worse credit signals:

| Metric | loan_status=0 | loan_status=1 |
|---|---|---|
| Mean interest rate | 13.84% | 11.67% |
| Mean origination FICO | 707.6 | 720.9 |
| Mean DTI | 14.01% | 13.17% |

loan_status=0 clearly corresponds to worse outcomes (higher rate, lower FICO, higher DTI) — confirming loan_status=0 = Charged Off, loan_status=1 = Fully Paid. Our target is defined as default = 1 - loan_status, so default=1 means the loan went bad, matching the convention in the PRD and docs/API.md.

Resulting class balance: 14.4% default rate — squarely inside the "10-20%, clear minority" range the Day 1 PRD anticipated.

## Feature List — Validated, With Changes Documented

| Yesterday's Proposal | Today's Validated Result | Status |
|---|---|---|
| loan_amount | loan_amnt | Available, direct match |
| term_months | term_ 60 months (binary) | Available, already one-hot in source |
| interest_rate | int_rate | Available, direct match |
| grade | fico_range_high | Substituted — LendingClub's letter grade wasn't present in this data source. Origination-time FICO score is available instead, and is arguably a more granular, equally legitimate origination-time risk signal. |
| annual_income | annual_inc | Available, direct match |
| dti | dti | Available, direct match |
| employment_length_years | emp_length | Available, already numeric 0-10 (no parsing needed) |
| home_ownership | home_ownership_* (5 categories) | Available, already one-hot in source |
| purpose | purpose_* (14 categories) | Available, already one-hot in source |
| earliest_credit_line_years | (none) | Dropped — not present in this data source. Not replaced; the remaining 14 features are sufficient for a v1.0 baseline, and this can be revisited if a richer data source is used later. |
| open_accounts | open_acc | Available, direct match |
| total_credit_lines | total_acc | Available, direct match |
| revolving_utilization | revol_util | Available — 50 nulls found and median-imputed (filled with 49.10) |
| delinquencies_2yrs | delinq_2yrs | Available, direct match |
| public_records | pub_rec | Available, direct match |
| verification_status | verification_status_* (3 categories) | Available, already one-hot in source |

14 of 16 proposed features validated directly, 1 substituted, 1 dropped — a normal, expected outcome of validating a proposal against real data, not a design failure.

## New Findings — Columns Excluded That Weren't in Yesterday's Plan

The real data included three columns not anticipated in yesterday's proposal, each excluded for a specific, checked reason:

| Column | Reason Excluded | Evidence |
|---|---|---|
| last_fico_range_high | Data leakage. This is a FICO score updated over the life of the loan, not at origination. | Correlates 0.495 with the target vs. only 0.130 for fico_range_high (origination) — a large enough gap to confirm it's capturing credit deterioration that already happened by the time the loan was charged off, not information available when the loan was made. |
| zip_code | Fair-lending exclusion. Geographic location is a well-known proxy for protected-class characteristics (redlining risk), independent of any correlation with the target. | Excluded on principle, not because it lacked predictive power — consistent with the fair-lending guardrails used elsewhere in this challenge (see Day 40's Underwriting Copilot). |
| installment | Redundant/collinear. Nearly a linear combination of loan amount, rate, and term. | Correlates 0.93 with loan_amnt — including it would add multicollinearity without new signal. |

## Final Feature Count

11 numeric features + 24 one-hot categorical columns (home ownership, purpose, verification status) + 1 term binary flag = 35 total input columns feeding the model, plus the default target column.

## Data Quality — Verified

- Final processed dataset: 39,252 rows x 35 feature columns + target
- Zero nulls in the final output (one column, revol_util, needed median imputation for 50 rows — everything else was already complete)
- Target confirmed strictly binary (0/1)

## Handoff to Day 5

data/processed/clean_loans.csv is the model-ready dataset. Day 5 (Baseline Model) reads directly from this file — no further cleaning needed.
