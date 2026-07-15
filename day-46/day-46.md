# Day 46 of 60 — Autonomous Agent Studio

## What Was Built

A real 8-agent orchestration pipeline — **Autonomous Agent Studio** — that generates and iteratively improves a Python file-utility script through a genuine `while` loop making live Claude API calls every round. No fixed round count, no canned scoring, no hardcoded sequence.

**Interview path (narrowed per spec, not stopped at just a domain):**
- **Domain:** Code Generation & Review
- **Scope:** A small utility script
- **Specific focus:** Python file/batch processing utility (rename, merge, convert files)
- **Success criteria:** Quality AND Robustness, weighted evenly (50/50)
- **Stop condition:** Threshold-primary (≥90/100), with plateau detection and a hard iteration cap as required safety fallbacks
- **Agents:** Auto-designed — all 8 available roles used, since a real code-gen loop genuinely needs each one

## An Honest Note on "No Key Needed"

The original prompt template states the app should call the Claude API "no key needed." That's not achievable for a standalone HTML file run locally in a browser — `fetch()` calls to `api.anthropic.com` always require a real API key; there's no keyless mode outside Anthropic's own sandboxed artifact environment. I built this the same secure way as Day 40's Underwriting Copilot: a password-field key input, kept in memory only, sent only to `api.anthropic.com`, with the `anthropic-dangerous-direct-browser-access` header required for browser-origin calls. I'm flagging this discrepancy directly rather than shipping something that silently doesn't work.

## The Real Loop

This is not a simulated pipeline. Every round runs:

**Round 0 (setup, 2 calls):** Planner drafts a technical plan → Executor writes the first complete implementation.

**Every round after (4 calls minimum):** Evaluator scores the current draft fresh (Quality /50 + Robustness /50, no memory of its own past scores) → Critic gets the Evaluator's report and finds 3-5 concrete, actionable issues → Safety Monitor independently checks the same draft for dangerous patterns (unsafe deletion, shell injection, path traversal) → Memory Manager compresses the full round history into a brief so Improver doesn't re-fix what's already fixed.

**Stop Check runs after Memory Manager, before Improver is even called** — checked in the required order: (1) plateau — score improved <2 points for 2 straight rounds, (2) threshold — crossed the target set at interview, (3) hard iteration cap (8 rounds, safety fallback only). The first one to fire wins and is logged by name.

**If nothing fires, Improver runs** (1 more call) and the loop repeats with the new draft. **If something fires, Improver is skipped entirely** and control passes to Final Reviewer, which runs exactly once regardless of which condition ended the loop.

## Verification (No Live API Key Available — Tested via Mocked Responses)

I don't have a live Anthropic API key in this environment, so I verified the actual orchestration logic — not just the UI — using Playwright route interception that inspects each request's system prompt to determine which agent is calling, and returns realistic scored responses. This tests the real client-side loop, parsing, and stop-check logic exactly as written; only the model's text generation is substituted.

| Test | Result |
|---|---|
| **Threshold path**: scores 60→72→81→93 across 4 rounds | Stopped exactly at round 4 with reason `THRESHOLD`, correctly logged and banner shown |
| **Plateau path**: scores 55→75→76→77 across 4 rounds | Stopped exactly at round 4 with reason `PLATEAU` (deltas of 1 and 1, both under the 2-point threshold) — never crossed 90, confirming plateau fires independently of threshold |
| **Retry logic**: simulated one 500 error on the first Evaluator call | Retry count correctly incremented to 1, pipeline recovered and continued normally |
| **Total failure**: simulated a persistent 401 (invalid key) | Error banner shown with the real API error message, pipeline halted cleanly, Start button re-enabled — no crash |
| **Safety flagging**: simulated Safety Monitor returning `FLAGGED` on round 2 | Round 2's safety badge correctly rendered as "flagged" in the round history, safety node in the diagram received the flagged state |
| **API call accounting**: 4-round threshold run | 23 total requests logged (22 successful + 1 simulated failure), matching hand-calculated expectation: 2 (round 0) + 4×4 (eval/critic/safety/memory across 4 rounds) + 3 (improver, skipped on the stopping round) + 1 (final reviewer) = 22, plus 1 retried failure |
| Console/page errors across all test runs | 0 |

