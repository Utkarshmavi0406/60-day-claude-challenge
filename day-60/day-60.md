# Day 60 of 60 - Capstone Day 10: Final Review, Portfolio & Graduation

## The Capstone Is Live

RiskLens v1.0.0 is deployed and verified working at https://risklens-ki1d.onrender.com - a real prediction was confirmed live (26% probability, Medium Risk, correct SHAP factors rendering) before any graduation work began.

## Three Real Deployment Bugs, Each Diagnosed From the Actual Error

Getting to "live" wasn't automatic. Three sequential failures, each fixed by reading the real traceback rather than guessing:

1. ModuleNotFoundError: No module named 'api' - traced to a missing api/__init__.py.
2. The identical error persisted after that fix - traced to the actual root cause: the folder was named API (capital) on GitHub, but the start command referenced lowercase api. macOS's case-insensitive filesystem hid this locally; Render's Linux environment did not.
3. Could not import module "api.main" - traced to files still carrying their download-safe api_ prefixes (api_main.py instead of main.py) inside the repo, never renamed before committing.

Each was fixed, pushed, and reconfirmed via a fresh build log before moving to the next - the same discipline used throughout all 10 days, applied one more time under real launch pressure.

## Five-Lens Final Review

Reviewed as Senior Engineer, Product Manager, UI/UX Designer, Recruiter, and Open Source Maintainer. No blocking gaps found. One honest limitation named rather than hidden: no automated pytest suite exists yet, testing throughout the build was rigorous but script-based, not codified into CI. Documented as the first item in 30-day-growth-plan.md rather than glossed over.

## Deliverables

- future-scope.md - 3/6/12 month roadmap grounded in what v1.0 actually is
- challenge-retrospective.md - full Day 1-10 timeline, real decisions, real bugs, lessons learned, and a note from the AI pair programmer
- 30-day-growth-plan.md - 30 daily milestones, week-themed, building only on the real existing stack
- daily-build-prompt.md - the reusable prompt for that 30-day plan
- portfolio-assets.md - project descriptions, resume bullets, interview talking points, demo script, GitHub metadata
- graduation-infographic.html - the 60-day skill journey culminating in RiskLens
- certificate.html - printable Certificate of Completion, AB Talks branding and required links
- v1.0.0 tagged and released in the risklens repo

## Key Learnings

1. A working local build and a working deployed build are different claims, proven differently. Every prior day's testing was real and rigorous, and none of it caught the case-sensitivity bug, because that specific failure mode only exists on Linux, not macOS. The lesson isn't "test more", it's that some classes of bug are invisible until you test in the actual target environment, not a stand-in for it.

2. A second identical-looking error after a fix means the first diagnosis was wrong, not that the fix failed to apply. The temptation after the __init__.py fix didn't work was to assume it just needed more time or a harder push. Reading the error as new information, not as confirmation of the first guess, was what found the real case-sensitivity cause.

3. A retrospective is only honest if it names the wrong first guesses, not just the right final answers. The showState timing hypothesis on Day 9, the "non-trivial" model claim on Day 6, and today's __init__.py theory were all reasonable-sounding wrong turns before the real answer, leaving them in the record is what makes the record trustworthy.

## Final Status

- [x] Live application verified working end-to-end
- [x] Five-lens review complete, no blockers found
- [x] All four required files created
- [x] Portfolio assets generated from real project facts
- [x] Graduation infographic and certificate built and visually verified
- [x] v1.0.0 tagged in the risklens repository
- [x] Everything committed to both repositories
