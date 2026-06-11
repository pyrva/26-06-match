---
date: 2026-06-10
topic: pattern-matching-presentation
focus: Interactive presentation for PyRVA about Python structural pattern matching (3.10+), using Emily Bache coaching style
mode: elsewhere-software
---

# Ideation: PyRVA Pattern Matching Presentation

## Grounding Context

**Topic context:** Python structural pattern matching (match/case from 3.10+) — NOT a switch statement, it's "generalized iterable unpacking." Full feature set: literal, capture, wildcard, OR patterns, class patterns, sequence patterns, mapping patterns, guards, nested patterns. Key pitfall: bare names CAPTURE rather than compare. 5 anti-patterns: simple if/else, computable mappings, dict dispatch, singledispatch, switch-on-value.

**Audience:** PyRVA (Python User Group, Research Triangle NC), mixed experience levels, 60-90 minute slot.

**Style:** Emily Bache coaching approach — coding dojos, facilitated discovery, strong-style pairing ("idea must go through someone else's hands"), start simple for sense of achievement.

**Past PyRVA presentations:** Python Documentation Power Hour used proven format (hook+poll 5min → live demo 10min → paired exercise → share-out → ecosystem tour → challenges 15min → wrap-up). "Coding Night" used only 6 slides, heavily exercise-driven.

**External context:** PEP 636 uses text adventure game as progressive example. Ben Hoyt's before/after refactoring examples (email.utils, ast._convert). Brett Slatkin's PyBeach 2025 talk on patterns/anti-patterns. Emily Bache's Coding Dojo Handbook formats: Prepared Kata, Randori, Mob Programming with Strong-Style Pairing.

## Topic Axes
1. Exercise design — hands-on activities, kata structure, difficulty tiers, exercise domains
2. Presentation flow — session arc (hook → demo → practice → debrief → capstone)
3. Interactivity mechanics — formats of engagement (pairs, mobs, guided discovery, live coding)
4. Concept coverage — which features to cover and how deeply
5. Mixed-level facilitation — serving beginners AND experienced devs simultaneously

## Ranked Ideas

### 1. The Anti-Switch Arc [SELECTED — supporting element]
**Description:** The session's narrative spine. Opens with "match/case is NOT a switch statement" and every exercise progressively proves why. Each stage shatters a different switch assumption.
**Axis:** Presentation flow
**Basis:** `direct:` Ben Hoyt's framing: "generalized concept of iterable unpacking." `reasoned:` Refutation text effect from cognitive science.
**Rationale:** Ensures nobody leaves with the incomplete switch-statement mental model. Gives the session narrative spine.
**Downsides:** Requires careful exercise ordering.
**Confidence:** 92%
**Complexity:** Medium
**Status:** Explored

### 2. One Game, Eight Levels: The Compounding Text Adventure [SELECTED — primary seed for brainstorm]
**Description:** Build the entire session around PEP 636's text adventure domain. Start with minimal command parser (literal matches), progressively layer in capture, guards, OR patterns, mapping, class patterns, nested patterns — all within the same codebase. By the time the adventure needs "look at the golden key in the chest," participants use nested guarded class patterns naturally.
**Axis:** Exercise design
**Basis:** `direct:` PEP 636's text adventure is explicitly designed as progressive tutorial. Domain naturally demands every pattern type.
**Rationale:** Highest-leverage exercise design choice. One repo, one set of tests, one walkthrough. The domain itself teaches.
**Downsides:** May feel toy-like to some. Constrains real-world examples.
**Confidence:** 90%
**Complexity:** Medium
**Status:** Explored

### 3. The Unpacking Frame: One Mental Model
**Description:** Teach "pattern matching is destructuring, not switching" as the single frame. Explain bare names (assignment targets), wildcards, ordering — all through the unpacking analogy.
**Axis:** Concept coverage
**Basis:** `direct:` Ben Hoyt/PEP 635: "generalized iterable unpacking."
**Rationale:** Single correct mental model compounds across every concept. Preemptively kills switch/case misconception.
**Downsides:** Unpacking analogy breaks down for mapping/class patterns.
**Confidence:** 88%
**Complexity:** Low
**Status:** Unexplored

### 4. Tiered Kata Cards with Pre-Baked Repos
**Description:** Three tiers (Apprentice/Journeyer/Artisan) in one repo with hint/solution git branches. Self-serve hints reduce facilitator burden.
**Axis:** Mixed-level facilitation
**Basis:** `direct:` Past PyRVA presentations included scaling strategies. `reasoned:` Environment setup is the largest time sink.
**Rationale:** Turns mixed-level "problem" into a feature. Everyone ships working code.
**Downsides:** Significant prep. Self-selection anxiety.
**Confidence:** 85%
**Complexity:** High (prep), Low (execution)
**Status:** Unexplored

