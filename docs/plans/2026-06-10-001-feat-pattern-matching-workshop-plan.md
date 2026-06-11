---
date: 2026-06-10
status: active
depth: standard
origin: docs/brainstorms/2026-06-10-pattern-matching-session-requirements.md
---

# Plan: PyRVA Pattern Matching Workshop

## Summary

Build an interactive workshop for PyRVA on Python structural pattern matching. The deliverable is a self-contained exercise repo with a text adventure game (PEP 636 domain), tiered difficulty levels, hint/solution git branches, a pytest test suite, and a facilitator guide. The session runs 60–90 minutes with 4–5 deep exercise levels progressing from literal/wildcard patterns through capture/sequence, OR/guards, class patterns, and an anti-pattern capstone.

---

## Problem Frame

Python developers hear "match/case" and think "switch statement." This workshop confronts that misconception through progressive discovery using a text adventure game domain. Every exercise level reveals why match/case is *generalized unpacking*, not switching. The deliverable is the exercise repo and facilitator guide — not slides or a lecture.

---

## Requirements

- **R1.** Exercise repo with text adventure game domain following PEP 636's progressive example
- **R2.** 4 exercise levels covering literal/wildcard → capture/sequence → OR/guards → class patterns
- **R3.** Sabotage Mode capstone exercise for anti-patterns (Level 5)
- **R4.** Tiered difficulty (Apprentice/Journeyer/Artisan) with self-selection after mob calibration
- **R5.** Hint branch (`hint`) with partial solutions visible via `git diff`
- **R6.** Solution branch (`solution`) with complete working code
- **R7.** Test suite per level — participants make tests pass
- **R8.** Facilitator guide with timing, predict-then-run answer keys, common struggles, fallback plans
- **R9.** Follow PyRVA conventions: src/ layout, pyproject.toml, uv, pytest, ruff
- **R10.** Starter code with TODO markers where participants write match/case blocks

---

## Key Technical Decisions

**KTD-1. Text adventure domain model.** The game has Rooms (with exits, descriptions, items), Items (name, description), and Events (dataclasses: Click, KeyPress, Quit, TextCommand). Commands are parsed from strings via `.split()` into lists for Levels 1–3. Level 4 introduces event objects. This follows PEP 636's approach but extends it with dataclass events for the class patterns exercise. *(see origin: requirements doc — Exercise Repo Requirements)*

**KTD-2. Difficulty tiers map to exercise levels.** Apprentice = Levels 1–2 (literal, wildcard, capture, sequence). Journeyer = Levels 3–4 (OR patterns, guards, class patterns). Artisan = Level 4 with advanced variants + Sabotage Mode. All tiers work in the same codebase — the difference is how far participants go.

**KTD-3. Test-driven exercises.** Each level has a `test_levelN_*.py` file with failing tests. Participants make tests pass by writing match/case blocks. Tests serve as both specification and validation. This eliminates the need for participants to understand the full game architecture — they just need to make the handler function work.

**KTD-4. Module-per-level structure.** Each exercise level is a separate Python module (`src/adventure/handlers_level1.py`, etc.) with a `handle_command()` or `handle_event()` function containing TODO markers. This lets participants focus on one file per level without navigating the full codebase. The game engine imports the appropriate handler based on which level is active.

**KTD-5. Sabotage Mode uses pre-written good code.** The `src/adventure/sabotage_targets.py` file contains 5 well-written match/case blocks (one per anti-pattern category). Pairs modify these to be terrible, then swap. This avoids the problem of pairs not knowing enough to write plausible bad code.

---

## Output Structure

```
pyproject.toml
.python-version
README.md
FACILITATOR_GUIDE.md
src/
  adventure/
    __init__.py
    game.py                    # Game engine (Room, Item, Player)
    events.py                  # Event dataclasses (Click, KeyPress, Quit, TextCommand)
    handlers_level1.py         # Level 1: literal + wildcard patterns (TODO markers)
    handlers_level2.py         # Level 2: capture + sequence patterns (TODO markers)
    handlers_level3.py         # Level 3: OR patterns + guards (TODO markers)
    handlers_level4.py         # Level 4: class patterns (TODO markers)
    handlers_complete.py       # Reference: all levels implemented (for game testing)
    sabotage_targets.py        # Pre-written good match blocks for Sabotage Mode
tests/
  __init__.py
  test_level1_literal_wildcard.py
  test_level2_capture_sequence.py
  test_level3_or_guards.py
  test_level4_class_patterns.py
  test_sabotage_examples.py    # Tests that should FAIL after sabotage
docs/
  brainstorms/
  ideation/
  plans/
```

---

## Implementation Units

### U1. Project Scaffolding and Game Engine

