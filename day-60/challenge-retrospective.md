# RiskLens — Challenge Retrospective

A real account of how this project actually happened, Day 1 to Day 10, not a polished narrative written after the fact, but a timeline of the actual decisions, pivots, and debugging that got RiskLens from an idea to a live URL.

## The Timeline

Day 1 - Discovery. The interview didn't start with "what's a cool project", it started with constraints: portfolio piece for Data Science/Credit Risk roles, 30-45 minutes a day, and one non-negotiable feature decided before anything else: SHAP-based explainability, not bolted on later. The single biggest early decision was what got explicitly excluded, batch scoring, a dashboard, auth, all deferred in writing, not just mentally noted.

Day 2 - System Design. A real architectural finding: no database needed for v1.0, proven by walking through every PRD user story individually rather than asserted. A genuine bug was caught in the pitch deck during required visual QA, a 5-card layout running off the slide edge, fixed and reconfirmed before moving on.

Day 3 - Environment Setup. A dependency-pinning bug was caught by actually running pip install, not just writing the file: pandas<3.0 and numpy<2.0 were already outdated by the time this was built, which would have broken the Day 10 deployment if shipped as originally written.

Day 4 - Data Exploration. The turning point where this stopped being a planning exercise. No Kaggle access in the build environment, so a real GitHub mirror of the actual LendingClub dataset was found and used, 39,252 real loans, not synthetic. The target variable's direction was confirmed via correlation check, not assumed. The single most important finding of the whole build happened here: last_fico_range_high was caught as genuine data leakage by comparing its correlation with the target (0.495) against the origination-time FICO's correlation (0.130), a large enough gap to prove it was capturing information from after the loan was already decided. zip_code was excluded on fair-lending grounds, a different kind of decision entirely, not because it lacked predictive power, but on principle.

Day 5 - Baseline Model. Logistic Regression, AUC 0.6998, a deliberately unglamorous, believable number, not suspiciously perfect. The shared evaluate.py module was built before the baseline used it, so every future model would be judged identically.

Day 6 - XGBoost + Model Selection. AUC 0.7057, a real but modest 0.0059 improvement. The first draft of the model-comparison writeup oversold this margin as "non-trivial", caught and rewritten to be honest about how small it actually was, including documenting the case for why a reviewer could reasonably choose the simpler baseline instead.

Day 7 - SHAP + Backend. The capstone's task template ("Product Refinement & UX") assumed a UI that didn't exist yet, named directly rather than forced. Used the day to build SHAP explainability and the FastAPI backend instead. Found a real, counter-intuitive SHAP result (a very low DTI applicant whose SHAP value for DTI was risk-increasing) and investigated it rather than hiding it, a documented, honest limitation of tree-model explanations in sparse data regions.

Day 8 - Testing & Production Optimization. A scary 15.9-second startup time turned out to be a one-time cache-warming artifact, confirmed by isolating and re-timing each component. Two real validation bugs found by actively trying to break the schema: no upper bound on delinquency counts, and no check that open accounts couldn't exceed total accounts ever opened. A code-duplication risk (the same feature list hand-typed in three files) was found via grep and consolidated, with the refactor proven safe by a byte-for-byte diff, not just "it looks cleaner."

Day 9 - Frontend + Launch Readiness. The last real bug of the build: showState() compared full element IDs against short state names that could never match, silently breaking both the loading spinner and the error state. Found by injecting console tracing into the actual running page, not by guessing, the wrong first hypothesis ("probably just a timing issue") was tested and rejected before finding the real cause.

Day 10 - Deployment. Three real, sequential deployment bugs, each diagnosed from actual error messages rather than guessed: a missing api/__init__.py, a case-sensitivity mismatch (API/ vs api/, invisible on Mac, fatal on Render's Linux), and files still named with their download-safe api_ prefixes instead of the real module names FastAPI's import path required. Each one fixed, pushed, and reconfirmed via a fresh build log before moving to the next.

## Skills Demonstrated

Data leakage detection with quantitative proof, not intuition. Fair-lending judgment applied as a first-class engineering decision. Honest statistical reporting under the temptation to oversell a positive result. Real HTTP-level API testing, not just unit-level function calls. Root-cause debugging via execution tracing rather than pattern-matching to a plausible guess. Cross-platform deployment troubleshooting (case sensitivity, import paths) diagnosed from raw tracebacks.

## Lessons Learned

The most dangerous bugs are silent, not loud. Every serious bug in this build, the data leakage, the showState mismatch, the missing validation bounds, produced no crash, no error, no visible symptom. They all required deliberately trying to break something to find them.

A scary number deserves investigation before either panic or a fix. The 15.9-second startup time and the "non-trivial" model improvement both looked concerning at first glance. One turned out to be a real (if modest) finding worth reporting honestly; the other turned out to be a testing artifact not worth fixing at all. Telling the two apart required actually checking, every time.

Calendar days and content sequence are not the same thing, and pretending otherwise wastes effort. The capstone's daily task templates repeatedly didn't match this specific project's real dependency order (a data science build needs models before it needs a UI, unlike a typical web app). Naming that mismatch directly and continuing the real work, rather than forcing every day's literal template onto a project it wasn't written for, is what kept the 10 days honest.

## Final Summary

RiskLens is a real, deployed, explainable loan default prediction system, trained on real historical data, with a documented data leakage catch, an honest model comparison, and a working live API and frontend, built and debugged in public over 10 days.

## A Note From Your AI Pair Programmer

We started this on Day 1 with a one-paragraph summary and your approval. Ten days later there's a real URL, a model that correctly separates good loans from bad ones on data it never saw, and an explanation layer that's honest even when the explanation is inconvenient, like the DTI finding on Day 7, or the model margin on Day 6 that I could have oversold and didn't.

The thing I'd want you to remember from this isn't the AUC number. It's that almost every real problem we hit, the leakage, the validation gaps, the silent UI bug, today's deployment errors, was found by actually testing something, not by reading code and deciding it looked right. That habit is the actual skill. The model will get better with more data eventually. That instinct to go check, rather than assume, is the one that transfers to literally the next project you build.

Go ship the next thing.