### 5. Predict-Then-Run [SELECTED — supporting element]
**Description:** 3-4 micro-cycles replacing live demo: show match statement → pairs predict output → reveal answer → 2 min to write a variant. Creates "learning impasses" that stick.
**Axis:** Interactivity mechanics
**Basis:** `external:` Predict-Observe-Explain (White & Gunstone, 1992). `direct:` Code-alongs that break are a top frustration.
**Rationale:** Eliminates code-along fragility. Prediction forces active reasoning; surprise when wrong creates strong encoding.
**Downsides:** 2-min intervals may feel short.
**Confidence:** 86%
**Complexity:** Low
**Status:** Explored

### 6. Sabotage Mode
**Description:** Pairs deliberately write worst match/case possible (no syntax errors), swap with another pair, diagnose and fix. Teaches anti-patterns through construction.
**Axis:** Exercise design
**Basis:** `reasoned:` Construction > recognition on Bloom's taxonomy. `direct:` Anti-patterns deepen pattern understanding.
**Rationale:** Most memorable exercise. Generates reusable community artifact.
**Downsides:** Requires prior syntax knowledge. Some find "write bad code" uncomfortable.
**Confidence:** 82%
**Complexity:** Medium
**Status:** Unexplored

### 7. Mob-First Calibrate, Then Pairs With Pulse Checks
**Description:** 5-8 min mob to calibrate + validate environments → break into strong-style pairs → 60-second prediction pulse checks between tiers.
**Axis:** Presentation flow
**Basis:** `direct:` Bache found mobs work for calibration, pairs for sustained work. `reasoned:` Retrieval practice strengthens retention.
**Rationale:** Solves environment validation, room calibration, and continuous assessment simultaneously.
**Downsides:** Mob volunteer may feel intimidated. Pulse checks need anonymous polling setup.
**Confidence:** 84%
**Complexity:** Low
**Status:** Unexplored

## Rejection Summary

| # | Idea | Reason Rejected |
|---|------|-----------------|
| 1 | The Trap Door Opener | Duplicates Anti-Switch Arc |
| 2 | Code First, Explain Never | Too risky for mixed-level beginners |
| 3 | Bug Report as Exercise | Duplicates Sabotage Mode |
| 4 | Pre-Baked Repos (standalone) | Merged into Tiered Kata Cards |
| 5 | The Mystery Output Game | Merged into Predict-Then-Run |
| 6 | Strong-Style Pairing Enforcer | Too granular as standalone |
| 7 | Concept Menu, Not Sequence | Too risky for time-constrained session |
| 8 | One-Thing Journals | Duplicates Debrief as Deliverable |
| 9 | Code Archaeologists | Less interactive than Predict-Then-Run |
| 10 | Strong-Style Randori | Too risky as primary format |
| 11 | Concept Buffet | Better as supporting visual aid |
| 12 | Rosetta Stone Exercise | Requires prerequisite knowledge beginners lack |
| 13 | Exercise Exchange | Exercise quality hard to guarantee |
| 14 | Monster Builder | Duplicates Escape Room |
| 15 | Gallery Walk | Too much setup; Translation Game achieves same |
| 16 | Asymmetric Pair Programming | Too stressful for beginners |
| 17 | Mob Capstone (standalone) | Better as optional capstone format |
| 18 | Reusable Kata Repository | Meta-investment, not session idea |
| 19 | Ear Training | Anti-Switch Arc achieves similar hook |
| 20 | Belt System | Metaphor may feel infantilizing |
| 21 | Detective's Case Board | More complex than Debrief as Deliverable |
| 22 | Recipe Refactoring | Text adventure is proven; adds complexity |
| 23 | Translation Station | Depends on unpredictable audience composition |
| 24 | Code Sommelier | Too much prerequisite knowledge |
| 25 | Lightning Kata Relay | Too rushed for genuine discovery |
| 26 | Anti-Pattern Mob Trial | Sabotage Mode with pairs is safer |
| 27 | Paper Pattern Matching | Translation to code is awkward |
| 28 | Devil's Advocate Debate | Adversarial framing risks discomfort |
| 29 | Fishbowl Relay | Overengineered for likely group size |
| 30 | Guided Discovery (standalone) | Merged into One Game Eight Levels |
| 31 | Match-a-Thon | Too ambitious for time slot |
| 32 | Intimate Mob | Good fallback, not primary plan |
| 33 | Match/Case Migration Kata | Merged into Translation Game |
| 34 | The Translation Game | Absorbed into Sabotage Mode |
| 35 | Drill Then Scrimmage | Partially absorbed by Tiered Kata + Predict-Then-Run |
| 36 | Escape Room capstone | Strong runner-up — consider as session finale |
