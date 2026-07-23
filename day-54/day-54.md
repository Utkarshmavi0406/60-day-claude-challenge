# Day 54 of 60 - Capstone Day 4: Data Exploration & Cleaning Pipeline

## What Was Built

The first real implementation work on RiskLens: real LendingClub loan data downloaded, the target variable direction confirmed (not assumed), the Day 2 feature proposal validated against actual data, and a working clean_data.py pipeline that ran successfully end-to-end.

## This Is Real Data, Not Synthetic

I don't have Kaggle access in my environment, but rather than generate a synthetic stand-in, I found and downloaded a real public GitHub mirror of the LendingClub "accepted loans" dataset (2007 vintage, 39,252 real historical loans). Every number in today's validation - the class balance, the leakage discovery, the correlation checks - comes from genuine loan outcome data, not a fabricated approximation.

## Real Findings From Real Data

**Target variable direction was confirmed, not assumed.** The source data's loan_status column was already binary (1/0) with no documentation of which value meant what. Rather than guess, I checked whether loan_status=0 correlated with worse credit signals - it did (higher interest rate, lower FICO, higher DTI) - confirming 0 = Charged Off before building anything on top of that assumption.

**14 of 16 proposed features validated directly against real data.** 1 was substituted (grade -> fico_score, since LendingClub's letter grade wasn't present in this data source - FICO is an equally legitimate, more granular replacement). 1 was dropped (earliest_credit_line_years, not available).

**Three real risks were caught that weren't in the original plan:**

- last_fico_range_high - confirmed data leakage by comparing its correlation with the target (0.495) against the origination-time FICO's correlation (0.130). That gap is large enough to confirm it's capturing credit deterioration that already happened by the time the loan was charged off, not information available when the loan was made.
- zip_code - excluded on fair-lending grounds (a geographic proxy for protected-class characteristics), independent of whatever predictive power it might have had.
- installment - excluded for being collinear with loan amount (r=0.93), a redundant signal.

**Final result:** a clean, 39,252-row, 35-column, zero-null dataset with a 14.4% default rate - landing exactly inside the "10-20%" range the Day 1 PRD predicted for a healthy, non-degenerate classification target.

## Deliverables

- src/clean_data.py - the real, tested cleaning pipeline (leakage/fairness exclusions, target definition, null handling, all with inline documentation of why)
- data/raw/accepted_loans.csv - the real downloaded data (not committed to git per .gitignore, but the source is documented)
- data/processed/clean_loans.csv - the actual clean output, verified independently after generation
- docs/feature_spec.md - the full validation writeup: what matched, what changed, and the evidence for every exclusion
- docs/API.md (updated) - the endpoint contract updated to match the validated feature set, not the Day 2 proposal
- RiskLens_Implementation_Blueprint.md (updated) - Day 3 marked complete with real results; a second changelog entry acknowledging that calendar-day labels and content sequence have decoupled, and that the content sequence remains authoritative

## Key Learnings

1. "Validate against real data" has to mean actually running the check, not eyeballing a schema. The leakage finding on last_fico_range_high only surfaced because I computed and compared two correlation numbers - reading the column name alone might have raised suspicion, but the 0.495-vs-0.130 gap is what actually proves it, not just names it as plausible.

2. A feature substitution is a legitimate outcome of validation, not a failure of planning. Yesterday's proposal of "grade" was reasonable domain knowledge; today's real data simply didn't have it. Documenting the substitution with a rationale is what keeps this honest instead of either silently changing the API contract or refusing to adapt to what the real data actually offers.

3. Fair-lending exclusions and data-leakage exclusions are different kinds of decisions and deserve different justifications. zip_code wasn't excluded because it lacks predictive power, it very well might have some. It was excluded on principle. Conflating "this doesn't help the model" with "this shouldn't be used" would blur an important distinction a real credit risk reviewer would care about.

4. Schedule drift compounds if each day tries to re-fix it completely. After the second consecutive day where the actual capstone-template topic didn't match my own Blueprint's day-by-day predictions, the more sustainable fix wasn't another full renumbering, it was explicitly decoupling "calendar day label" from "content sequence," and saying so directly, rather than pretending a precision in day-numbering that two days of evidence had already disproven.

5. Finding real data via a GitHub mirror, when the primary source (Kaggle) isn't reachable, is worth the extra search effort. A synthetic fixture would have been defensible for testing code logic, but it couldn't have produced a real leakage finding or a real, meaningful class balance - those only exist because the data itself is real.

## Deliverables Checklist

- [x] Real data source located and downloaded (GitHub mirror of LendingClub data)
- [x] Target variable direction confirmed via correlation check, not assumed
- [x] Day 2's proposed feature list validated against real data, changes documented
- [x] Data leakage actively checked for and found (last_fico_range_high), not just assumed absent
- [x] Fair-lending exclusion applied and justified (zip_code)
- [x] clean_data.py written, run, and its output independently verified
- [x] docs/feature_spec.md and updated docs/API.md committed
- [x] Implementation Blueprint updated to reflect real completion status
- [x] Everything committed to the risklens project repository
- [x] Copies uploaded to today's daily challenge folder
