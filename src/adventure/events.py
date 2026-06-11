"""Event dataclasses for Level 4 — class pattern matching exercises.

These represent the different types of input events the game can receive.
Participants will use class patterns to match and dispatch these events.

    match event:
        case Click((x, y)): ...
        case KeyPress("q") | KeyPress("Q"): ...
        case KeyPress(key) if key in "wasd": ...
        case TextCommand(text): ...
        case Quit(): ...
"""

from __future__ import annotations


class Click:
    """A mouse click at a position in the game window.

    Supports positional matching via __match_args__:
        case Click((x, y)):   # extracts x and y from position
    """

    __match_args__ = ("position",)

    def __init__(self, position: tuple[int, int]) -> None:
        self.position = position

    def __repr__(self) -> str:
        return f"Click(position={self.position!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Click):
            return NotImplemented
        return self.position == other.position


class KeyPress:
    """A keyboard key press.

    Supports positional matching via __match_args__:
        case KeyPress("q"):        # matches specific key
        case KeyPress(key):        # captures key into variable
    """

    __match_args__ = ("key",)

    def __init__(self, key: str) -> None:
        self.key = key

    def __repr__(self) -> str:
        return f"KeyPress(key={self.key!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, KeyPress):
            return NotImplemented
        return self.key == other.key


class Quit:
    """A quit event (no attributes).

    Matching:
        case Quit():   # matches any Quit event
    """

    def __repr__(self) -> str:
        return "Quit()"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Quit):
            return NotImplemented
        return True


class TextCommand:
    """A text command entered by the player.

    Supports positional matching via __match_args__:
        case TextCommand(text):   # captures the text for further parsing
    """

    __match_args__ = ("text",)

    def __init__(self, text: str) -> None:
        self.text = text

    def __repr__(self) -> str:
        return f"TextCommand(text={self.text!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TextCommand):
            return NotImplemented
        return self.text == other.text
