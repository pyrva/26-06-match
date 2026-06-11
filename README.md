# PyRVA Pattern Matching Workshop

An interactive workshop on Python structural pattern matching (3.10+), built around a text adventure game.

## Quick Start

```bash
# Install dependencies
uv sync

# Run all tests (21 pass = game model, 54 fail = exercise TODOs)
uv run pytest

# Run a specific level's tests
uv run pytest tests/test_level1_literal_wildcard.py -v
```

## Exercise Levels

| Level | File | Pattern Types | Concepts |
|-------|------|---------------|----------|
| 1 | `handlers_level1.py` | Literal, wildcard | `case "quit":`, `case _:` |
| 2 | `handlers_level2.py` | Capture, sequence | `case ["go", direction]:` |
| 3 | `handlers_level3.py` | OR patterns, guards | `case ["go", ("n"|"north") as dir]:`, `case [...] if ...:` |
| 4 | `handlers_level4.py` | Class patterns | `case Click((x, y)):` |
| Capstone | `sabotage_targets.py` | Anti-patterns | When NOT to use match/case |

## Difficulty Tiers

- **Apprentice** — Levels 1–2 (literal matching, capture patterns)
- **Journeyer** — Levels 3–4 (OR patterns, guards, class patterns)
- **Artisan** — Level 4 + advanced variants + Sabotage Mode

## Getting Hints

```bash
# See partial solutions
git stash
git checkout hint
git diff main..hint
git checkout main
git stash pop
```

## Running the Game

```bash
# Run with complete handlers (see the full game in action)
uv run python -m adventure
```

## Files

- `FACILITATOR_GUIDE.md` — Full session plan with timing, answer keys, and fallback plans
- `src/adventure/game.py` — Game engine (Room, Item, Player)
- `src/adventure/events.py` — Event dataclasses for Level 4
- `src/adventure/handlers_levelN.py` — Exercise files with TODO markers
- `src/adventure/handlers_complete.py` — Full solution reference
- `src/adventure/sabotage_targets.py` — Sabotage Mode exercise targets
