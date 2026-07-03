"""
pass statement examples.
"""


def pass_in_loop_demo() -> str:
    """
    Demonstrates pass inside a loop.
    """
    for _ in range(3):
        pass

    return "pass used inside loop"


def pass_in_condition_demo(number: int) -> str:
    """
    Demonstrates pass inside a condition block.
    """
    if number > 0:
        pass

    return "pass used inside condition"