# Day 49 of 60 — Personal AI Playbook

## What Was Built

A personalized, modular AI prompt system — **Personal AI Playbook** — built from an interview about how I *actually* use Claude day-to-day, not generic prompt categories. The result: 10 tailored workflow templates across 4 job-specific categories, a Prompt Builder for assembling custom prompts from 9 reusable blocks, and a Loop Builder that converts any prompt into a self-checking autonomous loop.

**Interview answers that shaped the build:**
- **Role:** Credit Risk / Data Science professional
- **Primary AI use case:** Data analysis & modeling (SQL/Python queries, risk model logic, memo drafting)
- **Biggest repetitive task:** Drafting risk memos and committee-ready summaries from raw findings
- **Specific bottleneck:** Turning messy data/findings into something readable takes too long
- **Model:** Claude
- **Experience level:** Advanced+ — builds full AI-powered tools and workflows
- **Desired outcome:** All three — a reusable library, self-improving loops, and speed, in one daily-use system

## Why the Categories Aren't Generic

Rather than showing generic "writing," "coding," "brainstorming" buckets, the Dashboard organizes 10 workflows into exactly the 4 categories that match what came out of the interview:

1. **Risk Memo & Committee Communication** (3 workflows) — directly targets the stated #1 bottleneck: Raw Findings → Committee Memo, Executive Summary Compressor, Before/After Metric Narrative
2. **SQL & Python Query Generation** (3 workflows) — Delinquency/Roll-Rate Query Builder, Python Data Validation Script, Segment Cut Generator
3. **Code Review & Debugging** (2 workflows) — Risk Script Code Review, Bug Hypothesis Generator
4. **Model Documentation & Explanation** (2 workflows) — Model Logic Explainer, Model Change Documentation

Every template uses dropdown menus wherever a fixed set of options makes sense (SQL dialect, audience, tone, analysis type) rather than free text everywhere, exactly per the "give dropdown options wherever needed" requirement.

## Modular Blocks, Not a Prompt Library

The **Prompt Builder** ships 9 reusable blocks (Role, Objective, Context, Constraints, Reasoning Strategy, Output Format, Tone, Examples, Quality Checks). Each carries a plain-language explanation both in the picker *before* it's added and inside the assembled block *after* — so "Reasoning Strategy" is never a mystery term. These 9 blocks alone combine into thousands of possible prompt variations, which is the actual point: a system that scales to problems I haven't hit yet, instead of a library that runs out.

The **Loop Builder** works the same way with 5 components (Goal, Evaluation Criteria, Improvement Strategy, Stop Conditions, Safety Rules) layered on top of any base prompt, turning a one-shot request into a self-evaluating loop.

## Making Purpose Unmistakable (per the spec's explicit requirement)

- A persistent, plain-language explainer sits on the Dashboard by default, listing what each of the 4 tabs is for — dismissible only via the ✕ button, and that dismissal is remembered (localStorage), not re-shown every load.
- A permanent "❓ What is this?" button in the top bar reopens the full explanation on demand, any time — not just on first run.
- Every tab uses plain labels (Dashboard, Prompt Builder, Loop Builder, My Workflows) — no invented jargon.
- Section subtitles describe purpose in plain language (e.g. "Your saved AI prompt workflows, at a glance" — matching the spec's own example almost verbatim, since it's exactly the right register).

## My Results — Verified Functionality

Rather than trust the UI on sight, I tested the actual mechanics:

