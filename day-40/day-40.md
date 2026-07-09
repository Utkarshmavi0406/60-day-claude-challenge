# Day 40 of 60 — Underwriting Copilot (AI Product Design)

## What Was Built

A custom AI assistant, designed end-to-end through a structured product interview rather than a single prompt: **Underwriting Copilot**, a decision-support tool for credit analysts at a lending institution. It interviews an analyst conversationally to gather an applicant's loan, income, debt, and credit details, then generates a structured, fair-lending-aware underwriting report with a clear Approve / Decline / Refer verdict — live, via the real Claude API.

**Interview answers that shaped the design:**
- **Domain → Niche:** Finance / Credit Risk → Credit Risk Underwriting Copilot
- **Audience & outcome:** Credit analysts/underwriters deciding approve/decline/refer
- **Inputs:** Multi-turn conversation — the assistant asks follow-up questions interactively
- **Output:** A full structured report (income analysis, DTI, credit history, red flags, recommendation)
- **Tone:** Professional, formal, institutional

## The System Prompt

The full production system prompt lives in `system-prompt.md` and is also embedded directly in the app (visible in the "How this was built" panel). Four design decisions anchor it:

1. **Decision support, not decision-maker.** Every report explicitly reminds the analyst that a human retains final authority and must apply policy and law before acting.
2. **One question at a time.** Rather than a giant intake form, the assistant gathers loan details → income/employment → debts → credit history → other factors conversationally, adapting to what's already been said.
3. **A strict, parseable output contract.** Every final report must begin with the literal line `===FINAL_REPORT===`, which lets the frontend reliably detect "this is a report" and switch rendering modes instead of guessing from prose.
4. **Fair-lending guardrails are hard-coded, not implied.** The prompt explicitly lists ECOA/Regulation B protected characteristics (race, religion, sex, marital status, public assistance income, etc.) and zip-code proxying as factors that must never enter the risk assessment — this isn't left to the model's judgment.

## App Features

- **Live Claude API integration** — real `fetch` calls to `https://api.anthropic.com/v1/messages` using a user-supplied API key (kept in memory only, never persisted), with a model picker (Sonnet 5 / Opus 4.8 / Haiku 4.5).
- **Conversational interview UI** — chat bubbles for the back-and-forth interview, with a sidebar progress tracker (Loan details → Income → Debts → Credit history → Final report) that advances as topics are covered.
- **Automatic report-card rendering** — the moment a reply starts with `===FINAL_REPORT===`, the frontend swaps from a chat bubble to a formatted report card: color-coded verdict pill (green Approve / amber Refer / red Decline), sectioned markdown body, and Copy/Download actions.
- **Graceful states throughout** — typing indicator while waiting on the API, an empty state before starting, and an inline error banner (not a silent failure) for a missing/invalid key, rate limits, or network errors.
- **Collapsible "How this was built" panel** — covers system prompt design, UI decisions, and future extension ideas (tools, memory, multi-step workflows), plus the full system prompt for reference.
- Dark mode, responsive layout, keyboard send (Enter to send, Shift+Enter for newline).

## Key Learnings

1. **A marker string is a simple, effective mode-switch mechanism.** Rather than trying to detect "is this a report?" from prose heuristics, having the system prompt emit an exact literal line (`===FINAL_REPORT===`) turned frontend routing into a trivial `startsWith` check instead of fragile pattern matching.
2. **Guardrails belong in the prompt, not the frontend.** It would be tempting to filter protected-class terms in JavaScript, but that's the wrong layer — the model needs to know *why* those factors are excluded so it can explain the exclusion to the analyst, which only works if the constraint lives in the system prompt itself.
3. **Browser-side Claude API calls need an explicit opt-in header.** `anthropic-dangerous-direct-browser-access: true` is required for `fetch` calls to succeed from a browser origin — worth calling out explicitly since it's easy to miss and get a confusing CORS-shaped failure instead.
4. **Conversational input still needs structured output guarantees.** Free-text interview input feels natural, but the deliverable a credit analyst actually needs is a consistent, scannable report — solving this required treating "structured section order" as a hard contract in the prompt, not a suggestion.
5. **Progress indicators built from conversation content are inherently approximate.** The sidebar's stage tracker is keyword-heuristic (does the reply mention "income", "debt", etc.) rather than ground truth, which is an honest limitation worth stating rather than presenting as precise tracking.
6. **Interviewing for product requirements up front changes what gets built.** Answering "who is this for" and "what does one session need to produce" before touching code meant the UI design (conversational input, structured report output, institutional visual language) followed directly from stated product decisions instead of being retrofitted.

## Technical Notes

- Single self-contained HTML file, vanilla JS, no frameworks or external libraries — only Google Fonts as a progressive enhancement.
- Verified with Playwright using mocked API responses (no live key available in this environment): confirmed the full interview flow, correct report-card rendering with the right verdict-pill class, stage progression, error banner on a missing key, and zero console/page errors across the whole run.
- The report renderer includes a small custom markdown-to-HTML pass (headers, bold, bullet lists) rather than pulling in a markdown library, keeping the file dependency-free.

## Deliverables

- `main-app.html` — the complete Underwriting Copilot application (bring your own Claude API key to run it live)
- `system-prompt.md` — the full production system prompt
- `day40-card.png` — cinematic showcase card
- `app-empty-state.png`, `app-connected.png`, `app-interview-q1.png`, `app-report.png`, `app-docs-panel.png`, `app-dark-mode.png`, `app-error-state.png` — feature screenshots (interview flow tested with mocked API responses)
- `day-40.md` — this write-up
