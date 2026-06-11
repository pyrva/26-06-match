"""Tests for sabotage targets — these should all PASS with the good code.

After sabotage, some of these tests should FAIL, revealing the bugs
that pairs introduced.
"""

from adventure.sabotage_targets import (
    computable_mapping,
    simple_value_check,
    switch_on_value,
    type_dispatch,
    unreachable_case,
)


class TestSimpleValueCheck:
    def test_bright(self):
        assert simple_value_check(75) == "bright"

    def test_dark(self):
        assert simple_value_check(25) == "dark"

    def test_boundary_bright(self):
        assert simple_value_check(51) == "bright"

    def test_boundary_dark(self):
        assert simple_value_check(50) == "dark"

    def test_zero(self):
        assert simple_value_check(0) == "dark"

    def test_hundred(self):
        assert simple_value_check(100) == "bright"


class TestComputableMapping:
    def test_double_six(self):
        assert computable_mapping((6, 6)) == "double six — critical hit!"

    def test_doubles(self):
        assert "doubles" in computable_mapping((3, 3))

    def test_high_roll(self):
        assert "high roll" in computable_mapping((6, 4))

    def test_normal_roll(self):
        assert "normal roll" in computable_mapping((2, 3))

    def test_low_doubles(self):
        """Doubles (1,1) is still doubles, not a normal roll."""
        assert "doubles" in computable_mapping((1, 1))


class TestTypeDispatch:
    def test_int(self):
        assert type_dispatch(42) == "integer: 42"

    def test_float(self):
        assert "float" in type_dispatch(3.14)

    def test_str(self):
        assert type_dispatch("hello") == "string: 'hello'"

    def test_bool(self):
        assert type_dispatch(True) == "boolean: True"

    def test_list(self):
        assert "list of 3 items" in type_dispatch([1, 2, 3])

    def test_unknown_type(self):
        assert "unknown" in type_dispatch({"key": "value"})


class TestSwitchOnValue:
    def test_hello(self):
        assert switch_on_value("hello") == "Hi there!"

    def test_bye(self):
        assert switch_on_value("bye") == "See you later!"

    def test_help(self):
        assert switch_on_value("help") == "Ask me anything."

    def test_status(self):
        assert switch_on_value("status") == "All systems operational."

    def test_unknown(self):
        assert "don't know" in switch_on_value("dance")


class TestUnreachableCase:
    def test_single_command(self):
        assert unreachable_case(["look"]) == "Single command: look"

    def test_go_command(self):
        assert unreachable_case(["go", "north"]) == "Going north!"

    def test_take_command(self):
        assert unreachable_case(["take", "sword"]) == "Taking sword!"

    def test_unknown_command(self):
        assert unreachable_case(["fly", "up"]) == "Unknown command."

    def test_go_with_no_direction(self):
        """["go"] is a 1-element list — matches the first case."""
        assert unreachable_case(["go"]) == "Single command: go"
