# Day 52 of 60 - Capstone Day 2: System Design

## What Was Built

Full technical system design for RiskLens, built directly from Day 1's approved PRD and Implementation Blueprint - no redesign, only making the approved plan concrete.

## Decisions Finalized Today

1. **Tech stack confirmed:** Python/pandas/scikit-learn/XGBoost/SHAP for modeling, FastAPI for the backend, a single-file HTML/CSS/JS frontend served as static files from the same app, Render.com for hosting.
2. **No database in v1.0** - confirmed and validated against every single PRD user story in SCHEMA.md. Every v1.0 story is satisfiable with zero persistent storage; a proposed future schema is documented for when Future Scope items (batch scoring, portfolio dashboard) eventually get built.
3. **No authentication in v1.0** - confirmed, consistent with PRD Section 5.2.
4. **API surface locked to 2 endpoints:** POST /predict and GET /health. A concrete 16-field feature list was proposed today (based on standard LendingClub origination-time fields) to be validated against real data on Day 3.
5. **UI is a single screen with four states** (initial, loading, result, error), not multiple pages - a deliberate outcome of the PRD's single-applicant-scoring scope.
6. **Full project folder structure defined**, with the src/ vs api/ split (offline training pipeline vs. always-running service) as the most important organizing decision.

## A Real Schedule Adjustment, Made and Documented

Yesterday's Blueprint had "Day 2 = Data Exploration & Architecture." Today's actual capstone Day 2 turned out to be a full System Design session instead - broader and more valuable to do properly than the original plan anticipated. Rather than push the whole 10-day schedule back a day, the lightweight data-exploration tasks (target variable definition, feature shortlist) were folded into Day 3 alongside the environment/pipeline setup that was already planned there. Day 10 deployment date is unaffected. This is documented as an explicit changelog note at the top of the updated Implementation Blueprint, not silently changed.

## Deliverables

- `ARCHITECTURE.md` - tech stack table, Mermaid component diagram, two data-flow diagrams (offline training vs. online serving), request sequence diagram, external services audit
- `SCHEMA.md` - the "no database" decision, validated line-by-line against PRD user stories, plus a Future Scope schema sketch
- `API.md` - full contract for both endpoints: request/response shapes, the proposed 16-field feature list, validation rules, and every error case
- `UI-WIREFRAMES.md` - user flow diagram, the four-state single-screen model, a low-fidelity ASCII wireframe, and an explicit "no navigation" decision
- `PROJECT-STRUCTURE.md` - the full folder tree with a rationale for each major directory
- `RiskLens_Implementation_Blueprint.md` (updated) - Days 2-10, with the schedule adjustment folded in and documented

## Key Learnings

1. **A schedule change is only honest if it's dated and explained, not just quietly absorbed.** The Blueprint update includes a visible changelog note explaining exactly what moved and why, rather than silently rewriting Day 3 as if it was always the plan.
2. **"No database" is a stronger claim when it's proven, not just stated.** Walking through every PRD user story individually and confirming none of them need persistence turned a one-line architecture choice into something a reviewer can actually verify, not just trust.
3. **Proposing a concrete API contract before the data is even downloaded is a deliberate sequencing choice.** It commits to a specific, reviewable feature list today based on domain knowledge, with Day 3 explicitly tasked to validate it against real data rather than silently discovering the contract was wrong later in the build.
4. **A single-screen app with zero navigation is a real design decision, not a missing feature.** Documenting *why* there's no second screen (the PRD's scope doesn't need one) prevents that from reading as an oversight to anyone reviewing the project later.

## Deliverables checklist

- [x] Tech stack confirmed with the user before proceeding
- [x] Architecture diagrams generated (component, data flow x2, sequence)
- [x] Database decision made and validated against PRD user stories
- [x] API contract fully specified for both endpoints
- [x] UI flow and wireframe documented
- [x] Full project structure defined
- [x] Implementation Blueprint updated to reflect today's decisions
- [x] All docs committed to the risklens project repository
- [x] Copies uploaded to today's daily challenge folder