| Test | Result |
|---|---|
| Live template preview updates when a variable field changes | ✅ Confirmed — typing in "raw findings" immediately reflected in the preview text |
| Favoriting a workflow + Favorites filter | ✅ Favorited item appears, filter shows exactly the favorited set |
| Dashboard search ("SQL") | ✅ Returns exactly the 3 SQL/Python workflows tagged accordingly |
| Prompt Builder: block order in live preview | ✅ ROLE → OBJECTIVE → CONSTRAINTS appeared in the exact order added |
| Prompt Builder: duplicate-block prevention | ✅ Clicking "Role" twice does not add a second Role block |
| Prompt Builder: reorder (↑/↓) | ✅ Block order visibly changed after clicking move-up |
| Loop Builder: live preview contains base task + all added components | ✅ Confirmed BASE TASK, GOAL, EVALUATION CRITERIA, STOP CONDITIONS, SAFETY RULES all present |
| Save from Loop Builder → appears in Custom filter | ✅ Confirmed |
| My Workflows tab shows favorited + custom items together | ✅ Confirmed (scoped correctly to the visible panel) |
| Export produces valid, complete JSON | ✅ Downloaded file contains favorites + full custom workflow with correct template text |
| Keyboard shortcuts (`1`-`4` tabs, `/` search focus, `Esc` closes modals) | ✅ All confirmed working |
| Explainer dismissal persists across a full page reload | ✅ Confirmed via localStorage |
| Console/page errors across the full test suite | 0 |

## Key Learnings

1. **A block-based system is a genuinely different design problem than a prompt library.** The instinct is to store finished prompts; the harder, more valuable version is deciding what the *irreducible components* of a good prompt are (role, objective, constraints, etc.) so they recombine instead of accumulating as one-offs. Fewer moving parts, more coverage.
2. **"Make the purpose unmistakable" is a real, testable UX requirement, not a nice-to-have.** I explicitly verified the explainer stays dismissed across reload (so it doesn't nag) but the help button always reopens it (so it's never truly lost) — those are two different, both necessary, behaviors.
3. **Duplicate-prevention in a block builder is a small detail that avoids a confusing failure mode.** Without it, clicking "Role" twice would silently produce two ROLE: sections in the assembled prompt with no clear way to tell they were duplicates apart from scrolling — worth the extra guard clause.
4. **Testing "My Workflows shows the right count" needs to be scoped to the actual visible panel, not the whole DOM.** My first test assertion failed not because the app was wrong, but because inactive tab panels stay in the DOM (`display:none`, not removed) — my query wasn't scoped to `#myWorkflowsResults` and was silently counting the Dashboard's cards too. A good reminder that a failing test can be the test's bug, not the app's — but only if you actually go verify which one.
5. **The most valuable workflow template wasn't the most complex one.** "Before/After Metric Narrative" — the simplest of the 10, converting two raw numbers into one memo-ready sentence — maps most directly onto the actual stated bottleneck ("turning messy data into something readable takes too long"). Complexity and usefulness aren't the same axis.
6. **Export/import needs to be tested with a real downloaded file, not just a mocked function call.** Triggering the actual browser download event and reading the resulting JSON back off disk confirmed the full round-trip works, including the multi-line template text with embedded newlines surviving JSON serialization correctly.

## Technical Notes

- Single self-contained HTML file, vanilla JS, no frameworks. All state (favorites, custom workflows, explainer dismissal) persisted via `localStorage` under one namespaced key.
- Prompt Builder and Loop Builder both use the same underlying pattern (block picker → assembled list → live preview → copy/save), implemented once and reused, keeping the two builders behaviorally consistent.
- Verified with Playwright across the full feature surface: live preview reactivity, favoriting, search/filter, block reordering and duplicate-prevention, loop assembly, save-to-custom, a real triggered file download for export, all 3 keyboard shortcuts, and persistence across an actual page reload.

## Deliverables

- `main-app.html` — the complete Personal AI Playbook application
- `day49-card.png` — cinematic showcase card
- `exported-workflows.json` — real exported workflow library from a live test session
- `app-dashboard.png`, `app-workflow-modal.png`, `app-prompt-builder.png`, `app-loop-builder.png`, `app-my-workflows.png`, `app-help-modal.png`, `app-dark-mode.png` — full walkthrough screenshots
- `day-49.md` — this write-up
