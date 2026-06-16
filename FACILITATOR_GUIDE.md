# Facilitator Guide: Pattern Matching Workshop

## Session Overview

| Phase | Activity | Time |
|-------|----------|------|
| 1 | Hook + Calibrate | 10 min |
| 2 | Level 1: Literal & Wildcard | 10 min |
| 3 | Level 2: Capture & Sequence | 12 min |
| 4 | Level 3: OR Patterns & Guards | 12 min |
| 5 | Level 4: Class Patterns | 15 min |
| 6 | Capstone: Sabotage Mode | 15 min |
| 7 | Wrap-up | 5 min |
| **Total** | | **~79 min** |

**Materials needed:**
- Projector + screen
- Participants bring laptops with Python 3.10+ (or Google Colab backup)
- Participants clone the exercise repo
- Sticky notes or shared doc for debrief
- Timer (phone is fine)

**Repo setup:**
```
git clone <repo-url>
cd pattern_matching
uv sync
uv run pytest  # verify environment
```

---

## Phase 1: Hook + Calibrate (10 min)

### Anti-Switch Poll (1 min)

**Say:** "How many of you think Python's `match`/`case` is a switch statement? Raise your hand."

**Say:** "Great — forget that. It's not a switch statement. By the end of tonight, you'll understand why. And it's going to be fun."

### The Unpacking Frame (3 min)

**Show on screen:**
```python
first, *rest = [1, 2, 3]
```

**Ask pairs:** "What does `first` hold? What does `rest` hold?"

**Reveal:** `first = 1`, `rest = [2, 3]`

**Say:** "Pattern matching is *this operation generalized*. Variables are assignment targets, not comparisons. `case direction:` BINDS a variable — it doesn't check if direction equals something. This one idea explains everything tonight."

### Mob Calibration (6 min)

**Say:** "Let's solve the first puzzle together. I'll navigate, I need a volunteer to type."

1. Open `src/adventure/handlers_level1.py`
2. Show the `pass` statement
3. Guide the volunteer to write:
   ```python
   match command:
       case "quit":
           player.running = False
           return "Goodbye!"
       case _:
           return "I don't understand that command."
   ```
4. Run `uv run pytest tests/test_level1_literal_wildcard.py::TestQuitCommand -v`
5. Show it passes

**Say:** "Great — now break into pairs. One person is the Navigator (decides WHAT to type), the other is the Driver (types it). The Navigator cannot touch the keyboard. Swap roles at each level."

**Read the room:**
- If most people struggled with the mob → slow down, spend more time on Levels 1–2
- If people breezed through → speed up, add complexity hints
- If someone can't run Python → point them to the Colab backup

---

## Phase 2: Level 1 — Literal & Wildcard (10 min)

### Predict-Then-Run Cycle (5 min)

**Show on screen:**
```python
match command:
    case "quit":
        return "Goodbye!"
    case "look":
        return player.current_room.look()
    case _:
        return "I don't understand that command."
```

**Ask pairs to predict (30 seconds each):**
1. What does `handle_command(player, "look")` return?
2. What does `handle_command(player, "LOOK")` return?
3. What does `handle_command(player, "fly")` return?

**Reveal answers:**
1. The room description ✓
2. "I don't understand that command." (case-sensitive!)
3. "I don't understand that command." ✓

**Say:** "The case-sensitivity surprise is your first `aha` moment. Pattern matching compares exact values — 'LOOK' ≠ 'look'. Remember this when we get to capture patterns."

### Pair Exercise (5 min)

**Task:** Complete Level 1 by adding cases for "help" and "inventory".

**Test:** `uv run pytest tests/test_level1_literal_wildcard.py -v`

### Common Struggles

| Struggle | Hint |
|----------|------|
| "What do I return for help?" | Any text listing the commands is fine — there's no single right answer |
| Tests still fail after writing code | Make sure you have a `match command:` not `match words:` |
| "inventory test fails" | Use `player.show_inventory()` — it handles the empty case |

---

## Phase 3: Level 2 — Capture & Sequence (12 min)

### Predict-Then-Run Cycle (5 min)

**Show on screen:**
```python
command = "go north".split()  # → ["go", "north"]

match command:
    case ["go", direction]:
        print(direction)
```

**Ask pairs to predict:**
1. What is `direction`? → `"north"`
2. What happens for `"go".split()` (just `["go"]`)? → No match, falls through
3. What happens for `"go north east".split()` (3 elements)? → No match — the pattern expects exactly 2

**Say:** "This is the moment where switch thinking BREAKS. A switch matches on a single value. Pattern matching DESTRUCTURES sequences. `direction` is an assignment target, just like `first` in `first, *rest = [1, 2, 3]`."

**The big reveal:** "`direction` doesn't compare to anything — it BINDS a new variable. This is unpacking, not switching."

### Pair Exercise (7 min)

**Task:** Complete Level 2 by adding cases for `["go", direction]`, `["take", item]`, and `["examine", target]`.

**Test:** `uv run pytest tests/test_level2_capture_sequence.py -v`

### Common Struggles

