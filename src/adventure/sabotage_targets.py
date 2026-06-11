"""Sabotage Mode targets — well-written match/case blocks for pairs to sabotage.

HOW THIS WORKS:
1. Read each function below — they are all correct, well-written match/case code.
2. Your pair's job: SABOTAGE one of these functions. Make it as confusing,
   fragile, or buggy as possible — WITHOUT introducing syntax errors.
   (The code must still be valid Python that runs, just does the wrong thing.)
3. Swap your sabotaged code with another pair.
4. The other pair must diagnose and FIX the sabotage.

ANTI-PATTERN CATEGORIES (each function demonstrates one):
1. simple_value_check  — A match that should be a plain if/else (2 branches, simple equality)
2. computable_mapping  — A match doing explicit lookup instead of a formula
3. type_dispatch       — A match that only checks types (singledispatch would be better)
4. switch_on_value     — A match doing value-to-value lookup (dict.get would be better)
5. unreachable_case    — A match with a broad capture BEFORE a specific literal (ordering bug)
"""


def simple_value_check(light_level: int) -> str:
    """Determine if it's dark or light based on a threshold.

    ANTI-PATTERN: When you only have 2 branches and simple equality/comparison,
    a plain if/else is cleaner. match/case adds a nesting level for no benefit.

    SABOTAGE IDEAS: Add unnecessary cases, reorder them, add guards that
    are always true, use capture patterns where literals would be clearer...
    """
    match light_level:
        case level if level > 50:
            return "bright"
        case _:
            return "dark"


def computable_mapping(dice: tuple[int, int]) -> str:
    """Describe a dice roll result.

    ANTI-PATTERN: The result is computable from the inputs — you don't need
    a match at all. sum(dice) >= 10 would be simpler. But the match is
    readable, so this is a judgment call.

    SABOTAGE IDEAS: Make the conditions overlap, remove cases so some inputs
    fall through to the wildcard incorrectly, add contradictory guards...
    """
    match dice:
        case (a, b) if a == b and a == 6:
            return "double six — critical hit!"
        case (a, b) if a == b:
            return f"doubles — roll again"
        case (a, b) if a + b >= 10:
            return "high roll — great success!"
        case _:
            return "normal roll"


def type_dispatch(value: object) -> str:
    """Describe the type of a value.

    ANTI-PATTERN: When you only need to dispatch on type and call a function,
    functools.singledispatch is the standard Python tool. match/case works
    but doesn't compose as well with the rest of the Python ecosystem.

    SABOTAGE IDEAS: Make the type checks overlap, reorder so str catches
    before int when both are present, add unnecessary isinstance guards...
    """
    match value:
        case bool():
            return f"boolean: {value}"
        case int():
            return f"integer: {value}"
        case float():
            return f"float: {value:.2f}"
        case str():
            return f"string: {value!r}"
        case list():
            return f"list of {len(value)} items"
        case _:
            return f"unknown type: {type(value).__name__}"


def switch_on_value(command: str) -> str:
    """Map a command string to a response — pure value lookup.

    ANTI-PATTERN: This is the most common misuse of match/case. When you're
    doing simple value-to-value mapping, dict.get() is shorter, faster, and
    more Pythonic. match/case here is just a verbose dictionary.

    SABOTAGE IDEAS: Reorder cases so a specific match comes after the
    wildcard, add unnecessary guards, duplicate cases...
    """
    responses = {
        "hello": "Hi there!",
        "bye": "See you later!",
        "help": "Ask me anything.",
        "status": "All systems operational.",
    }
    match command:
        case "hello":
            return "Hi there!"
        case "bye":
            return "See you later!"
        case "help":
            return "Ask me anything."
        case "status":
            return "All systems operational."
        case _:
            return "I don't know that command."


def unreachable_case(command: list[str]) -> str:
    """Handle adventure commands — but watch out for ordering bugs!

    ANTI-PATTERN: The broad capture `case [action]:` comes BEFORE the
    specific `case ["go", direction]:`. Since pattern matching evaluates
    top-to-bottom and the first match wins, ["go"] will match the broad
    capture and the specific case will NEVER be reached.

    WAIT — this function is actually CORRECT. Can you see why the ordering
    works here? (Hint: the first case matches exactly 1-element lists,
    while the second matches 2-element lists — they don't overlap!)

    SABOTAGE IDEAS: Reorder the cases so the broad capture DOES come first,
    add a case ["go", direction] before the specific case but with a guard
    that's always true, make the wildcard catch things it shouldn't...
    """
    match command:
        case [action]:
            return f"Single command: {action}"
        case ["go", direction]:
            return f"Going {direction}!"
        case ["take", item]:
            return f"Taking {item}!"
        case _:
            return "Unknown command."
