# Day 37 — Task Compass: Learn How Work Flows Through Real Organizations

## Challenge
**Build Task Compass** — A management simulation that teaches ownership, delegation, workflow, and collaboration through interactive gameplay — not theory. Three stages, drag-and-drop, Organizational Thinking Dashboard at the end.

*Workplace: Tech Company*

---

## What Was Built

A complete **Management Simulation Game** — single HTML file, pure vanilla JavaScript and CSS. Three stages with drag-and-drop mechanics, reveal explanations after each question, and a personalized Organizational Thinking Dashboard with four scored dimensions.

**File:** `task-compass.html`

---

## Three Stages

### Stage 1: Who Owns This? (3 Questions)

A work ticket appears. Player drags one role card from the palette into the "Primary Owner" slot.

**Tickets:**
1. **Payments Fail on iPhone** (HIGH) → Primary: Frontend Dev — WebKit compatibility issue
2. **Database at 95% Capacity** (CRITICAL) → Primary: DevOps Engineer — infrastructure capacity
3. **Cart Abandonment Up 40%** (HIGH) → Primary: UX Designer — confusing user flow

After submission, a reveal overlay explains:
- Who the primary owner is and exactly why
- Which roles assist and what each contributes
- No "correct/incorrect" labels — always educational reasoning

### Stage 2: Task Routing (3 Questions)

A workflow task appears. Player builds the chain by dragging roles into 5 sequential slots.

**Workflows:**
1. **Production Bug Reported** → Support → QA → Backend → Eng Mgr → Support
2. **Enterprise Feature Launch** → PM → UX Designer → Frontend → QA → Eng Mgr
3. **Compliance Data Export** → Eng Mgr → Backend → Data Analyst → QA

After submission, the optimal workflow is displayed with a step-by-step explanation of why this sequence is most effective.

The core workflow pattern taught: triage → define → build → validate → close — consistent across nearly every organizational task.

### Stage 3: Collaboration Challenge (3 Questions)

A complex situation card appears. Player assigns a Lead Team (primary) + up to 3 Supporting Teams.

**Situations:**
1. **NPS Drops 15% in One Quarter** → Lead: PM, Supporting: Support/Analyst/Eng Mgr
2. **Competitor Launches at Half Price** → Lead: PM, Supporting: Marketing/Eng Mgr/Analyst
3. **App Load Time Triples After Deploy** → Lead: Eng Mgr, Supporting: DevOps/Backend/QA

After submission, reveals: lead team reasoning, communication flow between departments, and the key insight that complex problems require coordinated teams — not individual heroes.

---

## Role Cards (10 Roles)

| Role | Icon | Color | Responsibility |
|------|------|-------|---------------|
| Frontend Dev | 💻 | Blue | Client-side UI, browser rendering, platform compatibility |
| Backend Dev | 🔧 | Green | Server logic, APIs, databases, performance |
| QA Engineer | 🧪 | Amber | Testing, bug validation, release quality |
| Product Manager | 📋 | Purple | Strategy, prioritization, roadmap |
| UX Designer | 🎨 | Pink | User experience, interface design, user research |
| Customer Support | 🎧 | Cyan | Communication, triage, customer satisfaction |
| Engineering Manager | 👔 | Red | Team leadership, delivery, escalations |
| Data Analyst | 📊 | Teal | Insights, metrics, patterns |
| DevOps Engineer | ⚙️ | Orange | Infrastructure, deployments, reliability |
| Marketing Manager | 📣 | Yellow | Brand, campaigns, positioning |

---

## Scoring System

| Dimension | What It Measures | How Scored |
|-----------|-----------------|------------|
| **Ownership Clarity** | Did you identify correct primary owners? | Stage 1: +25 for correct, +8 for any engagement |
| **Delegation Thinking** | Did you build workflows with the right roles? | Stage 2+3: based on role match quality |
| **Collaboration Breadth** | Did you assign appropriate supporting teams? | Stage 3: +10-25 per question |
| **Workflow Understanding** | Did you sequence steps correctly? | Stage 2: position-match scoring |

---

## Organizational Thinking Dashboard

Four animated bar chart scores (0-100%) with personalized:
- "Where You Showed Strength" — identifies highest-scoring dimension
- "Where to Explore Further" — identifies lowest-scoring dimension
- "One Insight About How Organizations Actually Work" — contextual to overall performance

---

## My Results

**Overall: 79% — Strong Thinker**

- Ownership Clarity: 82%
- Delegation Thinking: 76%
- Collaboration Breadth: 88%
- Workflow Understanding: 71%

**Strength:** Collaboration — I intuitively reached for cross-team solutions for complex situations

**Growth area:** Workflow sequencing — the order of steps matters as much as which steps to include

---

## Key Learnings

### 1. Ownership Clarity Accelerates Everything
The most consistent pattern across all 9 questions: when one person or team clearly owns a problem, every subsequent step moves faster. The moment ownership is ambiguous, everyone waits for someone else to move first. This is why the payment bug goes to Frontend Dev (not "the engineering team") — specificity of ownership is the mechanism, not just a detail.

### 2. The Workflow Pattern Is Astonishingly Consistent
The same sequence appears across completely different task types: triage (who discovers the problem and routes it) → define (who understands what it actually is) → build (who fixes or creates) → validate (who confirms it works) → close (who communicates completion). The roles change every time. The logic doesn't. Understanding this pattern is more durable than memorizing which team handles what.

### 3. The "Who Escalates To Whom" Problem Is Underappreciated
Stage 2 taught this: workflows don't just sequence horizontally — they often return to the person who received the problem at the end (Support → QA → Backend → Eng Mgr → Support again). The escalation and closure loops are what make workflows circular rather than linear, and this is where most handoff failures happen in real organizations.

### 4. Complex Problems Almost Always Need More People Than You Expect
When NPS drops 15%, first instinct might be "customer support problem." But the reveal shows you need PM (coordinates), Analyst (quantifies), Engineering Manager (implements), and Support (gathers data). None of them alone can solve it. Building a mental model for "what kind of problem is this?" → "who does that require?" is a genuinely useful organizational skill.

### 5. The Lead Team Defines the Framing, Not Just the Action
In Stage 3, the choice of who leads matters because it determines how the problem gets framed for everyone else. When the app load time triples after a deploy, naming Engineering Manager as lead (not DevOps) signals that this is a coordinated incident response — not just a technical investigation. Leadership of a situation shapes how all other roles understand their contribution.

---

## Technical Notes
- Vanilla HTML/CSS/JavaScript — zero dependencies
- Dynamic rendering: all screens injected into one `#main-area` element
- HTML5 Drag and Drop API + custom touch event support (touchstart/move/end)
- Role card state management: placed roles tracked in `G.placedRoles` object
- Slot management: placing a new role returns the previous occupant to palette
- CSS glassmorphism: `rgba(255,255,255,0.05)` + `rgba` borders for dark glass effect
- Score bars animate via CSS transitions triggered 300ms after dashboard renders

---

## Deliverables
- `task-compass.html` — Complete interactive management simulation
- `detective-card.png` — Cinematic Day 37 card (purple/blue tech theme)
- `app-welcome.png` — App welcome screen screenshot
- `day-37.md` — This file

---

*Day 37 of 60 · Built with Claude AI · #60DaysOfAI*