| Struggle | Hint |
|----------|------|
| "How do I move the player?" | `player.move(direction)` returns `True`/`False` — if `True`, `return player.current_room.look()`; else `f"You can't go {direction}."` |
| "take doesn't work" | Remember to remove the item from the room AND add to inventory |
| "examine can't find items I'm carrying" | Check both `player.current_room.items` and `player.inventory` |
| "go with extra words fails" | That's correct! `case ["go", direction]:` only matches 2-element lists |

### Pulse Check (60 seconds)

**Show on screen:**
```python
match ["take", "sword", "of", "doom"]:
    case ["take", item]:
        print(f"Taking {item}")
    case _:
        print("Unknown")
```

**Ask:** "What prints?" → "Unknown" (4 elements, pattern expects 2)

---

## Phase 4: Level 3 — OR Patterns & Guards (12 min)

### Predict-Then-Run Cycle (4 min)

**Show on screen:**
```python
match words:
    case ["go", ("north" | "n") as direction]:
        move(direction)
    case ["go", direction] if direction in player.current_room.exits:
        move(direction)
    case ["go", _]:
        return "You can't go that way."
```

**Ask pairs to predict:**
1. What does `direction` hold for `["go", "n"]`? → `"n"` (the original value, use a map to normalize)
2. What happens for `["go", "west"]` when there's no west exit? → "You can't go that way."
3. What happens for `["go", "up"]`? → "You can't go that way." (guard fails, falls to wildcard)

### Pair Exercise (8 min)

**Task:** Complete Level 3 — add OR patterns for all 4 direction aliases, guards for exit validation, and command synonyms.

**Test:** `uv run pytest tests/test_level3_or_guards.py -v`

### Common Struggles

| Struggle | Hint |
|----------|------|
| "Direction alias works but player goes to wrong room" | You need to normalize: `"n"` → `"north"` using a dict |
| "The guard doesn't work" | Guards come AFTER the pattern: `case ["go", direction] if ...` |
| "Order matters?" | Yes! Put specific OR patterns before the general guarded case |
| "get/take/grab OR pattern syntax error" | It's `case ["get" \| "take" \| "grab", item_name]:` |

---

## Phase 5: Level 4 — Class Patterns (15 min)

### Predict-Then-Run Cycle (5 min)

**Show on screen:**
```python
match event:
    case Click((x, y)):
        print(f"Clicked at {x}, {y}")
    case KeyPress("q") | KeyPress("Q"):
        print("Quit!")
    case KeyPress(key) if key in "wasd":
        print(f"Move: {key}")
```

**Ask pairs to predict:**
1. What are `x` and `y` for `Click((3, 7))`? → `3` and `7`
2. Does `KeyPress("q")` match the OR pattern? → Yes
3. Does `KeyPress("w")` match the guarded case? → Yes (`"w" in "wasd"` is True)
4. What does `Quit()` look like in a case? → `case Quit():` (no args)

**Say:** "This is where switch thinking is IMPOSSIBLE. You cannot switch on an object's type AND extract its attributes in one expression. `case Click((x, y)):` does `isinstance(event, Click)` AND `(x, y) = event.position` in one line."

### Pair Exercise (10 min)

**Task:** Complete Level 4 — handle Click, KeyPress (quit/WASD/unknown), TextCommand, and Quit events.

**Test:** `uv run pytest tests/test_level4_class_patterns.py -v`

### Common Struggles

| Struggle | Hint |
|----------|------|
| "Click((x, y)) doesn't extract" | Check `events.py` — `Click.__match_args__ = ("position",)` enables positional matching |
| "KeyPress doesn't match" | Make sure you import `KeyPress` from `adventure.events` |
| "TextCommand delegation fails" | Split the text: `text.strip().split()`, then call level3 handler |
| "WASD doesn't move" | Map keys: `{"w": "north", "a": "west", "s": "south", "d": "east"}` |

### Pulse Check

**Show on screen:**
```python
match KeyPress("w"):
    case KeyPress("q") | KeyPress("Q"):
        print("quit")
    case KeyPress(key) if key in "wasd":
        print(f"move {key}")
    case KeyPress(key):
        print(f"unknown: {key}")
```

**Ask:** "What prints?" → "move w"

