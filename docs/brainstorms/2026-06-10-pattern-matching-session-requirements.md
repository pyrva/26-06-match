---
date: 2026-06-10
topic: pattern-matching-session
output: md
status: draft
---

# Requirements: PyRVA Pattern Matching Workshop

## Summary

A 60–90 minute interactive workshop for PyRVA on Python structural pattern matching (3.10+), built around a text adventure game domain. Participants discover the feature through an "Anti-Switch Arc" narrative — each exercise progressively reveals why `match`/`case` is *generalized unpacking*, not switching. Delivered through predict-then-run micro-cycles and strong-style pair exercises, using Emily Bache's coaching philosophy.

---

## Problem Frame

Most Python developers hear "match/case" and think "Python finally got a switch statement." This mental model is actively harmful — it prevents people from understanding structural destructuring, capture semantics, and class patterns. The session's entire arc is designed to confront and replace this misconception through progressive discovery, not lecture.

---

## Learning Objectives

After this session, participants will be able to:

1. **Distinguish** pattern matching from switch/case — explain why bare names capture rather than compare, and why ordering matters
2. **Use** literal, capture, sequence, OR, guard, and class patterns in a `match`/`case` block
3. **Choose** when `match`/`case` is the right tool vs. `if`/`elif`, dict dispatch, or `singledispatch`
4. **Recognize** the 5 anti-patterns (simple if/else replacement, computable mappings, dict dispatch, singledispatch, basic switch-on-value)

---

## Session Structure

Target duration: **75 minutes** with flexibility to stretch to 90 or compress to 60.

### Phase 1: Hook + Calibrate (10 min)

**Narrative:** "How many of you think `match`/`case` is Python's switch statement? Great — forget that."

**Activities:**
- **Anti-Switch poll** (1 min) — show of hands on "is match/case a switch statement?" The answer is no, and we'll spend the session proving why.
- **The Unpacking Frame** (3 min) — `first, *rest = [1, 2, 3]` on screen. Ask pairs to predict what `first` and `rest` hold. Then: "Pattern matching is *this operation generalized*. Variables are assignment targets, not comparisons. This single idea explains everything we'll do tonight."
- **Mob calibration** (6 min) — facilitator navigates, volunteer drives. Solve the simplest text adventure command together: `case "quit":` → game exits. Validates one environment for the whole room. Shows the workflow. Reads the room's skill level.

**Key facilitator moment:** If the mob reveals most people are beginners, slow the pace. If mostly experienced, speed up and add complexity in later phases.

### Phase 2: Level 1 — Literal & Wildcard Patterns (10 min)

**Anti-Switch Arc:** This is the one level where switch thinking *works*. Literal matches look exactly like a switch statement. Let participants get comfortable here before subverting it.

**Predict-Then-Run cycle:**
- Show `match command: case "quit": ... case "look": ... case _: ...`
- Pairs predict what happens for input `"look"`, `"inventory"`, `"QUIT"` (case sensitivity surprise)
- Reveal with explanation: `_` is the wildcard, like `*rest` in unpacking
- **2-minute pair exercise:** Add handlers for `"help"` and `"inventory"` in the text adventure

**Text adventure commands:** `quit`, `look`, `help`, `inventory`, `_` (unknown)

**Pulse check:** Show `match "LOOK": case "look": ... case _: ...` — what matches? (Answer: the wildcard. Case-sensitive.)

### Phase 3: Level 2 — Capture & Sequence Patterns (12 min)

**Anti-Switch Arc:** Switch thinking *breaks here*. A switch statement matches on a single value. `match`/`case` destructures sequences. This is where the "generalized unpacking" frame clicks.

**Predict-Then-Run cycle:**
- Show `command = "go north".split()` → `["go", "north"]`
- Show `match command: case ["go", direction]: print(direction)`
- Pairs predict: what is `direction`? What happens for `"go"` alone? For `"go north east"`?
- Reveal: `direction` is bound to `"north"` (capture pattern!). Single word `"go"` doesn't match. Three words don't match.
- **The big reveal:** `direction` is an *assignment target*, not a comparison. This is unpacking, not switching.

