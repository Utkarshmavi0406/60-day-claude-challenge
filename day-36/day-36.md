# Day 36 — Cognitive Pattern Explorer

## Challenge
**Explore Your Thinking Patterns** — Build a psychology-inspired self-reflection experience that explores thinking patterns through interactive scenarios. Calm, game-like, and exploratory — never clinical or diagnostic.

---

## What Was Built

A complete **Cognitive Pattern Explorer** — single HTML file, pure vanilla JavaScript and CSS. Two exploration modes (Calm/Stress), three interactive chapters, and a personalized Reflection Journal with thinking profile breakdown.

**File:** `cognitive-pattern-explorer.html`

---

## Important Disclaimer

This app is **educational only**. It uses reflective language ("you often...," "this suggests...") rather than clinical labels. It does not diagnose, assess, or clinically evaluate mental health in any way. All content is designed for self-reflection and curiosity — not medical or psychological assessment.

---

## Two Exploration Modes

### 🌿 Calm Mode
Scenarios framed as everyday, low-pressure situations. Soft purple/lavender color theme with floating ambient orbs. Encourages reflection at a gentle pace.

### ⚡ Stress Mode
The same structural activities with higher-stakes, pressure-framed language. Warm orange/amber color theme. Designed to reveal whether thinking patterns shift under pressure — which often produces the most interesting self-knowledge.

---

## App Flow (3 Chapters + Journal)

### Chapter 1: Discover Your Thinking Style
5 scenarios, 5 options each (one per tendency). Options are shuffled randomly. User clicks their most natural response.

**Calm Mode scenarios:**
1. Unexpected project deadline change (Monday morning)
2. Close friend's honest feedback about being distant
3. Exciting but uncertain new opportunity
4. Hard work doesn't pay off as hoped
5. Meaningful decision without complete information

**Stress Mode scenarios:**
Same themes with higher-stakes framing (manager messaging urgently, public failure, end-of-day deadline with missing information).

### Chapter 2: What Matters Most?
5 priority cards to arrange in personal order (most → least important). Drag-and-drop on desktop, touch-and-hold on mobile. Top 2 ranked cards contribute to scoring.

**Cards:**
- Gathering complete information
- Trusting my emotional read
- Anticipating what could go wrong
- Acting quickly and decisively
- Finding the most balanced approach

### Chapter 3: Map Your Thinking
6 thinking steps to arrange in personal sequence. First 3 positions contribute to scoring.

**Steps:**
- Gather information and facts
- Notice my emotional reaction
- Identify potential risks
- Talk it through with someone
- Make a decision and act
- Reflect on the outcome

### Reflection Journal
- **Thinking Profile Breakdown** — 5 animated bars showing % weight of each tendency
- **Primary Tendency Card** — Profile, strength, and "worth noticing" note
- **Secondary Tendency** — Shown if within 10% of primary
- **3 Key Insights** — Personalized to dominant tendency + mode comparison note
- **Mode Reflection** — Encourages comparison between Calm and Stress mode results

---

## 5 Thinking Tendencies

| Tendency | Emoji | Tag | Core Profile |
|----------|-------|-----|-------------|
| Analytical Thinker | 🔍 | Data-Driven | Seeks information before acting; systematic and considered |
| Emotional Intuitive | 🌊 | Feeling-Led | Tunes into emotional current first; trusts gut and empathy |
| Overthinking Loop Style | 🌀 | Deep Processor | Cycles through possibilities; strong desire to get it right |
| Action-First Thinker | ⚡ | Movement-Oriented | Moves before full picture emerges; trusts adjustment in motion |
| Balanced Reflective Thinker | ⚖️ | Adaptive | Flexes between approaches depending on situation |

---

## Scoring System

**Chapter 1 (5 scenarios, 5 options each):**
- Each selected option: +1 to that tendency

**Chapter 2 (Priority ranking):**
- #1 ranked card: +3 to that tendency
- #2 ranked card: +2 to that tendency

**Chapter 3 (Thinking sequence):**
- Step placed first: +3 to that tendency
- Step placed second: +2
- Step placed third: +1

**Total → Percentage:**
Sum all tendency points, calculate each as % of total. Display as animated bar chart.

