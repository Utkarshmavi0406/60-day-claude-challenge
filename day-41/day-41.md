# Day 41 of 60 — Interactive Learning Studio: Probability Distributions

## What Was Built

A complete, self-contained interactive course — **Probability Distributions: Binomial, Poisson & Normal** — built through a scoped-down interview (Data Science & Statistics → Probability Theory → Probability Distributions), with Claude auto-structuring all four modules and closing sections.

This isn't a roadmap or a summary — it's a full teaching experience: four progressively harder modules, five live mathematical simulators the learner controls directly, 16 auto-graded quiz questions with instant per-answer explanations, a scenario-based final challenge, a printable cheat sheet, and a curated "continue learning" section.

## Course Structure

**Introduction** — learning objectives, ~55 min estimated time, prerequisites (basic algebra), expected outcomes, and a reward system (a "Distribution Master" badge unlocked on completion).

**Module 1 — The Binomial Distribution** (foundational)
Discrete vs. continuous random variables, the four Binomial conditions, the PMF formula, a live n/p simulator with real-time mean/variance, a worked defective-bulb example, and a misconception callout on what "independence" actually means.

**Module 2 — The Poisson Distribution** (building)
Modeling event counts at a known rate, the PMF formula, why mean = variance = λ, how Poisson emerges as the limit of Binomial as n→∞, a live λ simulator, and a worked support-inbox example.

**Module 3 — The Normal Distribution** (continuous distributions)
The empirical rule (68–95–99.7), the density formula, a live μ/σ curve with shaded standard-deviation bands, an interactive z-score calculator with percentile lookup, and the n·p≥5 rule for Binomial→Normal approximation.

**Module 4 — Choosing & Connecting** (mastery)
A side-by-side comparison table, a live Central Limit Theorem simulator (drag dice-averaged-per-sample from 1 to 12 and watch a flat distribution become a bell curve over 2,000 simulated trials), and three scenario-matching exercises.

**Each module ends with a 4-question quiz** — instant per-question correct/incorrect highlighting, a written explanation for every answer, a score summary, and a button that unlocks the next module.

**Closing sections** — a three-part applied final challenge (Poisson → Binomial → Normal in one call-center scenario), a printable formula cheat sheet (`window.print()` with dedicated print CSS), and a Continue Learning section with books, documentation, research directions, communities, practice platforms, search keywords, and follow-up AI prompts.

## My Results

Verified by completing the entire course programmatically end-to-end:

| Check | Result |
|---|---|
| All 4 modules + final section reachable and unlockable in sequence | ✅ Confirmed via nav-pill state (`done` on all 6 sections) |
| Quiz scoring accuracy (3 correct / 1 intentionally wrong) | ✅ Correctly scored 3/4, right/wrong answers highlighted, all 4 explanations shown |
| Binomial math correctness (n=20, p=0.2) | ✅ Mean = 4.00, Variance = 3.20 — matches n·p and n·p·(1−p) exactly |
| Progress bar after Module 1 completion | ✅ 33% (2 of 6 sections) |
| Console/page errors across full run | 0 |

## Key Learnings

1. **A marker-driven unlock system needs its state machine designed before the content.** Deciding upfront that sections are indexed 0–5 and that `progress.completed` gates the next nav-pill made module locking, the progress bar, and localStorage persistence all fall out of one simple array — rather than needing separate logic per module.
2. **Simulators teach faster than static diagrams for this topic specifically.** Letting the learner drag n and p and watch a Binomial distribution skew live communicates "why does p away from 0.5 cause skew" far more directly than a paragraph describing the same fact — this became the anchor design decision for every module.
3. **The Central Limit Theorem is best taught by breaking the learner's expectation live.** Starting the CLT simulator at N=1 (a flat, obviously non-Normal die roll) and letting the learner slide up to N=12 makes the emergence of the bell curve feel discovered rather than asserted.
4. **Quiz distractors need to test real misconceptions, not just wrong arithmetic.** Several questions (e.g., "which of these is NOT a Binomial requirement") were written around the actual misconception callouts embedded earlier in the same module, so getting a question wrong points the learner back to something they already read.
5. **Precomputed math needs its own sanity check, not just visual plausibility.** Verifying mean/variance output programmatically against the textbook formulas (n·p, n·p·(1−p), λ, λ) caught the kind of silent off-by-one or scaling bug that would otherwise only surface as "the bars look a little off."
6. **A printable cheat sheet is a CSS problem, not a content problem.** The same HTML that's fully interactive on screen becomes a clean one-page reference on paper using a single `@media print` block that hides everything except the final section — no separate "printable version" of the content was needed.

## Technical Notes

- Single self-contained HTML file, vanilla JS, all charts rendered as hand-built inline SVG (bar charts for discrete PMFs, smoothed path curves with shaded standard-deviation bands for the Normal PDF) — no charting library.
- Math implemented from scratch: factorial/combination for the Binomial PMF, a direct Poisson PMF, a Normal PDF, and an Abramowitz–Stegun `erf` approximation for the Normal CDF used in the z-score percentile lookup.
- Progress persisted via `localStorage` (safe here since this is a standalone file, not a Claude.ai artifact), with a reset control that clears saved state and quiz UI back to first-attempt condition.
- Verified with Playwright (system Chrome): full course walkthrough across all 4 modules and quizzes, live slider interactions on every simulator, dark mode, and a second pass specifically checking quiz-grading DOM state and Binomial math output against hand-calculated expected values.

## Deliverables

- `main-app.html` — the complete Interactive Learning Studio course
- `day41-card.png` — cinematic showcase card
- `app-intro.png`, `app-module1.png`, `app-module1-simulator.png`, `app-quiz1-result.png`, `app-module2.png`, `app-module3.png`, `app-module3-zscore.png`, `app-module4.png`, `app-module4-clt.png`, `app-final-challenge.png`, `app-final-revealed.png`, `app-dark-mode.png` — full course walkthrough screenshots
- `day-41.md` — this write-up
