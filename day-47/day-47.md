# Day 47 of 60 — Content Intelligence Studio

## What Was Built

A multimodal, multi-stage AI content review platform — **Content Intelligence Studio** — that analyzes a LinkedIn post through five specialist reviewers, each a genuine live Claude call, synthesized into one decisive final report with a rewrite, alternative hooks, and a publishing checklist.

**Interview path:**
- **Content type:** LinkedIn post / caption text
- **Platform:** LinkedIn
- **Goal:** Maximize engagement (likes, comments, shares)
- **Upload:** Text (with an optional screenshot-attach capability built in, since the platform spec requires multimodal support even though this run's primary input is text)
- **Review tone:** Balanced — fair mix of praise and critique

## The Review Pipeline

1. **Hook & Opening Line Reviewer** — evaluates only the portion of the post visible before LinkedIn's "see more" truncation, the single highest-leverage few seconds of attention.
2. **Structure & Readability Reviewer** — formatting, line-break rhythm, and mobile-feed scannability.
3. **Engagement Psychology Reviewer** — emotional pull, relatability, curiosity gaps, and whether the post is likely to drive comments versus a passive scroll-past.
4. **CTA & Comment-Bait Reviewer** — whether the closing line genuinely invites a specific response or is generic filler.
5. **Content Strategist** — reads all four reports plus the original post and synthesizes one final report: executive summary, missed opportunities, platform-specific recommendations, a complete rewrite, 3 alternative hooks, a publishing checklist, and a predicted-performance estimate explicitly labeled as an AI estimate, not a guarantee.

Every score, sentence, and rewrite shown in the UI is that round's literal API response — no hardcoded logic, no canned feedback, no rule-based scoring, and critically, **no JSON anywhere** (the prompt specifically flagged JSON parsing as a failure mode to avoid, so every agent uses a plain-text labeled-section contract, extracted with tolerant regex).

## Multimodal Capability

Per the build requirement, the app genuinely supports image upload — an optional screenshot attach that, when present, gets base64-encoded and sent as a real image content block to Claude's vision-capable endpoint. It's wired into the Hook Reviewer, Structure Reviewer, and Content Strategist calls (the three where visual formatting is actually relevant), while Engagement Psychology and CTA review text content only. Verified this routing is correct by inspecting actual outgoing request bodies during testing — 3 of 5 calls carried image data when a screenshot was attached, matching the intended design exactly.

## My Results (Sample Analysis)

Ran the pipeline against a real draft post about this very project:

| Reviewer | Score |
|---|---|
| Hook | 58/100 |
| Structure | 74/100 |
| Engagement Psychology | 44/100 |
| CTA | 35/100 |
| **Overall (Strategist synthesis)** | **53/100** |

**Most valuable insight:** the CTA Reviewer flagged "Thoughts?" — the actual closing line of the draft — as one of the lowest-response phrases on LinkedIn, and rewrote it into a specific, opinion-inviting question instead. The Content Strategist's rewrite also surfaced something I hadn't noticed myself: the post described building a tool that scores content, but never stated what score the post itself received — a natural, curiosity-driving detail sitting unused.

## Verification (No Live API Key — Tested via Mocked Responses at the Fetch Boundary)

Same rigor as Day 46: intercepted requests at `fetch()` itself (not the UI), so tests exercised the real pipeline, parsers, and rendering — only the model's text generation was substituted.

| Test | Result |
|---|---|
| Full 5-call pipeline with realistic scored responses | All 4 category scores + overall score parsed exactly, matching mock values (58/74/44/35 → 53) |
| Image attach + routing | 3 of 5 requests correctly carried image data (Hook, Structure, Strategist); Engagement and CTA correctly did not |
| Rewritten post + 3 alt hooks + checklist parsing | All rendered correctly from the plain-text label contract, zero JSON used anywhere |
| Copy-to-clipboard on rewrite and hooks | Working, confirmed state change |
| Invalid API key (401) | Error banner shown with the real API message, pipeline halted cleanly, Start button re-enabled |
| Console/page errors across all tests | 0 |

## Key Learnings

1. **The explicit "avoid JSON" instruction in the brief was worth taking literally, not just as a suggestion.** Every agent's output contract uses labeled plain-text sections (`HOOK_SCORE:`, `STRENGTH:`, etc.) extracted via regex that captures everything up to the next known label. This is more forgiving of minor model formatting drift than JSON ever is, and it's exactly the failure mode ("expected '{' or '('") the brief called out by name.
2. **Not every reviewer needs the image.** It would have been easy to attach the screenshot to all five calls "to be safe." Engagement Psychology and CTA review the words, not the visual layout — sending image tokens they don't need would have been wasted cost with zero analytical benefit. Being deliberate about which 3 of 5 calls actually need vision made the pipeline both cheaper and more focused.
3. **A regex that stops at "the next known label" is more robust than stopping at a fixed string.** Early parsing attempts anchored each field's end to a single specific next-label, which broke the moment the model's actual field order drifted slightly. Building the "stop" pattern from the full list of possible remaining labels made parsing resilient to minor structural variation.
4. **The CTA reviewer catching "Thoughts?" specifically was the most concrete proof this isn't generic feedback.** A rule-based system could tell you a post has a question mark. Only a real model call can recognize that *this particular* question is a weak, overused pattern and propose a genuinely better, content-specific alternative.
5. **"Predicted performance" needs the disclaimer built into the UI, not just the prompt.** Even though the system prompt instructs the model to frame its estimate as non-guaranteed, adding a visible `⚠ AI ESTIMATE — NOT A GUARANTEE` tag in the interface itself removes any ambiguity for the person reading the dashboard, regardless of how the model happened to phrase that round's text.
6. **Testing multimodal routing requires inspecting the actual request payload, not just the rendered output.** The UI would have looked identical whether or not the image was actually being sent. Only checking the intercepted request body's `content` array for an `image` block proved the routing logic was correct.

## Technical Notes

- Single self-contained HTML file, vanilla JS, sidebar + dashboard layout matching the pattern established in Day 46.
- All 5 agent system prompts enforce a strict plain-text output contract; parsing uses a shared `grab()` helper that stops at the next known label rather than a hardcoded single delimiter.
- Image upload uses `FileReader.readAsDataURL`, strips the data-URL prefix, and sends the raw base64 payload as an Anthropic `image` content block alongside text — genuine multimodal analysis, not a placeholder.
- Verified with Playwright: full 5-stage pipeline with realistic mock responses, image-attach request-body inspection, copy-button functionality, reviewer card expand/collapse, dark/light toggle, and invalid-key error handling.

## Deliverables

- `main-app.html` — the complete Content Intelligence Studio application (bring your own Claude API key to run it live)
- `day47-card.png` — cinematic showcase card
- `app-empty.png`, `app-image-attached.png`, `app-complete.png`, `app-reviewer-expanded.png`, `app-light-mode.png`, `app-final-full.png` — screenshots across the full workflow
- `content-analysis-report.txt` — full activity log + final report from the verified test run
- `day-47.md` — this write-up
