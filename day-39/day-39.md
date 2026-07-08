# Day 39 of 60 — PDF Splitter & Merger

## What Was Built

A premium, single-file, browser-based PDF utility with two tools: a **Splitter** and a **Merger**, both processing documents entirely client-side. No file is ever uploaded anywhere — everything happens inside the browser tab using WebAssembly-free, pure-JS PDF libraries (`pdf-lib` for reading/writing PDFs, `pdf.js` for rendering real page thumbnails).

Feature selection: **Auto-decide**, so the build includes the full premium spec from the prompt template.

## App Features

**PDF Splitter**
- Drag-and-drop or click-to-browse upload, with page count and file size detected automatically
- Real rendered page thumbnails for every page (not placeholders), progressively rendered in batches for performance
- Four split methods:
  - **Custom Ranges** — comma-separated ranges (`1-3, 5, 7-9`), each becoming its own output file
  - **Split After Pages** — enter page numbers to split after (e.g. "3, 7" on a 10-page doc → three files)
  - **Every N Pages** — equal-sized chunks, last chunk shorter if needed
  - **Extract Selected** — click thumbnails to select pages, then choose one combined PDF or one PDF per page
- Live validation with per-range error messages (out-of-range, malformed input) that disable the split button until fixed
- A structure preview listing every output file and its page range before anything is generated
- Individual download links per output file after processing

**PDF Merger**
- Multi-file drag-and-drop or file picker
- Each file shows a real first-page thumbnail, name, page count, and size
- Native HTML5 drag-and-drop reordering by a dedicated handle
- Live summary: total files, total pages, estimated output size
- One-click merge with a single downloadable `merged.pdf`

**Shared** — dark mode, keyboard shortcuts (`S`/`M` to switch tools, `Ctrl/Cmd+Enter` to run), processing spinners, friendly error handling for corrupted/password-protected PDFs, fully responsive layout, accessible focus states.

## My Results / Scores

Verified end-to-end with a 10-page and a 4-page test PDF:

| Test | Result |
|---|---|
| Split "1-3, 4-6, 7-10" on 10-page doc | 3 output files, 3/3/4 pages — verified correct |
| Split "every 4 pages" on 10-page doc | 3 output files, 4/4/2 pages |
| Extract 3 selected pages | 1 combined 3-page PDF |
| Merge 10-page + 4-page docs | 1 output file, 14 pages — verified correct |
| Console/page errors during full test run | 0 |

## Key Learnings

1. **"Self-contained" and "offline" are different claims, and the spec asked for both.** Loading `pdf-lib` and `pdf.js` from a CDN would have made the file small but silently broken the "works offline" requirement the moment there's no internet. Inlining both libraries' minified source directly into `<script>` tags — and the pdf.js worker as a base64-encoded Blob URL — is what makes offline actually true rather than aspirational.
2. **pdf.js needs its worker even when everything is local.** Without setting `GlobalWorkerOptions.workerSrc`, page rendering silently fails. Converting the worker script to base64, decoding it into a `Blob`, and pointing `workerSrc` at `URL.createObjectURL(blob)` keeps the worker fully local with no separate file to manage.
3. **Validation has to happen before generation, not during.** Building the "preview output structure" list first — computing every output file's page range and flagging invalid ones — meant the split button could simply be disabled until every range was valid, instead of failing midway through generating files.
4. **"Split after pages" is a different data shape than "custom ranges."** It was tempting to reuse the same range-parsing function for both, but split-after points describe boundaries, not ranges, and forcing them through the same parser produced off-by-one errors until I gave it its own conversion function.
5. **Rendering 50+ thumbnails at once will visibly stutter.** Batching thumbnail rendering (6 pages at a time via `Promise.all`, sequential batches) kept the UI responsive on longer documents instead of blocking the main thread with dozens of simultaneous canvas renders.
6. **Drag-and-drop reordering needs a DOM-to-state sync step.** Native HTML5 drag events move DOM elements directly; the app state (`MG` array) only matches reality after reading the final DOM order back out on `dragend` — skipping that step causes merges to silently use the pre-drag order.

## Technical Notes

- Single self-contained HTML file (~2.4MB) — no external requests at runtime; `pdf-lib.min.js` and `pdf.js` (legacy/UMD build) are inlined, and the pdf.js worker is embedded as base64 and instantiated via Blob URL.
- All PDF byte manipulation uses `PDFDocument.load` / `copyPages` / `save` from pdf-lib; all visual thumbnails use `pdf.js`'s canvas renderer.
- Verified with Playwright (system Chrome) across both tools: thumbnail rendering, all four split methods, drag-reorder, merge, dark mode, and actual file downloads — confirmed the downloaded PDFs have the correct page counts (3 pages for a split part, 14 pages for a 10+4 merge).
- Google Fonts (`Fraunces`, `Inter`, `JetBrains Mono`) are loaded as a progressive enhancement only; the type stack has solid system-font fallbacks so the UI still looks correct fully offline.

## Deliverables

- `main-app.html` — the complete PDF Splitter & Merger application
- `day39-card.png` — cinematic showcase card
- `app-welcome.png`, `app-split-thumbnails.png`, `app-split-preview.png`, `app-split-results.png`, `app-split-every-n.png`, `app-split-extract.png`, `app-merge-list.png`, `app-merge-results.png`, `app-dark-mode.png` — feature screenshots
- `processed-split-part1.pdf`, `processed-merged.pdf` — real processed output files from a test run
- `day-39.md` — this write-up
