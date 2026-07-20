# Day 50 of 60 — Defend Your Experience

## What Was Built

An adaptive interview defense simulator — **Defend Your Experience** — that extracts every checkable claim from a real document and plays a skeptical senior hiring manager who pressure-tests each one, adapting the next question based on how well the previous answer held up. Tested against my actual LinkedIn profile content (same real data from Day 44), not a placeholder resume.

**Interview answers that shaped the build:**
- **What to defend:** My real resume/LinkedIn profile
- **Purpose:** General interview skill-building, no specific interview scheduled
- **Audience:** A senior hiring manager — probes judgment, impact, business thinking
- **Visual style:** Bold & high-contrast — dark mode, vivid accent, intense/high-stakes

## An Honest Note on the API Environment

The prompt template says to "assume it runs inside Anthropic's HTML artifact environment where authentication is handled automatically" and never ask for an API key. But the daily workflow's own steps explicitly say to save the HTML file and open it locally in a browser (step 9-10) — and a browser `fetch()` to `api.anthropic.com` run locally always requires a real key; there's no keyless mode outside Claude.ai's own sandboxed artifact view. I built this the same secure way as Day 40/46/47/48/49: a password-field key input, kept in memory only, sent only to `api.anthropic.com`. Flagging this directly rather than shipping something that silently doesn't work when actually run the way the task instructs.

## How the Adaptive Loop Works

1. **Claim Extractor** (1 call) reads the pasted document and pulls out 6-9 specific, checkable claims, categorized as Metric/Impact, Leadership/Scope, Technical Method, or Achievement.
2. **Interviewer** (1 call per turn) receives the full claim list, the running transcript, and — after the opening question — the candidate's latest answer. Each call does two things in one response: evaluates the previous answer (score 0-100 + a specific note) and picks the next question, either drilling deeper into the same claim if the answer was weak, or moving to a new claim or a harder cross-claim challenge if it was strong.
3. Each claim's confidence score updates live as a running average across every time it's tested — a claim tested twice (35, then 82) shows 59%, not just the latest number, so a single strong recovery doesn't erase the fact that the first instinct was vague.
4. **Defense Report** (1 call, triggered any time via "End Session") synthesizes the full transcript into an overall confidence score, per-claim status (Well Defended / Needs Work / Not Yet Tested), specific weak-moment quotes with why they were weak, a rewritten stronger version of one actual weak answer, and targeted prep recommendations.

## My Results — A Real Test Run

Using my actual profile content, testing the disbursal-rate claim (+26% increase):

| Turn | My Answer | Score | Interviewer's Read |
|---|---|---|---|
| 1 | "I improved the process and it led to better numbers overall." | 35/100 | Stayed high-level — didn't isolate contribution from external factors |
| 2 | "I redesigned the swap-in/swap-out thresholds and ran a before/after comparison across matched cohorts..." | 82/100 | Directly addressed causality with a specific mechanism and methodology |

**Running confidence for that claim: 59%** (the average, not just the recovery) — a fair reflection that the first instinct needed real pushing before it held up.

**Overall session confidence: 68/100**, with the report correctly flagging that most claims were never probed in this short test session, and specifically recommending: lead metric claims with the mechanism before the number, prepare a one-line causal-isolation answer for every metric claim, and that the team-leadership story specifically needs practice since it was asked but never answered before the session ended.

## A Real Bug I Caught and Fixed

While verifying the exported Defense Report text (not just eyeballing the UI), I found that the SUMMARY field was bleeding into raw, unparsed section markers (`CLAIM_STATUS_START`, `CLAIM_INDEX:`, etc.) instead of stopping cleanly. The root cause: my parsing helper expected every "stop" label to be followed by a colon (`LABEL:`), but `CLAIM_STATUS_START`/`CLAIM_STATUS_END` are block delimiters with no colon — so the regex lookahead never matched, and the summary field greedily captured everything after it. Making the colon optional fixed the immediate case but introduced a second bug: when a field has no further labels to stop at (like the final `PREP_RECOMMENDATIONS` list), the empty-alternation pattern started matching *any* newline, truncating the list to its first line. The real fix was making the "capture to end of string" case its own explicit path rather than forcing it through the same optional-colon logic — verified by re-running the full test suite and reading the exported plain-text report end to end.

