"""
Tests for break_continue.py
"""

from loops import BreakContinueExamples


def test_break_example():
    assert (
        BreakContinueExamples.break_example(
            [10, 20, 30],
            20
        )
        == "20 Found"
    )


def test_stop_at_five():
    assert (
        BreakContinueExamples.stop_at_five()
        == [1, 2, 3, 4]
    )


def test_continue_example():
    assert (
        BreakContinueExamples.continue_example(
            [1, 2, 3, 4, 5, 6]
        )
        == [1, 3, 5]
    )


def test_skip_empty_strings():
    assert (
        BreakContinueExamples.skip_empty_strings(
            ["Python", "", "AI"]
        )
        == ["Python", "AI"]
    )