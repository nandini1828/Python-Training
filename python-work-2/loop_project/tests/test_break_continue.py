from loops.break_continue_pass import (
    break_demo,
    continue_demo,
    pass_demo,
)


def test_break_demo():

    expected = [0, 1, 2, 3, 4]

    assert break_demo(5) == expected


def test_continue_demo():

    expected = [1, 3, 5, 7, 9]

    assert continue_demo(10) == expected


def test_pass_demo():

    assert pass_demo(3) == "Loop finished"