**Goal:** Set up the project structure, dependencies, and core game model (Room, Item, Player) so exercise handlers have something to work against.

**Requirements:** R1, R9, R10

**Dependencies:** None

**Files:**
- `pyproject.toml`
- `.python-version`
- `src/adventure/__init__.py`
- `src/adventure/game.py`
- `tests/__init__.py`

**Approach:** Create the project with hatchling build backend, Python 3.10+ requirement, pytest and ruff in dev dependencies. The game engine defines `Room` (name, description, exits dict, items list), `Item` (name, description), and `Player` (current_room, inventory). Include a `create_game()` function that sets up a small adventure with 3–4 rooms and a few items. The engine provides a `run_command(player, command)` entry point that delegates to the active handler module. Keep the game model minimal — no persistence, no saving, just in-memory state.

**Patterns to follow:** PyRVA verified_fakes project — src/ layout, hatchling backend, uv lockfile, ruff config.

**Test scenarios:**
- Game creates with valid rooms and items
- Player starts in the starting room
- Room has correct exits and items
- Game engine delegates command parsing to handler

**Verification:** `uv run pytest` passes. `uv run python -m adventure` runs a minimal game loop.

---

### U2. Event Dataclasses

**Goal:** Define the event classes used in Level 4 (class patterns exercise) and the TextCommand wrapper.

**Requirements:** R1, KTD-1

**Dependencies:** U1

**Files:**
- `src/adventure/events.py`

**Approach:** Define dataclasses: `Click(position: tuple[int, int])`, `KeyPress(key: str)`, `Quit()`, `TextCommand(text: str)`. Set `__match_args__` on Click so `case Click((x, y)):` works positionally. These are the event types participants will pattern-match in Level 4. Keep them simple — no methods, no validation, just data holders.

**Test scenarios:**
- Each event type instantiates with correct attributes
- Click stores position as tuple
- KeyPress stores key as string
- Quit has no required attributes
- TextCommand stores text as string

**Verification:** Events instantiate and their attributes are accessible.

---

### U3. Level 1 — Literal and Wildcard Patterns

**Goal:** Create the Level 1 exercise module and test suite. Participants implement command handlers using literal matches and the wildcard pattern.

**Requirements:** R2, R7, R10

**Dependencies:** U1

**Files:**
- `src/adventure/handlers_level1.py`
- `tests/test_level1_literal_wildcard.py`

**Approach:** The handler module has a `handle_command(player, command: str) -> str` function. Command is a raw string. The function body is a `match command:` with TODO markers: `case "quit":` → return "Goodbye!", `case "look":` → return room description, `case "help":` → return help text, `case _:` → return "I don't understand". Tests verify each command returns the expected response. The game engine's `run_command` calls this handler directly (no `.split()` at this level — single-word commands only).

**Patterns to follow:** Test structure from verified_fakes — descriptive test names, parametrized where sensible.

**Test scenarios:**
- `"quit"` returns goodbye message
- `"look"` returns current room description
- `"help"` returns help text with available commands
- `"inventory"` returns player's inventory (or "empty" message)
- Unknown commands like `"fly"`, `"dance"` return default "I don't understand" message
- Case sensitivity: `"LOOK"` returns default (not "look") — this is a predict-then-run surprise

**Verification:** All Level 1 tests pass when TODO markers are filled in. Tests fail with the starter code.

---

### U4. Level 2 — Capture and Sequence Patterns

**Goal:** Create the Level 2 exercise module and test suite. Participants implement multi-word command handlers using capture and sequence patterns.

**Requirements:** R2, R7, R10

**Dependencies:** U1, U3

**Files:**
- `src/adventure/handlers_level2.py`
- `tests/test_level2_capture_sequence.py`

**Approach:** The handler module has `handle_command(player, words: list[str]) -> str`. Input is pre-split via `command.split()`. Participants write `match words:` with capture patterns: `case ["go", direction]:` → move player, `case ["take", item]:` → add to inventory, `case ["examine", target]:` → describe item or feature. Tests verify movement between rooms, item pickup, and examination. Include a bonus case for `["go", *args]` to show extended unpacking.

**Test scenarios:**
- `["go", "north"]` moves player to north room and returns new room description
- `["go", "south"]` moves player to south room
- `["go", "east"]` returns "You can't go that way" (no east exit)
- `["take", "sword"]` adds sword to inventory and returns pickup message
- `["take", "sword"]` again returns "You already have that"
- `["examine", "sword"]` returns sword description (if in room or inventory)
- `["examine", "dragon"]` returns "You don't see that here"
- `["go"]` (no direction) falls through to wildcard
- `["go", "north", "fast"]` (extra words) falls through to wildcard — predict-then-run moment

