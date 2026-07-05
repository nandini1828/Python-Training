"""
Examples of Truthy and Falsy values.
"""


def cart_status(cart: list) -> str:
    """Check shopping cart."""
    if cart:
        return "Items Available"
    return "Cart Empty"


def username_exists(username: str) -> bool:
    """Check username."""
    return bool(username)


def check_dictionary(data: dict) -> str:
    """Check dictionary."""
    if data:
        return "Dictionary Contains Data"
    return "Dictionary Empty"


def number_status(number: int) -> str:
    """Check integer."""
    if number:
        return "Non-zero"
    return "Zero"


def profile(profile_data: dict) -> bool:
    """Profile exists."""
    return bool(profile_data)