**Pair exercise (6 min):** Implement command handlers in the text adventure:
- `["go", direction]` → move in a direction
- `["take", item]` → pick up an item
- `["examine", target]` → look at something
- Bonus: `["go", *args]` → what happens with `"go north east"`?

### Phase 4: Level 3 — OR Patterns & Guards (12 min)

**Anti-Switch Arc:** Switch statements can match multiple values with fall-through. Pattern matching does this explicitly with `|`, *and* adds conditional logic with guards — something switch cannot do at all.

**Predict-Then-Run cycle:**
- Show `case ["go", ("north"|"south"|"east"|"west") as direction]:`
- Pairs predict: what does `direction` hold for `"go north"`? For `"go up"`?
- Show guard: `case ["go", direction] if direction in current_room.exits:`
- Pairs predict: what happens when direction is valid? When invalid?
- Reveal: OR patterns group alternatives with a single binding. Guards add arbitrary conditions *after* structural matching.

**Pair exercise (6 min):**
- Add direction abbreviations: `"n"|"north"`, `"s"|"south"`, etc.
- Add a guard that validates the direction exists in the current room
- Add a fallback `case ["go", _]:` that says "You can't go that way"

### Phase 5: Level 4 — Class Patterns (15 min)

**Anti-Switch Arc:** Switch thinking is *impossible here*. You cannot switch on an object's type and extract attributes in one expression. This is the "generalized unpacking" frame at its most powerful.

**Predict-Then-Run cycle:**
- Introduce event objects: `Click(position=(3, 7))`, `KeyPress(key="q")`, `Quit()`
- Show `match event: case Click(position=(x, y)): print(x, y)`
- Pairs predict: what are `x` and `y`? What matches `Quit()`? What matches `KeyPress(key="q")`?
- Reveal: class patterns combine `isinstance` + attribute extraction in one expression. `case Quit():` checks type *and* binds nothing (no positional args).

**Pair exercise (8 min):**
- Implement an event handler for the text adventure:
  - `case Click((x, y)):` → describe what's at that position
  - `case KeyPress("q") | KeyPress("Q"):` → quit
  - `case KeyPress(key) if key in "wasd":` → movement shortcuts
  - `case TextCommand(text):` → parse as text command (feeds into earlier levels)

**Pulse check:** Show `case KeyPress(key) if key == "q":` vs `case KeyPress("q"):` — which is "better"? (Debatable — the literal is simpler, the guard is more explicit. Good discussion prompt.)

### Phase 6: Capstone — Sabotage Mode (15 min)

**Anti-Switch Arc payoff:** Now that you know *how* to use `match`/`case`, learn *when not to*.

**Activity:**
1. Each pair takes a working `match`/`case` block from the text adventure and makes it as bad as possible — confusing, fragile, buggy — without syntax errors (3 min)
2. Swap with another pair (1 min)
3. Diagnose and fix the other pair's sabotage (6 min)
4. Debrief: collect the room's "greatest hits" anti-patterns on a shared board (5 min)

**Anti-patterns to discover:**
- Unreachable cases (wrong ordering)
- Over-broad captures (bare names catching everything)
- Missing wildcard (unhandled inputs crash)
- Cases that should be `if`/`elif` (simple equality on 2 values)
- Cases that should be `dict.get()` (value-to-value mapping)

### Phase 7: Wrap-up (5 min)

- **Participant takeaways:** Each person says (or writes on sticky) the one thing that surprised them most
- **The Unpacking Frame recap:** "What would unpacking do here?" is the question that answers every `match`/`case` question
- **Resources:** PEP 636 tutorial, Ben Hoyt's article, the exercise repo for later practice
- **The closing question:** "What would you have missed if you kept calling this a switch statement?"

---

## Exercise Repo Requirements

The exercise repo must support:

