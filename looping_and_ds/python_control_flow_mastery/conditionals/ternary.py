"""
Ternary operator examples.
"""


def get_voting_status(age: int) -> str:
    """
    Returns Eligible if age >= 18 else Not Eligible.
    """
    return "Eligible" if age >= 18 else "Not Eligible"


def get_parity(number: int) -> str:
    """
    Returns Even if number is divisible by 2, otherwise Odd.
    """
    return "Even" if number % 2 == 0 else "Odd"