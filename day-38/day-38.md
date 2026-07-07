# Day 38 of 60 — Typing Speed Studio (Programming Edition)

## What Was Built

A premium, single-file, fully offline typing platform built specifically around **programming practice**. Instead of a generic typing test, it renders as a real code editor — tab bar, line-number gutter, live status bar — and drops the user into realistic code snippets across seven languages: JavaScript, Python, Java, C++, SQL, HTML, and CSS.

Category chosen: **Programming**, with feature selection set to **Auto-decide**, so the build includes the full premium spec from the prompt template: every typing mode, the complete post-session analytics dashboard, gamification, and accessibility/customization controls.

## App Features

**Typing modes**
- **Time** (15 / 30 / 60 / 120s) — endless dev-themed sentence stream, auto-extends as you type
- **Words** (25 / 50 / 100 / 250) — fixed-length word-count sprint
- **Quote** — original programming aphorisms, untimed
- **Programming** — real, hand-written code snippets per language (functions, classes, decorators, SQL queries, etc.)
- **Custom Text** — paste your own passage
- **Adaptive** — auto-raises or lowers difficulty (plain text → single snippet → mixed multi-language snippet) based on rolling WPM + accuracy
- **Focus Mode** — dims everything except the current line
- **Zen Mode** — hides the stats strip and progress bar for distraction-free untimed practice

**Live stats** — WPM, Raw WPM, CPM, Accuracy, Elapsed Time, Mistake Count, Current Streak (with best streak), Completion %, and remaining time/words, all updating every 100ms.

**Post-session analytics dashboard**
- Hero card: WPM, Accuracy, Raw WPM, Consistency, Duration, estimated percentile
- Dual-line WPM + Accuracy chart sampled once per second, rendered on `<canvas>`
- Character breakdown (Correct / Incorrect / Extra / Missed)
- QWERTY key-error heatmap showing exactly which keys were mistyped most
- Auto-generated performance summary (strengths, weaknesses, most-mistyped keys, a concrete next-practice suggestion)
- 8 achievement badges (Century Club, Sharpshooter, Metronome, Polyglot, etc.) persisted across sessions
- Personal bests per mode/language, and a 50-session history table

**Everything else in the spec** — sound effects (Web Audio beeps for correct/incorrect/finish), keyboard shortcuts (`Esc` restart, `Tab` pause/resume), pause/resume, restart, 4 accent themes + light/dark toggle, font-size controls, responsive layout, `prefers-reduced-motion` support, and full `localStorage` persistence for history/bests/badges (safe here since this is a standalone HTML file, not a Claude.ai artifact).

## My Results / Scores

Test run (Programming mode, JavaScript, `debounce` snippet):

| Metric | Result |
|---|---|
| WPM | 92 |
| Raw WPM | 96 |
| Accuracy | 97% |
| Consistency | 91% |
| Estimated percentile | Top ~5% |
| Badges earned | Speedster 60+, Sharpshooter 95+ |

## Key Learnings

1. **Character-level state beats string-diffing.** Modeling the passage as an array of `{ch, status}` objects — rather than diffing two strings on every keystroke — made backspace, extra characters, and the focus-mode line slicing trivial to implement correctly.
2. **A hidden `<input>` is still the most reliable typing-capture pattern.** Capturing `keydown` on a focused, invisible input (instead of listening on the display div directly) sidesteps IME/mobile-autocomplete weirdness while keeping the visible text purely presentational.
3. **Sanity-clamping matters more than the formula.** The brief explicitly called out avoiding "20,000 WPM" results — the fix wasn't a smarter formula, it was a hard ceiling (`clampNum`) plus computing WPM from a minimum elapsed-time floor so a two-keystroke burst can't produce an absurd instantaneous rate.
4. **Consistency is just normalized standard deviation.** Sampling WPM once per second and computing `100 - (stddev/mean)*100` turned out to be a simple, honest way to reward steady typists over "burst and stall" typists, and it made the WPM/Accuracy chart genuinely informative instead of decorative.
5. **Adaptive difficulty needs hysteresis, not a single threshold.** Raising the level only above ~55 WPM / 92% accuracy and lowering it below ~25 WPM / 80% accuracy (rather than one shared cutoff) stopped the mode from flapping between levels every other session.
6. **Programming-mode content is the hardest part to make feel real.** Generic "lorem ipsum" text is trivial; realistic, syntactically correct code snippets across 7 languages that also read naturally as typing practice required writing each one by hand rather than templating them.

## Technical Notes

- Single self-contained HTML file, vanilla JS, zero dependencies, zero network calls required at runtime (Google Fonts is a progressive enhancement only — the type stack has solid system-font fallbacks).
- Rendering: DOM spans per character for the editor (correct/incorrect/extra/cursor states via CSS classes), Canvas 2D for the WPM/Accuracy chart, CSS Grid for the QWERTY heatmap.
- Persistence: `localStorage` for session history (last 50), personal bests per mode/language, and earned achievement badges — this is a standalone file, so localStorage is safe and appropriate here (unlike inside a Claude.ai artifact).
- Verified with Playwright (system Chrome at `/opt/google/chrome/chrome`) — simulated a full typing session end-to-end with zero console/page errors before shipping.

## Deliverables

- `main-app.html` — the complete Typing Speed Studio application
- `day38-card.png` — cinematic showcase card
- `day-38.md` — this write-up
