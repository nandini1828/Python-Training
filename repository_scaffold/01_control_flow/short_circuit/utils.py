"""
utils.py

Reusable utility functions demonstrating Python's
short-circuit evaluation.

These functions are designed to showcase how Python's
`and` and `or` operators stop evaluating expressions
once the final outcome is determined.
"""


def safe_division(numerator: float, denominator: float):
    """
    Safely divide two numbers.

    Returns None if the denominator is zero.
    """
    return denominator != 0 and numerator / denominator


def get_display_name(username: str) -> str:
    """
    Return the username if available,
    otherwise return 'Guest'.
    """
    return username or "Guest"


def authenticate(username: str, password: str) -> bool:
    """
    Authenticate a user.

    Returns True only if both username
    and password are provided.
    """
    return bool(username and password)


def get_user_name(response: dict):
    """
    Safely retrieve the user's name
    from an API response.
    """
    return (
        response
        and response.get("data")
        and response["data"].get("name")
    )


def load_configuration(user_config):
    """
    Return the user configuration if available;
    otherwise return the default configuration.
    """
    return user_config or "Default Configuration"


def cart_has_items(cart: list) -> bool:
    """
    Check whether the shopping cart
    contains any items.
    """
    return bool(cart and len(cart) > 0)


def get_file_content(content: str) -> str:
    """
    Return file content if present;
    otherwise return backup content.
    """
    return content or "Using Backup File"


def can_access_system(is_employee: bool, has_id: bool) -> bool:
    """
    Determine whether an employee
    can access the system.
    """
    return is_employee and has_id


def get_cached_value(cache: dict, key: str):
    """
    Return a cached value if present;
    otherwise return a message indicating
    that the value should be fetched.
    """
    return cache.get(key) or "Fetching from Database..."


def validate_age(age: int) -> bool:
    """
    Validate whether a person's age
    falls within the eligible range.
    """
    return age >= 18 and age < 60