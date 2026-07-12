# Day 43 of 60 — AI Workflow Architect

## What Was Built

A complete, end-to-end interactive workflow application — **AI Workflow Architect** — mapping the recurring process a credit risk analyst runs to monitor an existing loan book for early signs of deterioration: **Delinquency & Default Trend Monitoring**.

**Interview path that shaped the scope** (mirroring the prompt's own example depth of Marketing → Social Media → Instagram → Personal Brand Growth):
- **Domain:** Finance / Credit Risk / Investing
- **Process:** Portfolio Risk Monitoring
- **Specific focus:** Delinquency & default trend monitoring across a loan book
- **Structure:** Auto-decide — Claude designed the full 6-stage workflow

This is a genuine end-to-end workflow, not a checklist: it goes from raw loan-level data extraction all the way to a committee escalation decision and the feedback loop that closes the cycle.

## The 6-Stage Workflow

1. **Data Collection & Preparation** — pulling and validating the loan-level extract
2. **Delinquency & Roll Rate Calculation** — bucket classification, transition matrices, vintage curves
3. **Trend Analysis & Anomaly Detection** — separating structural deterioration from seasonal noise
4. **Root Cause & Driver Investigation** — triangulating quantitative data with practitioner context
5. **Reporting & Escalation** — the executive summary, plus an **interactive 3-question escalation decision tree**
6. **Action & Monitoring Cadence** — closing the feedback loop and locking in the next cycle

Every stage includes: objectives, tasks, best AI tools (with a clearly marked recommended primary tool and *why*), alternative tools, ready-to-use prompts (bookmark + one-click copy on each), best practices, common mistakes, expected outputs, a time estimate, and efficiency tips — exactly the structure the brief specified, generated specifically for this process rather than generically.

## Interactive Features

- **Interactive pipeline diagram** on the Overview — click any node to jump straight to that stage, with live completion state
- **Escalation decision tree** embedded in Stage 5 — a real 3-question branching framework (magnitude → materiality → systemic vs. isolated cause) that produces one of four distinct, evidence-backed recommendations
- **Progress tracking** — mark each stage reviewed; a progress ring on Overview and checkmarks in the sidebar update live, persisted via `localStorage`
- **Notes** — a per-stage notes field, autosaved as you type, aggregated in a dedicated Notes & Bookmarks view
- **Bookmarks** — star any prompt to save it, aggregated in the same view for quick reference
- **AI Stack comparison table**, **Future Automation Opportunities**, **Workflow Summary**, curated **Learning Resources/Communities/Search Keywords**, and **4 additional deep-dive prompts**
- **Printable Workflow Guide** — a condensed one-page reference reachable via a dedicated view and `window.print()`, with matching print CSS

## My Results

Verified with an extensive automated interaction test rather than a single pass:

| Check | Result |
|---|---|
| All 6 stage views render with full content | ✅ Confirmed — 6 stage nav items, 6 pipeline nodes, all stage views exist in DOM |
| Decision tree, path Yes→Yes→Yes (large, material, systemic) | **"Escalate to Risk Committee"** — correct |
| Decision tree, path No (deviation under 1.5× trailing average) | **"No escalation needed"** — correct |
| Progress ring after marking 2 of 6 stages reviewed | Displays "2/6" — correct |
| Bookmark a prompt, add a stage note | Both appear correctly in the aggregated Notes & Bookmarks view |
| Data persistence across full page reload | Stage progress, notes, and bookmark all survived reload via `localStorage` |
| Console/page errors across the full test | 0 (after fixing one bug — see Key Learnings) |

## Key Learnings

1. **Data-driven rendering pays off fast on content-heavy builds.** Rather than hand-writing six near-identical stage layouts, I modeled every stage as a JS object (objectives, tasks, tools, prompts, mistakes, outputs) and wrote one `renderStageHTML()` template. This meant 100% of my authoring effort went into workflow-specific domain content instead of repetitive markup — and every stage automatically got notes, bookmarks, and progress tracking wired up identically for free.
2. **A wrapper container has to survive the assembly step.** My Python assembly script replaced the `<div id="viewsRoot"></div>` placeholder with static view content, which accidentally deleted the container element itself — so the JS trying to `appendChild` the six dynamically-built stage views threw `Cannot read properties of null`. The fix was keeping the wrapper div and inserting content *inside* it, not replacing it outright. Caught immediately by an automated sanity check before it ever reached a "looks fine" screenshot.
3. **A decision tree is a much stronger deliverable than a decision checklist.** Framing "should this escalate?" as three sequential, falsifiable yes/no questions (rather than a bulleted list of "consider these factors") forces the same rigor every cycle and produces a specific, defensible recommendation instead of a vague judgment call — I tested both branches to confirm the logic actually discriminates correctly.
4. **Closing the loop (Stage 6) is what separates monitoring from reporting.** It would have been easy to end the workflow at the committee memo in Stage 5. Explicitly adding a stage whose entire purpose is checking whether *last* cycle's actions worked is what turns this into a genuine recurring process rather than a one-off analysis.
5. **Event delegation is the right call when content is entirely dynamic.** Since all 6 stage views, the bookmark buttons, and the notes textareas are built by JavaScript rather than hardcoded in HTML, wiring listeners via `document.body.addEventListener` with `closest()` matching (rather than querying and binding after each render) meant new content never silently lost its interactivity.
6. **Verifying persistence requires an actual reload, not just checking in-memory state.** The most convincing proof `localStorage` is working correctly is reloading the page and re-reading it fresh — testing against the same page instance that wrote the data can hide bugs where state looks right in memory but was never actually serialized.

## Technical Notes

- Single self-contained HTML file, vanilla JS, all workflow content modeled as structured data and rendered through shared templates — no external libraries or frameworks.
- State (stage progress, notes, bookmarks) persisted under one namespaced `localStorage` key (`awa_v1`), safe here as a standalone file rather than a Claude.ai artifact.
- Verified with Playwright (system Chrome): full navigation across all 6 stages plus Overview/Stack/Notes/Print views, both decision-tree branches, mark-reviewed toggling, bookmark/note creation, and a reload-based persistence check.
- One real bug (a null container reference from the file-assembly step) was caught by an automated sanity check before the full test suite ran, and fixed prior to delivery.

## Deliverables

- `main-app.html` — the complete AI Workflow Architect application
- `day43-card.png` — cinematic showcase card
- `app-overview.png`, `app-stage1.png` through `app-stage6.png`, `app-decision-tree-result.png`, `app-overview-progress.png`, `app-notes-bookmarks.png`, `app-stack.png`, `app-print-guide.png`, `app-light-mode.png` — full walkthrough screenshots
- `day-43.md` — this write-up