- **Single domain:** The text adventure game runs throughout. One codebase, progressively extended.
- **Tiered difficulty:** Apprentice (Levels 1–2), Journeyer (Levels 3–4), Artisan (Level 4 + advanced variants). Participants self-select after the mob calibration.
- **Hint branch:** `git diff hint` shows partial solutions. Pairs self-rescue without raising a hand.
- **Solution branch:** Complete working code for reference.
- **Tests:** Each level has a test suite. Running `pytest` immediately validates the environment. Tests are the "puzzle" — make them pass.
- **Starter code:** `TODO` markers and `pass` statements where participants write their `match` blocks. Clear comments explain what each handler should do.

### Text Adventure Domain Model

The game has:
- **Rooms** with exits, descriptions, and items
- **Items** with names and descriptions
- **Events** (Click, KeyPress, Quit, TextCommand) — introduced at Level 4
- **Commands** parsed from user input: `quit`, `look`, `go <direction>`, `take <item>`, `examine <target>`, `help`, `inventory`

The starting room has a few exits and items to keep the domain simple but extensible.

---

## Facilitator Guide Requirements

The facilitator guide must include:

- **Timing markers** for each phase with "if running long" and "if running short" fallback plans
- **Predict-Then-Run answer keys** — the expected predictions and the actual outputs for each micro-cycle
- **Common pair struggles** per level — what pairs typically get stuck on and the hint to give
- **Environment troubleshooting** — Python 3.10+ requirement, how to verify (`python --version`), fallback for older versions (Google Colab link)
- **Mob calibration tips** — how to read the room, when to speed up or slow down
- **Fallback plans:**
  - Running short → add Sabotage Mode examples, extend debrief
  - Running long → cut Level 4 (class patterns), go straight from Level 3 to Sabotage Mode
  - Mostly beginners → slow pace, spend more time on Levels 1–2, use full 90 min
  - Mostly experienced → speed through Levels 1–2, add complexity to Levels 3–4, include mapping patterns

---

## Success Criteria

- **Every participant** writes at least one working `match`/`case` block with their own hands
- **Every participant** can articulate the difference between pattern matching and switch/case (verified in wrap-up)
- **No participant** spends more than 3 minutes on environment setup
- **The room** produces a shared anti-pattern list during Sabotage Mode debrief
- **Participants** leave with the exercise repo for continued practice

---

## Scope Boundaries

### In scope
- 4–5 deep exercise levels with predict-then-run hooks
- Exercise repo with tiered difficulty, tests, hint/solution branches
- Facilitator guide with timing, answer keys, fallback plans
- Sabotage Mode as capstone anti-pattern exercise

### Deferred for later
- Mapping patterns (`{"key": value, **rest}`) — advanced, niche
- Complex nested patterns (3+ levels deep) — too much for one session
- Full slide deck — session uses minimal/no slides
- `__match_args__` customization — too implementation-focused

### Outside this session
- Comparison with pattern matching in other languages (Rust, Scala, Haskell)
- `singledispatch` deep-dive (mentioned as alternative, not taught)
- Integration with type checkers (mypy, pyright) and exhaustiveness checking

---

## Dependencies and Assumptions

- **Python 3.10+** is required for `match`/`case`. Participants must have it installed or use a provided Google Colab link.
- **PyRVA venue** has projector/screen, WiFi, and power for laptops. Room supports pair seating.
- **Attendance** is 10–25 people (typical for PyRVA). Format adjusts if significantly more or fewer.
- **Participants bring laptops** with Python installed. A backup Colab link handles corporate/restricted machines.
- **Facilitator** is comfortable with mob programming facilitation and strong-style pairing rules.

---

## Outstanding Questions

- **Q1:** Should the text adventure have a graphical component (terminal colors, ASCII map) or remain pure text? (Pure text is simpler; colors add engagement.)
- **Q2:** Should we use a polling tool (Mentimeter, Slido) for pulse checks, or keep it show-of-hands? (Polling is anonymous — better data — but adds setup.)
