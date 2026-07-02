# Day 33 — Media Integrity Analyzer

## Challenge
**Build a Media Integrity Analyzer** — Teach media literacy through interactive discovery, not memorization. Every section explains the concept, shows real-style examples, and reveals manipulation techniques through guided exploration.

*Pure vanilla HTML/CSS/JS — no React, no Tailwind, no external assets.*

---

## What Was Built

A complete **Media Literacy Educational App** — single HTML file, pure vanilla JavaScript and CSS. Works fully offline. Theme selection, two interactive challenges, live metrics, and a final Media Integrity Dashboard.

**File:** `media-integrity-analyzer.html`

---

## Theme Selection (5 Options)
- 🟠 **Claude Orange** — Signature (#FF6B35)
- 🔵 **Ocean Blue** — Investigative (#0EA5E9)
- 🟢 **Emerald** — Clarity (#10B981)
- 🟣 **Amethyst** — Deep Dive (#8B5CF6)
- 🔴 **Crimson** — Alert Mode (#EF4444)

Each theme changes CSS custom properties (`--accent`, `--accent-rgb`, `--glow`) across the entire app instantly.

---

## Challenge 1: Headline Detective

### What It Teaches
News headlines are written to maximize engagement, not accuracy. Common manipulation tactics: CAPS for false urgency, exaggerated scale, certainty words for preliminary findings, conspiracy framing, identity triggers ("YOUR morning coffee").

### 4 Randomized Headline Scenarios

**Scenario 1: Health Misinformation**
- Headline: "Scientists CONFIRM: Drinking This Common Beverage Will Add 10 Years to Your Life"
- Reality: 47-person, non-peer-reviewed preliminary study found marginal cardiovascular markers
- Accuracy Score: 14% | Source Reliability: 20%
- Flags: "CONFIRM," "10 Years," "Big Corporations Hiding," mystery beverage bait

**Scenario 2: Scale Exaggeration**
- Headline: "BREAKING: Mysterious Outbreak Spreads Across Entire City, Officials Completely Overwhelmed"
- Reality: 12 food poisoning cases at one restaurant, officials called it "routine"
- Accuracy Score: 18% | Source Reliability: 22%
- Flags: "BREAKING," "Entire City," "Overwhelmed," "Spirals Out of Control"

**Scenario 3: Screenshot Misinformation**
- Headline: "Whistleblower's DELETED Message Exposes the Secret Plan to Control What You Think"
- Reality: Unverified screenshot flagged as fabricated by digital forensics experts
- Accuracy Score: 8% | Source Reliability: 12%
- Flags: "DELETED," "Secret Plan," "Control Your Mind," "Save Before Taken Down"

**Scenario 4: Science Distortion**
- Headline: "WARNING: The Ingredient in YOUR Morning Coffee Is Being Linked to Permanent Brain Damage"
- Reality: Mouse study using doses equivalent to 40+ cups/day; authors said don't draw human conclusions
- Accuracy Score: 12% | Source Reliability: 25%
- Flags: "WARNING," "YOUR," "Permanent Brain Damage," "Millions at Risk"

### User Interaction Flow
1. Read headline + article naturally
2. Click: Would you click? (Yes / Maybe / No)
3. Click on any words in the headline that seem misleading
4. Reveal: Accuracy score, flagged phrases with explanations, fair rewritten headline, key takeaway

---

## Challenge 2: Emotion Detector

### What It Teaches
Some content is engineered to trigger strong emotions specifically to bypass critical thinking and maximize sharing. The stronger the emotional reaction, the more likely the critical brain steps back.

**Common techniques:**
- Fear Appeal — "Your children are at risk"
- Outrage Bait — Designed to generate anger enough to share
- False Urgency — "Share before they delete this"
- Us vs. Them — Villain/hero framing
- Vulnerability Performance — Fake personal stories to build false trust

### 4 Randomized Emotion Scenarios

**Scenario 1: Parental Fear Post (Facebook)**
- Content: Food contamination warning targeting parents with "SECRETLY," "SILENCED," "HIDING"
- Manipulation Score: 94% | Audience Targeting: 92%
- Technique: Fear Appeal + Parental Guilt + Conspiracy Framing + Urgency Sharing Pressure

**Scenario 2: Economic Outrage (Twitter/X)**
- Content: AI job replacement + billionaire bonuses + "staying silent is COMPLICIT"
- Manipulation Score: 82% | Audience Targeting: 88%
- Technique: Outrage Amplification + Us vs. Them Framing + Silence = Complicity Guilt

**Scenario 3: Aspirational Bait (Instagram)**
- Content: "Broke at 31 → $40K/month in 6 months, 2 hours a day" leading to "FREE guide"
- Manipulation Score: 86% | Audience Targeting: 84%
- Technique: Aspirational Bait + Vulnerability Performance + Engagement Farming + False Scarcity

**Scenario 4: Financial Fear Article**
- Content: "CONFIRMED: New policy will make groceries IMPOSSIBLE to afford by March"
- Manipulation Score: 90% | Audience Targeting: 90%
- Technique: Fear Amplification + Definitive Framing for Speculation + Hidden Knowledge Sales Hook

### User Interaction Flow
1. Read the post/article as you would while scrolling
2. Select how it made you feel (6 emotion options)
3. Click on words that triggered your emotional reaction
4. Reveal: Manipulation score, target audience, technique breakdown, highlighted trigger words, neutral rewrite, key takeaway

---

## Live Metrics (Updated Throughout)

| Metric | Color | What It Measures | Updates After |
|--------|-------|-----------------|---------------|
| Headline Accuracy | Green | How accurately the headline represents the article | Challenge 1 |
| Source Reliability | Blue | How reliable the content source appears | Challenge 1 |
| Emotional Manipulation | Red | How much emotional manipulation is present | Challenge 2 |
| Audience Targeting | Amber | How specifically the content targets a vulnerable audience | Challenge 2 |

Metrics displayed as a fixed bottom strip with animated fill bars visible throughout the session.

---

## Media Integrity Dashboard

**User Score Calculation:**
- Baseline: 40 points
- Clicked "No" on headline (skeptical): +20
- Clicked "Maybe" (cautious): +10
- Identified correct misleading words in headline: +30
- Selected "Suspicious" emotion: +20
- Identified correct emotional trigger words: +30
- Maximum: ~100%

**Grade Scale:**
- 85%+: 🔍 Media Literacy Expert
- 70-84%: 📚 Critical Thinker
- 55-69%: 🧭 Learning to Look Deeper
- <55%: 🌱 Beginning Your Journey

**3 Practical Habits Taught:**
1. Read before you share — headlines are designed for sharing without reading
2. Notice your emotion before acting — strong emotion = critical thinking being bypassed
3. Search for the primary source — most misleading content has traveled through distortion layers

---

## My Session Results

**Theme:** Claude Orange 🟠

**Headline analyzed:** "Scientists CONFIRM: Drinking This Common Beverage Will Add 10 Years to Your Life"
- Click answer: No (recognized sensationalism)
- Correctly flagged: CONFIRM, "10 Years," conspiracy framing
- Headline Accuracy revealed: 14%
- Source Reliability: 20%

**Emotion post analyzed:** Parental Food Safety Fear Post
- Felt: Suspicious (recognized the manipulation formula)
- Correctly identified: "URGENT," "SECRETLY contaminated," "SILENCED," sharing pressure
- Manipulation Score: 94%
- Audience Targeting: 92%

**Final Score: 82% — 📚 Critical Thinker**

---

## Key Learnings

### 1. One Word Can Do Enormous False Work
The word "CONFIRMS" in a science headline is doing enormous work. A 47-person, non-peer-reviewed preliminary study confirms nothing — it suggests a hypothesis worth investigating. The gap between what "CONFIRMS" implies (certainty, scientific consensus, replication) and what the study actually represents is where the manipulation lives. Most readers never reach the article to discover this.

### 2. Scale Exaggeration Is the Most Common Manipulation Tactic
The hardest headline scenario was the "city-wide outbreak" that turned out to be 12 food poisoning cases at one restaurant. The headline described a crisis; the article described a routine inspection. This 10x exaggeration of scale is the most common form of headline manipulation because it's difficult to detect without reading the full article — which most people never do.

### 3. "Share Before They Delete This" Is a Specific Manipulation Formula
The urgency phrase "save this before it's taken down" has one function: to get you to share before your critical thinking can engage. If information is genuinely important, it exists on multiple sources, has been covered by multiple journalists, and hasn't disappeared. Content that needs to be shared "before it's deleted" is almost always either false or deeply exaggerated.

### 4. Strong Emotion Is a Signal, Not Just a Response
The most practically useful insight from this challenge: strong emotional reactions to content are not proof that something important is happening. They are evidence that the content was engineered to produce that reaction. This doesn't mean all emotional content is false — but it does mean that the moment you feel strongly about sharing something, that's exactly when you should slow down, not speed up.

### 5. The Neutral Rewrite Is the Most Revealing Exercise
Seeing the neutral rewrite of manipulative content next to the original is the clearest demonstration of how much information is added through emotional language that doesn't exist in the underlying facts. The $40K/month Instagram post becomes: "Advertisement: This account sells online business courses. Results vary." The food safety panic becomes: "A consumer advocacy group sent a letter requesting ingredient clarification." The rewrite makes the manipulation structure visible in a way that explanation alone can't.

---

## Deliverables
- `media-integrity-analyzer.html` — Complete interactive media literacy app
- `integrity-card.png` — Cinematic Day 33 card (Claude Orange editorial theme)
- `day-33.md` — This file

---

*Day 33 of 60 · Built with Claude AI · #60DaysOfAI*
