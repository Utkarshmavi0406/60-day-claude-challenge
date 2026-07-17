# Day 48 of 60 — The Verdict Engine

## What Was Built

A decision-support application — **The Verdict Engine** — comparing three real cloud machine learning certifications (AWS, Azure, GCP) across four criteria, with every data point traced to a named, citable source. No live AI calls at runtime; the research was done upfront via web search, and the app itself is a fast, fully client-side live-weighting engine.

**Interview path:**
- **Comparing:** Cloud certifications (AWS vs Azure vs GCP for data/ML)
- **For:** A data science/credit risk student choosing one cert to boost job prospects (my exact situation)
- **Criteria:** Exam Cost, Job Market Demand, Prep Time, Relevance to Credit Risk/Finance roles
- **Data source:** Researched and cited by Claude, using only named, real sources
- **Weighting:** Adjustable — live sliders, ranking updates instantly

## The Three Certifications Compared

- **AWS Certified Machine Learning Engineer – Associate (MLA-C01)** — $150, 3-year validity
- **Microsoft Certified: Azure Data Scientist Associate (DP-100)** — $165, 1-year validity (annual renewal)
- **Google Cloud Professional Machine Learning Engineer (PMLE)** — $200, 2-year validity

## Most Surprising Finding

Researching AWS's own official certification page turned up something I wasn't looking for: **MLA-C01 is being retired.** Registration for its replacement, MLA-C02, opens September 1, 2026 — and the last day to sit the current exam in English is September 28, 2026. That's a real, time-sensitive fact that would matter enormously to anyone actually planning to sit this exam soon, and it only surfaced because the research went to the primary source rather than stopping at third-party summaries.

The second most useful finding: **Azure's certification only stays valid for 1 year**, versus 3 for AWS and 2 for GCP. That wasn't one of the four criteria I asked to weight, but it's a real, materially-relevant cost-of-ownership difference the sticker price alone doesn't show — so it's surfaced as supplementary context in the comparison table rather than hidden.

## How the Live Weighting Works

Four sliders (0-10 each) let the user weight Cost, Job Market Demand, Prep Time, and Finance Relevance by personal priority. Each certification's raw sourced data is normalized into a 0-100 per-criterion score (e.g., cost is inverted so cheaper scores higher, market share is scaled against the highest value in the set), then combined into a single weighted average that re-sorts the ranking live as sliders move — with the winning card visually highlighted.

## My Results — Verified Weighting Logic

Rather than trust the UI on sight, I tested each criterion in isolation by zeroing out the other three weights and confirming the winner matched what the underlying sourced data predicts:

| Test | Predicted Winner (from raw data) | Actual App Result |
|---|---|---|
| Cost weight = 10, others = 0 | AWS ($150, cheapest) | ✅ AWS |
| Job Market Demand weight = 10, others = 0 | AWS (~32% market share, largest) | ✅ AWS |
| Prep Time weight = 10, others = 0 | AWS (~5 weeks, fastest structured plan) | ✅ AWS |
| Finance Relevance weight = 10, others = 0 | Azure (explicitly sourced as finance-strongest) | ✅ Azure |
| Equal weights (default) | — | AWS 91, Azure 58, GCP 29 |

All four isolated tests matched the sourced data exactly, confirming the weighting math is correct — not just visually plausible.

## Key Learnings

1. **"Research and cite real sources" is a much stronger constraint than it sounds, and it changes what you can claim.** I could not find a single clean, sourced "job postings requiring this certification" count for any of the three providers — so rather than approximate one, I used overall cloud market share as a disclosed proxy, explicitly labeled as a substitution rather than presented as a direct citation.
2. **Distinguishing SOURCED from AI-INTERPRETED data has to be a first-class UI element, not a footnote.** The Finance Relevance score is fundamentally different in kind from the other three criteria — it's built from qualitative statements, not a single number. Tagging it differently in the comparison table (and explaining why in the research panel) was necessary to keep the tool honest about its own limits.
3. **Real sources disagree, and the disagreement itself is useful information.** AWS prep time ranged from 2 weeks to 6 months across sources depending entirely on the candidate's starting point. Picking one number and hiding the range would have been a quieter but real form of fabrication — disclosing the full range in the research panel was the more honest choice.
4. **A "did you know" fact outside the requested criteria can still belong in the app.** Validity period wasn't one of the four weighted criteria, but Azure's 1-year renewal cycle is a genuinely material difference. Surfacing it as unweighted supplementary context (rather than either omitting it or forcing it into the weighted score the user didn't ask for) respected both the interview answer and the user's actual interest.
5. **Testing a weighted-ranking tool means testing the math, not the UI.** Screenshots alone can't distinguish "the ranking looks reasonable" from "the ranking is actually computed correctly." Isolating each criterion to 100% weight and checking the winner against the raw sourced data directly was the only way to confirm the scoring logic — and it caught nothing wrong here, but it's the check that would have caught a bug if one existed.
6. **A single escaped-apostrophe bug almost shipped again.** A JS string containing `Azure's` was written with a doubled backslash escape, which would have silently broken every script on the page. Running a syntax check via `new Function()` on the extracted script — before ever opening the file in a browser — caught it immediately, the same discipline that's now standard after Day 42's version of this exact mistake.

## Technical Notes

- Single self-contained HTML file, vanilla JS. No API calls at runtime — this is a research-then-build tool, not a live-inference tool, matching the task's actual shape (grounded static facts + live client-side math, not live model reasoning).
- Every "SOURCED" data point traces to a specific named source shown in the Sources Panel; the one "AI-INTERPRETED" data point (Finance Relevance) is visually distinguished with a different tag color throughout.
- Weighted scoring is a simple, disclosed formula: normalize each criterion 0-100 against the range present in the dataset, then compute a weight-proportional average — explained in plain language in the collapsible "How this was researched" panel.
- Verified with Playwright: isolated single-criterion weight tests (4 total) all matched sourced-data predictions exactly, source panel and provenance-flag counts confirmed, dark mode and collapsible research panel both functional, zero console/page errors.

## Deliverables

- `main-app.html` — the complete Verdict Engine application
- `day48-card.png` — cinematic showcase card
- `sourced-data-report.md` — full raw research findings with every citation
- `app-default.png`, `app-cost-only.png`, `app-finance-only.png`, `app-research-panel.png`, `app-dark-mode.png` — screenshots across weighting scenarios
- `day-48.md` — this write-up
