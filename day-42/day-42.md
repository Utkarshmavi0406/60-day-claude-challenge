# Day 42 of 60 — Personal Financial Command Center

## What Was Built

A complete, interactive financial dashboard — not a simple expense tracker — built for a specific, interview-derived profile: a **student earning paid internship income, with no student loans, focused on both goal-based saving and early investing.** Every module, the health score formula, and the AI-generated insights are tuned specifically to that situation (temporary internship income, no debt drag, dual savings/investing priorities).

**Interview answers that shaped the design:**
- **Persona:** Student
- **Income situation:** Paid internship income
- **Debt:** No student loans
- **Priority:** Both saving for a goal AND investing
- **Modules:** Auto-decide — Claude designed the full module set

## Modules Built

1. **Overview** — a live 100-point Financial Health Score gauge with a transparent 5-factor breakdown, 4 key metric cards, a monthly cash-flow bar chart, a spending-by-category donut chart, and rule-based AI insights that respond to the actual data.
2. **Income & Expenses** — add/edit/delete income sources (with an optional end date for temporary internship income) and categorized expenses, plus a dedicated Subscriptions snapshot card — the category students most often overspend in without noticing.
3. **Budget** — per-category budget inputs, a grouped budget-vs-actual bar chart, and a status list flagging over-budget categories in coral.
4. **Savings Goals** — add goals with a target, current amount, and target date; each goal shows a progress bar and a live-calculated "you need to save $X/month to hit this on time."
5. **Investments** — add holdings with balance, monthly contribution, and expected return; a compound-growth line chart projects contributed-vs-value over 1/5/10-year toggles.
6. **What-If Simulator** — three sliders (extra monthly investment, dining/entertainment spending adjustment, post-internship income) that clone the data model in memory and show a live "Current vs. Projected" comparison of health score, net cash flow, and 12-month investment value, plus a dedicated "what happens the month my internship ends" analysis — before anything is saved.
7. **Tips & Checklist** — internship-specific financial tips (treat the income as temporary, capture any 401(k) match, redirect the loan payment you don't have), a persisted planning checklist, and curated books/tools/communities/search keywords/AI prompts.
8. **Printable Report** — a clean one-page summary (score, income/expenses, goals, investments, budget, top insights) reachable via a dedicated view and a `window.print()` button with matching print CSS.

## My Results

Verified with an extensive automated test pass rather than eyeballing it once:

| Check | Result |
|---|---|
| Health score computed from seed data | **79/100** ("Good" tier) |
| Manual recomputation of income/expenses/savings rate | Income $3,200, Expenses $1,402.48, Net $1,797.52, Savings rate 56.2% — **matches displayed values exactly** |
| Investment 12-month projection ($600 balance, $200/mo, 7% annual) | Formula gives $3,122 — **matches app output exactly** |
| Goal required-monthly-contribution ($3,000 target, $1,200 current, 8 months) | $225/month — **matches app output exactly** |
| What-If Simulator direction test | Adding +$500/mo contribution raised the projected health score from 79 → 84, correctly in the expected direction |
| Data persistence across a full page reload | Added expense, added goal, and 2 checklist items all correctly survived reload via `localStorage` |
| Console/page errors across the full interaction test | 0 (after fixing one bug — see Key Learnings) |

## Key Learnings

1. **A single syntax typo can silently disable an entire app.** An over-escaped apostrophe in a `confirm()` string (`you\\'ve` instead of `you have`) threw a parse-time JS error that prevented *every* event listener in the file from attaching — including navigation. The app still rendered its default view, so it looked fine at a glance; only automated interaction testing caught it, which is exactly the kind of bug a "looks right in a screenshot" review would miss.
2. **A believable financial health score needs believable seed data, not just a correct formula.** I deliberately tuned the sample dataset so one budget category runs slightly over (Food) and the emergency fund and investment-consistency components land short of full marks — producing a score of 79 instead of a maxed-out 100. A demo dataset that always scores perfectly hides whether the scoring logic actually responds to real variation.
3. **"What-if" only feels trustworthy if it doesn't touch real data until asked to.** Cloning the entire data object (`JSON.parse(JSON.stringify(DATA))`) for scenario math, and only committing changes on an explicit "Apply this scenario" click, means dragging a slider can never accidentally corrupt the user's actual budget — a meaningful trust boundary for a financial tool specifically.
4. **Treating recurring cost categories as a lens, not a separate data structure, reduces redundancy.** Subscriptions didn't need their own array — filtering the existing Expenses list by `category === 'Subscriptions'` satisfies the "subscriptions module" requirement with zero duplicated state and guarantees the two views can never drift out of sync.
5. **A profile-specific detail (internship end date) changes what "AI insight" even means here.** Because this persona's income is explicitly temporary, the single highest-value insight isn't a generic budgeting tip — it's a countdown-aware warning tied to the actual end date the user entered, which is why that logic got its own dedicated section in the What-If module rather than being one line among many in Overview.
6. **Verifying financial math programmatically is non-negotiable for this category of app.** Hand-deriving the expected DTI-style figures (savings rate, compound growth, required monthly savings) and asserting the app's displayed numbers against them caught real correctness, not just "the chart looks plausible" — the same standard I'd want from any tool making financial recommendations.

## Technical Notes

- Single self-contained HTML file, vanilla JS, all charts (donut, grouped bar, dual-line) hand-built as inline SVG — no charting library.
- Data model persisted via `localStorage` under one namespaced key (`pfcc_v1`), safe here since this is a standalone file, not a Claude.ai artifact. A "Reset to sample data" control clears back to the seeded profile.
- Verified with Playwright (system Chrome): full navigation across all 8 modules, live form interactions (add expense, add goal, investment projection range toggle, checklist toggling), dark mode, and — critically — a second pass that reloaded the page and asserted `localStorage` contents to confirm real persistence rather than just in-session state.
- One real bug was caught and fixed during testing (see Key Learnings #1) — the fix and the passing re-test are both part of this delivery, not glossed over.

## Deliverables

- `main-app.html` — the complete Personal Financial Command Center
- `day42-card.png` — cinematic showcase card
- `app-overview.png`, `app-cashflowView.png`, `app-budgetView.png`, `app-goalsView.png`, `app-investView.png`, `app-whatifView.png`, `app-tipsView.png`, `app-reportView.png` — every module
- `app-add-expense.png`, `app-add-goal.png`, `app-whatif-adjusted.png`, `app-invest-10yr.png`, `app-checklist.png`, `app-dark-mode.png` — interaction screenshots
- `day-42.md` — this write-up
