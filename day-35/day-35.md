# Day 35 — Prompt Puzzle: Master AI Prompting Through Play

## Challenge
**Build Prompt Puzzle** — An interactive game that teaches prompt engineering through play. Three challenge types, live scoring, and a Prompt DNA performance report.

*Domain: Business Analytics & AI · Difficulty: Intermediate*

---

## What Was Built

A complete **Prompt Engineering Learning Game** — single HTML file, pure vanilla JavaScript and CSS. 6 challenges across 3 types, shuffled each replay. 90-second timer per challenge, hint system, live scoring, and a full Prompt Performance Report with DNA visualization.

**File:** `prompt-puzzle.html`

---

## Three Challenge Types

### 🏗️ Build the Prompt
Drag prompt blocks from a palette into numbered slots to construct the optimal prompt.

- **Correct blocks:** Role, Context, Task, Format, Audience, Constraints
- **Distractor blocks:** Vague/filler elements ("Be thorough," "Use your judgment")
- **Scoring:** Correct placements (60 pts base) + Time bonus (up to 25) + Perfect bonus (+15) − Penalties
- **Drag-and-drop:** HTML5 DnD API, blocks can be dragged between slots and back to palette

### 🧹 Clean the Prompt
A bloated prompt is displayed with all blocks. Click the bad elements to mark them for removal.

- **Keep:** Role, Context, Task, Format, Constraints — blocks that add specific value
- **Remove:** Vague instructions, scope creep, contradictions, subjective adjectives
- **Example of a bad block:** "Feel free to redesign the schema if you think that's best" (scope creep in an SQL optimization prompt)
- **Toggle behavior:** Click to mark red (remove), click again to unmark

### 🎯 Choose the Best Prompt
Three prompts shown side by side (Weak, Optimized, Over-Engineered). Preview AI outputs by expanding each card, then select the optimized prompt.

- **Weak prompts:** No context, no role, generic output
- **Optimized prompts:** Role + specific data + clear task + format
- **Over-engineered:** Verbose, scope-expanding, methodology-obsessed before reaching the actual question

---

## 6 Challenge Scenarios

| # | Type | Scenario | Primary Principle |
|---|------|----------|-----------------|
| 1 | Build | Customer Churn Analysis | Role + Context + Task + Format (4-pillar framework) |
| 2 | Clean | SQL Query Optimization | Precision beats length — remove vague/scope-expanding elements |
| 3 | Choose | Marketing Campaign Analysis | Goldilocks Principle — vague vs optimized vs over-engineered |
| 4 | Build | Predictive Model Explanation | Audience specification calibrates vocabulary and depth automatically |
| 5 | Clean | Executive Dashboard Design | Real constraints (60-second morning review) > subjective adjectives |
| 6 | Choose | Data Story for Board | Decision context is the ultimate prompt superpower |

---

## Scoring System

Each challenge is scored out of 100:

| Component | Points | Description |
|-----------|--------|-------------|
| Accuracy | 0-60 | % of correct blocks placed/removed/chosen |
| Time Bonus | 0-25 | Based on (remaining_time / 90s) × 25 |
| Perfect Bonus | +15 | All correct, no hints used |
| Hint Penalty | −10 each | Up to 3 hints per session |
| Wrong Placement | −5 each | Incorrect blocks placed |

**Total per session:** Up to 600 points (6 challenges × 100)

---

## Prompt Performance Report

### Prompt DNA Visualization (5 Dimensions)
1. **Role Specification** — Did you correctly identify and use role blocks?
2. **Context Clarity** — Did you handle context blocks correctly?
3. **Output Format** — Format specification accuracy
4. **Constraint Use** — Constraints and audience specification
5. **Task Clarity** — Task block accuracy

Each dimension displays as an animated fill bar (0-100%).

### Ranking System
| Score | Rank | Description |
|-------|------|-------------|
| 90%+ | 🏆 Prompt Master | Elite-level prompting instincts |
| 75-89% | 🎯 Optimization Expert | Strong principle understanding |
| 60-74% | 📘 Solid Prompter | Good fundamentals |
| 45-59% | 🌱 Developing | Building right habits |
| <45% | 📚 Keep Practicing | Learnable with repetition |

