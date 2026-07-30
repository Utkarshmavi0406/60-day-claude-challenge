# RiskLens — Daily Build Prompt (Reusable for the 30-Day Growth Plan)

Paste this into a fresh Claude conversation each day, replacing only [DAY NUMBER]. Everything else stays identical for the full 30 days.

---

Today is Day [DAY NUMBER] of the RiskLens 30-Day Growth Plan, continuing from 30-day-growth-plan.md in the project repo.

Before doing anything: read 30-day-growth-plan.md and find the entry for Day [DAY NUMBER]. Also read README.md, docs/PROJECT-STRUCTURE.md, and docs/ARCHITECTURE.md for current project state. Treat all of these as the source of truth, do not redesign the project or jump ahead to a later day's milestone.

Rules for today:
1. Build only what Day [DAY NUMBER]'s milestone in 30-day-growth-plan.md describes, nothing more, nothing from a different day.
2. Assume zero technical experience unless told otherwise. Any manual step (installing something, configuring a service, running a command, deploying) gets exact, numbered instructions with real button/menu names, then wait for confirmation before continuing.
3. Generate complete, final file contents, never snippets, placeholders, or "add this below" instructions.
4. State clearly where each file belongs and whether it's new or replaces an existing one.
5. Before considering anything done, actually test it, run the code, hit the real endpoint, check the real output, and show the real result. Do not claim something works without demonstrating it.
6. If something breaks, debug it completely before moving on. Never build on top of broken code.
7. If today's milestone reveals a real bug, gap, or surprising finding in the existing codebase (not just today's new work), investigate and document it honestly, don't paper over it to keep moving.
8. Do not silently expand scope. If today's milestone turns out to need something not in 30-day-growth-plan.md, say so explicitly and ask before proceeding.

When today's milestone is complete:
- Summarize exactly what was built and verified.
- Update any documentation the change affects (README, docs/, etc.).
- Give me the exact git commands to commit and push today's work with a clear, specific commit message (not "update files").
- State what tomorrow's milestone (Day [DAY NUMBER + 1]) will be, based on 30-day-growth-plan.md.

Do not start tomorrow's work today.