**Verification:** All Level 2 tests pass when TODO markers are filled in.

---

### U5. Level 3 — OR Patterns and Guards

**Goal:** Create the Level 3 exercise module and test suite. Participants add command aliases (OR patterns) and conditional matching (guards).

**Requirements:** R2, R7, R10

**Dependencies:** U1, U4

**Files:**
- `src/adventure/handlers_level3.py`
- `tests/test_level3_or_guards.py`

**Approach:** Extends Level 2 with OR patterns for direction abbreviations and guards for exit validation. `case ["go", ("north"|"n"|"North") as direction]:` handles aliases. `case ["go", direction] if direction in player.current_room.exits:` validates the direction exists. `case ["go", _]:` catches invalid directions. Also add OR patterns for command synonyms: `["get"|"take"|"grab", item]`.

**Test scenarios:**
- `["go", "n"]` works same as `["go", "north"]` (alias)
- `["go", "North"]` works (case variation in OR pattern)
- `["go", "up"]` returns "You can't go that way" (invalid direction caught by guard)
- `["go", "east"]` returns specific message when east is not an exit
- `["take", "sword"]` and `["get", "sword"]` and `["grab", "sword"]` all work (command synonyms)
- Direction alias captured correctly: `"n"` maps to `"north"` in the movement logic
- Guard prevents moving to nonexistent exits even when direction matches pattern

**Verification:** All Level 3 tests pass. Aliases and guards work correctly.

---

### U6. Level 4 — Class Patterns

**Goal:** Create the Level 4 exercise module and test suite. Participants implement event dispatch using class patterns on dataclass objects.

**Requirements:** R2, R7, R10, KTD-1

**Dependencies:** U2, U5

**Files:**
- `src/adventure/handlers_level4.py`
- `tests/test_level4_class_patterns.py`

**Approach:** The handler has `handle_event(player, event) -> str`. Input is an event object (from events.py). Participants write `match event:` with class patterns: `case Click((x, y)):` → describe what's at that position, `case KeyPress("q") | KeyPress("Q"):` → quit, `case KeyPress(key) if key in "wasd":` → movement shortcuts, `case TextCommand(text):` → parse as text command (delegates to Level 3 handler), `case Quit():` → goodbye. This is where the anti-switch arc climaxes — you cannot do this with a switch statement.

**Test scenarios:**
- `Click((3, 7))` returns description of item/feature at position (3, 7)
- `Click((0, 0))` returns "Nothing interesting there" for unmapped position
- `KeyPress("q")` returns goodbye message and triggers quit
- `KeyPress("Q")` (uppercase) also triggers quit
- `KeyPress("w")` moves player north (WASD shortcut)
- `KeyPress("a")` moves player west
- `KeyPress("z")` returns "Unknown key" (not WASD or quit)
- `TextCommand("go north")` delegates to Level 3 handler and works correctly
- `Quit()` returns goodbye message
- `case Click((x, y)):` correctly extracts x and y from the position tuple

**Verification:** All Level 4 tests pass. Event dispatch works for all event types.

---

### U7. Complete Handlers Reference

**Goal:** Implement all handler functions completely (no TODOs) so the game is playable end-to-end. This serves as the solution reference and lets the game engine work for testing.

**Requirements:** R6

**Dependencies:** U2, U3, U4, U5, U6

**Files:**
- `src/adventure/handlers_complete.py`

**Approach:** Copy all handler modules and fill in every TODO with the correct implementation. The game engine can import from this module when running in "demo" mode or when participants want to see the full game in action. This file IS the solution branch content.

**Test scenarios:**
- Full game walkthrough: start → look → go north → take sword → examine sword → go south → quit
- All Level 1–4 tests pass against the complete handlers
- No TODO markers remain

**Verification:** All existing tests pass. Game is fully playable.

---

### U8. Sabotage Mode Targets

**Goal:** Create pre-written "good" match/case blocks that pairs will sabotage, and tests that should FAIL after sabotage.

**Requirements:** R3, KTD-5

**Dependencies:** U7

**Files:**
- `src/adventure/sabotage_targets.py`
- `tests/test_sabotage_examples.py`

**Approach:** Write 5 clean match/case functions, each demonstrating one anti-pattern category:
1. **Simple value check** — a 2-branch match on equality (should be `if/else`)
2. **Computable mapping** — a match that maps inputs to outputs via explicit cases (should be a formula or dict)
3. **Type dispatch** — a match that only checks types (should be `singledispatch`)
4. **Switch-on-value** — a match doing value-to-value lookup (should be `dict.get`)
5. **Unreachable case** — a match with a broad capture before a specific literal (ordering bug)

Each function has a docstring explaining what it does and a set of passing tests. After sabotage, some tests should fail (revealing bugs introduced). The facilitator guide explains each anti-pattern.

