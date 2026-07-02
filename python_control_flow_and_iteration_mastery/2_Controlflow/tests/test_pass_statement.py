"""
Tests for pass_statement.py
"""

from loops import PassExamples


def test_empty_if():
    assert (
        PassExamples.empty_if(10)
        == "Execution Completed"
    )


def test_empty_loop():
    assert (
        PassExamples.empty_loop(5)
        == "Loop Completed"
    )


def test_skip_even_numbers():
    assert (
        PassExamples.skip_even_numbers(
            [1, 2, 3]
        )
        == [1, 2, 3]
    )


def test_placeholder_function():
    assert (
        PassExamples.placeholder_function()
        == "Placeholder Function"
    )