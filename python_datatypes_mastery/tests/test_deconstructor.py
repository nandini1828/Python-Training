"""Tests for deconstruct_object behavior."""
from dataclasses import dataclass

from python_datatypes_mastery.classes.object_deconstructor import deconstruct_object


def test_deconstruct_primitives():
    assert deconstruct_object(1) == 1
    assert deconstruct_object("s") == "s"


def test_deconstruct_nested():
    @dataclass
    class Inner:
        x: int

    @dataclass
    class Outer:
        inner: Inner
        items: list

    o = Outer(Inner(5), [1, 2, {"a": 3}])
    result = deconstruct_object(o)
    assert isinstance(result, dict)
    assert result["inner"]["x"] == 5
    assert result["items"][2]["a"] == 3
