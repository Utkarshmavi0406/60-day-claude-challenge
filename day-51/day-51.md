# Day 51 of 60 - Capstone Kickoff: Product Discovery & Sprint Planning

## What Was Built

This is Day 1 of a 10-day capstone that runs alongside the remaining daily challenges. Today's deliverable isn't an app - it's the discovery, scoping, and planning that will guide the next 9 build days without re-planning from scratch each morning.

The project: RiskLens - an explainable loan default predictor. A user submits an applicant's financial profile (income, DTI, credit history, loan purpose) and gets back a default probability, a risk tier, and a SHAP-based, plain-English explanation of exactly which factors drove that score - trained on real LendingClub consumer loan data and deployed to a live public URL by Day 10.

## How the Idea Was Chosen

The interview didn't start from "what's a cool project" - it started from constraints:

1. Purpose: A portfolio piece for recruiters (not a personal tool, not a pure learning exercise)
2. Target audience: Data Science / Credit Risk Analyst roles specifically - my actual target
3. Technical comfort: Comfortable deploying backends/APIs/databases - this opened up a real full-stack scope rather than forcing a data-only project
4. Domain direction: A deployed loan default risk model, not a monitoring dashboard or an extension of an earlier challenge day
5. Dataset: LendingClub-style data - rich, realistic, and directly recognizable to credit risk interviewers
6. The one non-negotiable feature: SHAP-based explainability as a core v1.0 feature, not an afterthought - this is what separates the project from a generic "I trained a classifier" portfolio piece
7. Daily time budget: 30-45 minutes/day, same pace as the rest of the 60-day challenge - this is what forced single-applicant scoring only, no batch upload, no dashboard, no auth

## The Key Scoping Decision

The single biggest thing keeping this realistic: explicitly excluding batch CSV scoring and a portfolio-level dashboard from v1.0, even though both were tempting "while I'm in there" additions. Both are now documented in the PRD's Future Scope section with a one-line rationale each, rather than either being silently dropped or silently added mid-build. The PRD's Section 5.2 ("Explicitly Out of Scope") exists specifically to be the thing to point back to on Day 6 or Day 8 when a "just one more feature" idea shows up.

## Deliverables Generated

1. Product Requirements Document (RiskLens_PRD.docx) - 4 pages covering overview, problem statement, target users, goals, in-scope/out-of-scope v1.0 features, functional and non-functional requirements, the core user flow, data requirements, future scope, risks and mitigations, Day 10 definition of done, and a glossary (DTI, AUC, KS-statistic, SHAP, data leakage) so the document is readable by a non-technical reviewer too.

2. Implementation Blueprint (RiskLens_Implementation_Blueprint.md) - a day-by-day plan for Days 2-10, each with: objective, what I'll learn, features to build, a concrete step-by-step plan, exact files/folders to create, tools/libraries to integrate, testing tasks, common issues and debugging tips, an end-of-day checklist, expected project state/screenshots, and explicit handoff notes for the next day's fresh AI conversation. Written in markdown specifically because it needs to be pasted into a new chat every day, not read once and forgotten.

3. Project Pitch Deck (RiskLens_Pitch_Deck.pptx) - 9 slides covering the problem, target users, solution, key features, technical approach (as a 5-stage visual pipeline), future scope, and vision, in a navy/ice-blue/teal palette with a consistent icon-in-circle motif throughout, sandwich-structured (dark title and closing slides, light content slides between).

## A Real Bug Caught During Deck QA

The Technical Approach slide's 5-stage pipeline visual initially ran the 5th card ("Present") off the right edge of the slide - a spacing math error (5 cards times width plus 4 gaps exceeded the available slide width after accounting for margins). Caught during the required visual QA pass (rendering every slide to an image and actually looking at it, not just trusting the generator code), fixed by recalculating card width and gap size to fit the actual available space, and reconfirmed by re-rendering.

## Key Learnings

1. Scoping discipline has to be interview-driven, not self-imposed after the fact. Asking directly about daily time budget before proposing a feature set is what kept this to single-applicant scoring - if features were designed first and time budget asked about last, features would need to be walked back, which is a worse position than never adding them.

2. A PRD's "Out of Scope" section only works if it's specific enough to settle an argument with yourself later. "No dashboard" is vague enough to rationalize around; "no portfolio-level analytics dashboard (score distributions, aggregate model performance over time)" is specific enough that Day 8 can't quietly redefine what counts as in-scope.

3. The Implementation Blueprint's real audience is a future AI conversation with zero memory of today. Every day's section had to be written as if the person picking it up has amnesia about everything except what's explicitly restated - which is why every day repastes the previous day's key artifact (metrics file, model path, API contract) into that day's Handoff Notes, not just a vague "continue from yesterday."

4. Visual QA on generated documents isn't optional, even for a planning deliverable. The pitch deck's overflow bug would have been invisible in the generator code - it only showed up by actually rendering every slide to an image and looking, which caught a real, user-visible defect before it shipped.

5. Explainability as a stated non-negotiable feature, decided on Day 1, changes downstream decisions in Days 4-7 before they happen. Because SHAP was locked in during discovery rather than added opportunistically later, Day 5's model-selection criteria could already account for "does this model type have a clean SHAP explainer" as a real factor, not a surprise constraint discovered mid-build.

## Deliverables

- RiskLens_PRD.docx - the complete Product Requirements Document
- RiskLens_Implementation_Blueprint.md - the Days 2-10 build plan
- RiskLens_Pitch_Deck.pptx - the 9-slide pitch deck
- prdpage-*.jpg - PRD page renders
- slide-*.jpg - pitch deck slide renders
- day-51.md - this write-up

Note on interview screenshots: today's interview happened directly in this chat conversation rather than inside a generated app, so the screenshots of the interview and the approved project summary should be captured from the chat interface itself.