**Test scenarios:**
- All 5 sabotage targets pass their tests in the original (good) state
- Each target has at least 3 test cases covering happy path and edge cases
- Docstrings explain what the function does and which anti-pattern it relates to

**Verification:** `pytest tests/test_sabotage_examples.py` passes with good code. Tests are designed to catch common sabotage patterns.

---

### U9. Hint Branch Content

**Goal:** Create partial solutions for each level that provide hints without giving away the full answer.

**Requirements:** R5

**Dependencies:** U3, U4, U5, U6

**Files:**
- `src/adventure/handlers_level1.py` (hint version)
- `src/adventure/handlers_level2.py` (hint version)
- `src/adventure/handlers_level3.py` (hint version)
- `src/adventure/handlers_level4.py` (hint version)

**Approach:** For each level, create a hint version that:
- Implements the `match` statement structure with some cases filled in
- Leaves the key "learning" cases as TODOs
- Includes comments hinting at the pattern syntax to use
- Participants see hints via `git diff hint` — the diff shows what's added relative to starter code

This is committed on the `hint` branch. The diff between `main` and `hint` should be reviewable in under 30 seconds.

**Test scenarios:**
- Hint code is syntactically valid Python
- Hint code passes some (but not all) tests for each level
- The diff between main and hint is focused and helpful, not overwhelming

**Verification:** Hint branch exists. `git diff main..hint` shows focused, educational diffs.

---

### U10. Facilitator Guide

**Goal:** Write the comprehensive facilitator guide with timing, answer keys, pulse check answers, common struggles, and fallback plans.

**Requirements:** R8

**Dependencies:** U3, U4, U5, U6, U8

**Files:**
- `FACILITATOR_GUIDE.md`

**Approach:** The guide is a markdown document with these sections:
1. **Session overview** — timing summary, materials checklist
2. **Phase-by-phase guide** — for each of the 7 session phases:
   - Exact timing (min–max range)
   - What to say and do (facilitator script outline)
   - Predict-Then-Run answer keys (the code to show, the expected prediction, the actual result, the explanation)
   - Pulse check snippets with correct answers
3. **Common pair struggles** per level — what pairs get stuck on and the hint to give
4. **Fallback plans:**
   - Running short (add time to exercises, extend debrief)
   - Running long (cut Level 4, go from Level 3 to Sabotage Mode)
   - Mostly beginners (slow pace, more time on Levels 1–2, use full 90 min)
   - Mostly experienced (speed through Levels 1–2, add complexity to 3–4)
   - Low turnout (<8 people) — use mob format instead of pairs
   - Tech failure — backup Colab link, screenshot-based exercises
5. **Environment troubleshooting** — Python 3.10 check, common install issues
6. **Sabotage Mode anti-pattern key** — what each target demonstrates and the debrief talking points

**Test scenarios:** None — this is a documentation artifact.

**Verification:** The guide covers all 7 session phases with timing. Predict-Then-Run answer keys are complete. Fallback plans cover the scenarios in the requirements doc.

---

## Scope Boundaries

### In Scope
- Exercise repo with 4 levels + Sabotage Mode capstone
- Hint and solution git branches
- Test suite for each level
- Complete handlers reference (solution)
- Facilitator guide

### Deferred for Later
- Mapping patterns exercise (`{"key": value, **rest}`) — could be a follow-up session
- Complex nested patterns (3+ levels deep)
- `__match_args__` customization deep-dive
- Full slide deck (session uses minimal/no slides)
- Polling tool integration (Mentimeter/Slido)
- Terminal colors or ASCII map for the game

### Outside This Session
- Comparison with pattern matching in other languages
- `singledispatch` deep-dive
- Type checker integration (mypy exhaustiveness checking)

---

## Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Participants don't have Python 3.10+ | Medium | High | Provide Google Colab link as fallback; check `python --version` during mob calibration |
| Exercise levels too hard for beginners | Medium | Medium | Hint branch lets pairs self-rescue; facilitator circulates with common-struggle guide |
| Sabotage Mode produces chaotic code, not educational | Low | Medium | Pre-written sabotage targets constrain the exercise; debrief focuses on anti-patterns |
| Text adventure feels toy-like to experienced devs | Low | Low | Anti-pattern capstone provides real-world judgment practice; Level 4 events are realistic |
| Running over time | Medium | Medium | Level 4 is cuttable — skip class patterns and go straight from Level 3 to Sabotage Mode |

---

## Outstanding Questions

- **Q1 (deferred):** Terminal colors for the game output? Pure text for now; colors can be added later.
- **Q2 (deferred):** Anonymous polling for pulse checks? Show-of-hands for now; a polling tool can be added later.