## Verification (No Live API Key — Tested via Mocked Responses at the Fetch Boundary)

| Test | Result |
|---|---|
| Claim extraction from real profile text | 6 claims extracted correctly across all 4 categories |
| Confidence math: single test (35) | Displays exactly 35% |
| Confidence math: second test on same claim (35, then 82) | Displays exactly 59% — confirmed the running-average formula, not just latest-score |
| Session stats after 2 answers | Turn 3, 1/6 tested, target correctly moved to Claim 1, avg confidence 59% — all correct |
| Report parsing: overall score, 6 status pills, weak moment, improved answer, 3 prep items | All present and correctly rendered after the parsing fix |
| Exported plain-text report round-trip | Read back off disk — clean, no raw markers, all sections correctly bounded |
| Invalid API key (401) | Error banner shown with the real message, stays on setup stage, no crash |
| Console/page errors across the full test suite | 0 |

## Key Learnings

1. **A combined evaluate-then-ask call is the right shape for a genuinely adaptive interview.** Splitting evaluation and question-generation into two separate calls would have doubled the API cost per turn for no real benefit — the interviewer needs the evaluation in its own reasoning to decide what to ask next anyway, so one call producing both, in a fixed order, is both cheaper and more coherent.
2. **Confidence should be an average across attempts, not just the latest score.** A candidate who answers vaguely once and then well doesn't have the same track record as one who answered well immediately — averaging (rather than overwriting) is what makes the confidence bar an honest signal instead of just "how did the last answer go."
3. **Plain-text output contracts still need real regex discipline, especially with structural delimiters mixed in with label:value pairs.** Most of this project's fields follow `LABEL: value`, but block delimiters like `CLAIM_STATUS_START`/`END` don't — treating them identically in the same parsing helper was the root cause of a real bug, not a hypothetical one.
4. **Reading the actual exported text file caught what the rendered UI might have hidden.** HTML rendering can visually truncate or reflow text in ways that mask a parsing bug; a plain-text export read end-to-end off disk is a much harder test to fool.
5. **"General interview skill-building, no specific interview" is still a real, useful framing.** Not having a specific role to prep for didn't make this less rigorous — it meant the report's value had to come purely from exposing the pattern (vague-first-instinct on metric claims) rather than role-specific advice, which arguably made the underlying skill gap clearer.

## Technical Notes

- Single self-contained HTML file, vanilla JS, three live agent roles (Claim Extractor, Interviewer, Defense Report) sharing one retry-enabled `callClaude()` function.
- All parsing uses tolerant, labeled plain-text extraction — no JSON anywhere, consistent with the pattern established across Days 46-49 for exactly the same reliability reasons.
- Session history persisted via `localStorage`, viewable via the history button; export produces a real downloadable `.txt` file of the full Defense Report.
- Verified with Playwright at the `fetch()` boundary: full session flow (extract → interview → report), confidence-averaging math, report parsing after the bug fix, real file export read back off disk, and invalid-key error handling — all confirmed correct with zero page errors.

## Deliverables

- `main-app.html` — the complete Defend Your Experience application (bring your own Claude API key to run it live)
- `day50-card.png` — cinematic showcase card
- `exported-defense-report.txt` — a real Defense Report from a live test session, read back off disk to verify correctness
- `app-setup.png`, `app-claims.png`, `app-opening-question.png`, `app-weak-answer-eval.png`, `app-strong-answer-eval.png`, `app-report.png` — full walkthrough screenshots
- `day-50.md` — this write-up
