# Day 45 of 60 — AI Decision Strategist

## What Was Built

A single-session Decision Report generated from a real decision I'm actually facing: **stay focused on Credit Risk domain depth, or go deep on Data Science within Credit Risk.** The interview followed the exact 4-question flow specified — one question at a time, no analysis until all answers were collected — then produced a complete interactive HTML decision dashboard.

**The 4 answers that shaped the report:**
1. **Decision:** Credit Risk vs. Credit Risk with Data Science in depth
2. **Goal/Timeline:** A stable job at a reputable firm; timeline open
3. **Gut + blocker:** Gut says stay in Credit Risk (already know it well); blocked by fear that AI could take over the field
4. **Biggest fear + reversibility:** Not landing an AI-heavy role due to competition, and uncertainty about whether I could return to Credit Risk if that bet failed

## What the Report Found

The most important move the report made wasn't picking a winner — it was **reframing the decision itself**. I'd framed this as "Credit Risk vs. AI," but my own stated facts (a Data Scientist role at Bajaj Finserv building XGBoost/BERT models, an MS in Business Analytics & AI, a current Credit Risk internship) show I'm not choosing between two unknowns — I'm deciding how much further to lean into a combination I've already started.

**Decision Matrix (7 dimensions, /70 each):**
| Dimension | Option A: Credit Risk Domain Depth | Option B: Data Science Depth Within Credit Risk |
|---|---|---|
| Life/Career Upside | 7 | 9 |
| Financial Safety | 8 | 6 |
| Growth & Learning | 5 | 9 |
| Stress Level | 8 | 5 |
| Reversibility | 6 | 8 |
| Long-term Alignment | 6 | 9 |
| Regret Risk | 5 | 8 |
| **Total** | **45/70** | **54/70** |

**Verdict:** Go Deep on Data Science Within Credit Risk — because the report treated my Bajaj Finserv results as evidence I'd already generated about myself, not a hypothesis to test.

**Assumption Buster caught something real:** my fear about "not being able to come back to Credit Risk" rests on a premise that isn't true — going deeper on DS *within* credit risk was never actually leaving the field. That single reframe did more work than any of the scoring.

## My Results

Verified the report's internal math programmatically rather than trusting the displayed numbers on sight:

| Check | Result |
|---|---|
| Sum of Option A's 7 individual bar scores | 45 — matches displayed total exactly |
| Sum of Option B's 7 individual bar scores | 54 — matches displayed total exactly |
| Bar animation renders correct value in each bar | Confirmed via DOM text content, not just visual width |
| Copy-to-clipboard on shareable cards | Working, confirmed state change |
| Mobile responsive layout (375px) | Cards stack correctly, no horizontal overflow |
| Console/page errors | 0 |

## Key Learnings

1. **The interview constraint (one question, short replies, no analysis until the end) forces real signal instead of premature reassurance.** Answering question by question without knowing what came next meant I couldn't shape my answers around a conclusion I wanted — by the time Q4 asked about reversibility, I'd already committed to the earlier framing in Q1-Q3, which is exactly what made the Assumption Buster's reframe land.
2. **A decision matrix is only honest if the scores are actually justified by specifics, not vibes.** Every score in the matrix ties back to something I said — Option A's higher "Financial Safety" score reflects the faster, more predictable path at a reputable firm; Option B's lower "Stress Level" score reflects the competition fear I named directly in Q4. Generic scores would have made the "winner" feel arbitrary.
3. **The most valuable output wasn't the verdict — it was the assumption I didn't know I was making.** I'd been treating "go deep on Data Science" and "leave Credit Risk" as the same thing. They aren't. Naming that explicitly changed what the decision actually was.
4. **A premortem for both options (not just the "losing" one) is what makes the matrix trustworthy.** Imagining Option B failing — spreading too thin, competing against pure SWE candidates for the wrong job postings — kept the report from reading like a sales pitch for its own verdict.
5. **The 7-day test plan turns a report into an actual next action.** A decision report that ends at "here's your score" is just a more elaborate opinion. Ending at "pull these job postings, run this small experiment, have this specific conversation, then decide" is what makes it usable Monday morning.
6. **Verifying the matrix math programmatically caught what a glance wouldn't.** With 14 individual bar-fill values feeding into 2 displayed totals, confirming the sums matched exactly (not just "looked about right") is the same discipline I'd want from any tool doing the arithmetic behind a decision I'm actually going to act on.

## Technical Notes

- Single self-contained HTML file, vanilla JS, built to the exact CSS variable palette, typography, and section-accent-color specification provided in the prompt.
- Decision matrix bars are JS-generated from a data array (not hardcoded per-row markup), with `animation-delay` staggered per row so bars fill in sequence on load, matching the spec's 0.8s ease-out / staggered-delay requirement.
- All copy in Sections 1–7 draws only from my four interview answers plus facts already present in my own profile (from Day 44's LinkedIn audit) — no invented numbers, roles, or outcomes.
- Verified with Playwright: full-page and mobile-viewport screenshots, a DOM-level check confirming the matrix bar text values sum to the displayed totals exactly, and confirmed clipboard-copy functionality on the shareable cards.

## Deliverables

- `main-app.html` — the complete Decision Report
- `app-full.png` — full desktop screenshot
- `app-mobile.png` — mobile responsive screenshot
- `day-45.md` — this write-up
- `day45-card.png` — Cinematic card for day-45