**Follow-up:** "What if we swap the `if key in "wasd"` guard to `if key in "wasdq"`?" → Still "move w" (comes before the quit OR pattern? No — wait, `KeyPress("q") | KeyPress("Q")` comes FIRST in the match. So `q` still quits. But if someone types a different letter that's in both... actually `"wasdq"` would make `q` match the WASD case. Order matters!)

---

## Phase 6: Capstone — Sabotage Mode (15 min)

### Setup (2 min)

**Say:** "Now for the fun part. You know HOW to use match/case. Let's learn WHEN NOT TO."

**Instructions:**
1. Open `src/adventure/sabotage_targets.py` — read all 5 functions
2. Pick ONE function with your pair
3. SABOTAGE it — make it confusing, fragile, or buggy. NO syntax errors.
4. Swap your sabotaged code with another pair
5. Diagnose and fix the other pair's sabotage
6. We'll debrief as a group

### Sabotage Time (3 min)

Circulate. Encourage creative sabotage. Good sabotage techniques:
- Reorder cases so a broad pattern eats a specific one
- Add guards that are always True (or always False)
- Change a literal to a capture (e.g., `case "quit":` → `case command:`)
- Remove the wildcard case entirely

### Diagnosis Time (6 min)

Pairs swap and diagnose. Circulate and help pairs that are stuck.

### Group Debrief (4 min)

**Ask each pair:** "What anti-pattern did you find? What was wrong with it?"

**Build the anti-pattern list on the board:**

1. **Simple if/else** — 2 branches on equality → just use `if/else`
2. **Computable mapping** — explicit cases for what a formula can compute
3. **Type dispatch only** — just checking types → use `singledispatch`
4. **Switch on value** — value-to-value lookup → use `dict.get()`
5. **Unreachable case** — broad capture before specific literal → ordering bug

**Say:** "The best pattern matching code is code that DOESN'T use pattern matching — when something simpler would do. Match/case is for structural destructuring, not for simple value dispatch."

---

## Phase 7: Wrap-Up (5 min)

### Participant Takeaways (2 min)

**Say:** "Quick — each person, what's the ONE thing that surprised you most tonight?"

Take 4-5 responses. Validate each one.

### The Unpacking Frame Recap (1 min)

**Say:** "Remember the one question that answers everything: **'What would unpacking do here?'** If you're not sure what a pattern does, think about iterable unpacking. Variables are assignment targets. `_` is the wildcard. First match wins."

### Resources (1 min)

- PEP 636 tutorial: https://peps.python.org/pep-0636/
- Ben Hoyt's article: https://benhoyt.com/writings/python-pattern-matching/
- This exercise repo — keep practicing!
- Brett Slatkin's PyBeach 2025 talk (YouTube)

### The Closing Question (30 seconds)

**Say:** "What would you have missed if you kept calling this a switch statement?"

**Answer:** Everything. Destructuring, capture semantics, class patterns, guards, the whole point.

---

## Fallback Plans

### Running Short (< 70 min)

- Extend pair exercise time at each level
- Add more time to Sabotage Mode debrief
- Do a second round of sabotage (swap again)
- Run a live Q&A

### Running Long (> 85 min)

- **Cut Level 4** (class patterns). Go straight from Level 3 to Sabotage Mode.
- Reduce Predict-Then-Run cycles to 1-2 predictions instead of 3
- Shorten the wrap-up

### Mostly Beginners

- Slow pace through Levels 1–2
- Use the full 90 minutes
- Encourage the hint branch: `git stash && git checkout hint && git diff`
- Spend more time on mob calibration

### Mostly Experienced

- Speed through Levels 1–2 (they'll get it fast)
- Spend more time on Level 4 class patterns
- Add a bonus: mapping patterns (`case {"key": value, **rest}:`)
- Make Sabotage Mode harder — require pairs to sabotage TWO functions

### Low Turnout (< 8 people)

- Use mob programming for the entire session instead of pairs
- Facilitator navigates, each person drives for 5-7 minutes
- Skip the Sabotage Mode swap — mob does the sabotaging together

### Tech Failure

- **No Python 3.10+** → Google Colab link with the repo pre-loaded
- **Can't clone repo** → USB stick with the code
- **No internet** → Pre-download everything, have screenshots of the Predict-Then-Run snippets
- **Projector fails** → Print the Predict-Then-Run snippets as handouts

---

## Environment Troubleshooting

### Quick Check

```bash
python --version  # Must be 3.10 or higher
uv run pytest tests/test_game.py -v  # All should pass — this tests the game model, not the exercises
```

### Common Issues

| Issue | Fix |
|-------|-----|
| `python --version` shows 3.9 | Install 3.10+ or use Colab |
| `uv: command not found` | `pip install uv` or use `python -m pytest` instead |
| `ModuleNotFoundError: adventure` | Run from the repo root, not from inside `src/` |
| Tests import but fail with `NoneType` | The `pass` statement returns None — that's the TODO |
| `SyntaxError: invalid syntax` on `match` | Python version is < 3.10 — upgrade or use Colab |

### Google Colab Backup

Provide a Colab notebook that:
1. Clones the repo
2. Installs pytest
3. Runs the Level 1 tests
4. Has a code cell for each handler level

---

## Sabotage Mode Anti-Pattern Key

| # | Function | Anti-Pattern | When to use instead |
|---|----------|-------------|-------------------|
| 1 | `simple_value_check` | Simple if/else replacement | Use `if/else` for 2-branch equality checks |
| 2 | `computable_mapping` | Computable result via cases | Use a formula or computation instead of lookup |
| 3 | `type_dispatch` | Type-only dispatch | Use `functools.singledispatch` |
| 4 | `switch_on_value` | Value-to-value mapping | Use `dict.get()` — it's shorter and faster |
| 5 | `unreachable_case` | Ordering bug | Always put specific patterns before broad ones |