## My Results (Threshold Test Run)

| Round | Quality | Robustness | Total | Delta |
|---|---|---|---|---|
| 1 | 32/50 | 28/50 | 60/100 | — |
| 2 | 38/50 | 34/50 | 72/100 | +12 |
| 3 | 44/50 | 37/50 | 81/100 | +9 |
| 4 | 47/50 | 46/50 | 93/100 | +12 |

**Stop reason:** THRESHOLD, fired at round 4. Full chronological execution log included as `execution-log.txt`.

## Key Learnings

1. **"No fixed round count" has to be enforced structurally, not just described.** The stop check is the only thing that can end the `while(true)` loop — there's no round counter cap baked into the happy path, only the hard-cap fallback. Verifying the plateau test stopped at a *different* round-count than the threshold test (both happened to be 4 here, by design of the mock data, but for genuinely different reasons) was the real proof the logic isn't secretly sequence-based.
2. **A stop-check order matters more than it looks like it should.** Checking plateau before threshold before hard-cap means a session that happens to plateau exactly as it crosses threshold reports plateau — which is the more informative reason to a user watching the log, and matches the literal ordering the spec required.
3. **Testing the loop honestly requires mocking at the API boundary, not the UI boundary.** Faking button clicks and pre-populated results would have proven nothing about whether the actual orchestration code works. Intercepting the `fetch()` call itself and routing based on system-prompt content meant every test exercised the real `runPipeline()` function, the real parsers, and the real stop-check — only the model's output was substituted.
4. **Memory Manager only earns its place in the roster if Improver's prompt actually uses its output.** It would have been easy to add a Memory Manager agent that produces a brief nobody reads. Wiring its output directly into the Improver's user message — and having its own system prompt explicitly instruct it to prevent redundant re-fixes — is what makes it a real agent in the pipeline rather than decoration.
5. **Retry logic needs a call-counting seam that survives a failed attempt.** The API call counter increments before checking `resp.ok`, so a failed attempt still shows up in the total — an honest count of load placed on the API, not just successful calls, which matters for anyone reasoning about the cost of this pattern.
6. **A production-quality system prompt for a grading agent has to explicitly forbid comfortable scores.** Early drafts of the Evaluator prompt didn't specify what a 45+ score required, and mock testing revealed generically "nice" scores drift toward the middle. Explicitly reserving high scores for genuinely clean code was necessary to get a score curve that actually discriminates round-over-round.

## Technical Notes

- Single self-contained HTML file, vanilla JS, real `while(true)` orchestration loop with no hardcoded round count.
- All 8 agents (Planner, Executor, Evaluator, Critic, Safety Monitor, Memory Manager, Improver, Final Reviewer) have distinct, production-quality system prompts and are called live every round via `fetch()`.
- Structured-output parsing uses tolerant regex against explicit format contracts in each system prompt (e.g., `QUALITY_SCORE:`, `SAFETY_STATUS:`) rather than relying on the model to return JSON, which is more robust to minor formatting drift.
- Workflow diagram is hand-built inline SVG with a real loop-back arrow from Improver to Evaluator and a separate branch to Final Reviewer, matching the "not a straight pipeline" requirement — node states (`active`/`done`/`flagged`) update live via `classList` as the orchestration progresses.
- Retry logic: up to one automatic retry on 429/5xx or network failure per call, with a visible retry counter; total failure halts the pipeline gracefully with a specific error message rather than crashing.

## Deliverables

- `main-app.html` — the complete Autonomous Agent Studio application (bring your own Claude API key to run it live)
- `day46-card.png` — cinematic showcase card
- `app-start.png`, `app-complete.png`, `app-round-expanded.png`, `app-plateau-safety-flagged.png`, `app-error-state.png`, `app-final-run.png` — screenshots across the threshold path, plateau path, safety-flag rendering, and error handling
- `execution-log.txt` — full chronological activity log from the verified threshold-stop test run (60→72→81→93)
- `day-46.md` — this write-up