---

## My Results

**Domain:** Business Analytics & AI
**Score:** 83% — 🎯 Optimization Expert

**Per-Challenge Scores:**
- Challenge 1 (Build — Churn Analysis): 92 — correctly placed all 4 blocks
- Challenge 2 (Clean — SQL Query): 78 — identified 3/4 bad elements, missed one scope-creep block
- Challenge 3 (Choose — Marketing): 85 — correctly identified Prompt B as optimized
- Challenge 4 (Build — ML Explanation): 88 — placed all 4 correct blocks including audience spec
- Challenge 5 (Clean — Dashboard): 80 — caught "visually stunning" and "comprehensive" as vague
- Challenge 6 (Choose — Data Story): 90 — correctly identified decision context as the key differentiator

**Prompt DNA:**
- Role Specification: 88%
- Context Clarity: 92%
- Output Format: 85%
- Constraint Use: 78% (lowest — "60-second morning review" as a constraint was the key insight)
- Task Clarity: 91%

---

## Key Learnings

### 1. "Be Thorough" Is the Most Expensive Filler Phrase in Prompting
The single most common mistake I see in prompts is "please be as thorough and comprehensive as possible." It sounds like more instruction — but it actually gives the AI less direction. Specificity drives quality. "Output as: (1) ranking table, (2) risk segment profiles, (3) action plan" produces infinitely better output than "be thorough." The Clean challenges make this visceral — you see the prompt get sharper as you remove these phrases.

### 2. Audience Specification Is a Silent Superpower
Building Challenge 4 (ML model explanation) taught this concretely. Adding "Audience: VP of Sales with no data science background" to a prompt changes:
- Vocabulary (model → "experienced sales manager who reviewed 10,000 deals")
- Depth (explanation → metaphors, not formulas)
- Format (section structure → concrete workflow)
- Length (academic thoroughness → action-oriented brevity)

One sentence about the audience replaces 10 sentences of formatting instructions.

### 3. Over-Engineering Is as Harmful as Under-Specification
The Choose challenges revealed something counterintuitive: prompts that are too long perform worse than simpler, precise ones. The over-engineered marketing prompt spent 250 words demanding every possible framework before mentioning the actual data. The AI then spent 600 words on methodology before reaching the analysis. Precision is not about length — it's about signal-to-noise ratio.

### 4. Decision Context Transforms Analysis Into Strategy
The board data story scenario revealed the most important business prompting principle: when you tell the AI what decision the audience faces, it knows exactly which insight to amplify. "My audience is deciding whether to expand to 3 markets next quarter" turns a flat metric summary into a strategic narrative with a clear recommendation — without asking for one explicitly.

### 5. Real Constraints Are Worth More Than Adjectives
The dashboard design Clean challenge contained "make it visually stunning" and "60-second morning review" as two competing elements. "60 seconds each morning" told the AI more about design requirements than any aesthetic instruction could. Constraints shape solutions. Adjectives create noise. The game made me realize I've been writing prompts backwards — specifying how I want things to feel when I should be specifying what constraints exist.

---

## Technical Notes
- Vanilla HTML/CSS/JavaScript — zero dependencies
- 6 scenarios with full data (blocks, principle, outputs, DNA mapping)
- HTML5 Drag and Drop API for block placement
- CSS transitions for slot hover/drop states
- Timer with color-coded urgency (amber → red at 20 seconds)
- Animated score counter (count-up animation after each challenge)
- Floating toast notifications for hints and time-up
- DNA bars animate in 400ms after report loads

---

## Deliverables
- `prompt-puzzle.html` — Complete interactive prompt engineering game
- `prompt-puzzle-card.png` — Cinematic Day 35 card (purple theme)
- `day-35.md` — This file

---

*Day 35 of 60 · Built with Claude AI · #60DaysOfAI*