---

## Technical Features

**Drag-and-Drop:**
- HTML5 Drag and Drop API for desktop
- Custom touch event handling for mobile (touchstart/touchmove/touchend)
- Visual feedback: dragging item gets opacity reduction, target item gets highlight
- Rank numbers update dynamically as order changes

**Transitions:**
- Screen transitions: CSS keyframe animation (translateY + opacity)
- Bar chart: CSS transition on width, triggered 200ms after journal loads
- Progress dots: CSS transition on width (shows active step as wider pill)

**Accessibility:**
- `aria-label` on all interactive elements
- `role` attributes on custom list/radio elements
- Keyboard navigation for mode selection (Enter/Space)
- `prefers-reduced-motion` media query support

**Ambient Design:**
- Three floating orbs with CSS `filter:blur()` + keyframe float animation
- Mode switching updates CSS custom properties via body class
- Calm mode: purple/lavender palette
- Stress mode: orange/amber palette

---

## My Results

**Mode:** Calm Mode

**Thinking Profile:**
- 🔍 Analytical: 22%
- 🌊 Emotional Intuitive: 18%
- 🌀 Overthinking Loop: 12%
- ⚡ Action-First: 20%
- ⚖️ Balanced Reflective: 28%

**Primary Tendency:** Balanced Reflective Thinker (28%)

**Key Insight from the experience:** The "Stress Mode" design choice was the most interesting psychological element to build. The hypothesis embedded in the app is that thinking patterns under pressure differ from thinking patterns in calm states — and that gap is where genuinely useful self-knowledge lives. Someone who identifies as an "Action-First Thinker" in calm mode might discover they become an "Overthinking Loop" thinker under stress. That's not a contradiction — it's a useful distinction.

---

## Key Learnings

### 1. Self-Reflection Tools Work Best When They Don't Feel Like Tests
The design principle I held throughout: every interaction should feel like exploration, not assessment. The scenarios have no "correct" answers displayed. The tendencies don't have good/bad framing. The language says "you often" rather than "you are." When people don't feel evaluated, they respond more honestly — and get more from the experience.

### 2. The Gap Between Calm and Stressed Defaults Is the Real Insight
The most educational thing this app teaches is something you can only discover by doing it twice: your thinking patterns under everyday conditions and your thinking patterns under pressure are often meaningfully different. Building Stress Mode required rewriting every scenario with higher stakes while keeping the options the same. That structural difference is the educational point — not which tendency scores highest.

### 3. Overthinking is a Form of Care, Not a Weakness
Writing the Overthinking Loop Style profile taught me something: the reason people get caught in thinking loops isn't that they're broken — it's that they care deeply about getting it right and are trying to protect something they value. Framing it that way in the reflection ("this reflects a genuine desire to make the right choice") changes how people receive the feedback. Psychology-inspired apps need to carry this nuance.

### 4. Drag-and-Drop Priority Ranking Reveals More Than Multiple Choice
When I designed Chapter 2 (Priority Ranking) vs Chapter 1 (Scenario Response), I noticed they were actually testing different things. Chapter 1 reveals instinctive responses. Chapter 2 reveals declared values — what someone explicitly believes they prioritize. The gap between Chapter 1 scores and Chapter 2 scores is itself information. Someone might respond emotionally to scenarios but consciously rank "gathering information" as their top priority. Both are true simultaneously.

### 5. The Thinking Sequence (Chapter 3) Reveals Process, Not Preference
Asking someone to arrange steps in order (gather info → feel → consult → risk-assess → decide → reflect) reveals how they mentally model their own decision process. This is different from which tendency they select OR which priority they rank. It's a metacognitive exercise — thinking about thinking — which operates at a different level than the other chapters. Combining all three gives a richer picture than any one method alone.

---

## Deliverables
- `cognitive-pattern-explorer.html` — Complete interactive self-reflection app
- `cognitive-card.png` — Cinematic Day 36 card (purple/indigo theme)
- `app-start.png` — App start screen screenshot
- `day-36.md` — This file

---

*Day 36 of 60 · Built with Claude AI · #60DaysOfAI*
