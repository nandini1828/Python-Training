"""
utils.py

Reusable utility functions demonstrating Truthy and Falsy
concepts in Python.
"""


def is_truthy(value) -> bool:
    """
    Return True if the value is truthy.
    """
    return bool(value)


def is_falsy(value) -> bool:
    """
    Return True if the value is falsy.
    """
    return not bool(value)


def is_empty_string(value: str) -> bool:
    """
    Check whether a string is empty.
    """
    return value == ""


def is_non_empty_string(value: str) -> bool:
    """
    Check whether a string contains data.
    """
    return bool(value)


def is_empty_list(values: list) -> bool:
    """
    Check whether a list is empty.
    """
    return len(values) == 0


def is_non_empty_list(values: list) -> bool:
    """
    Check whether a list contains elements.
    """
    return len(values) > 0


def is_empty_dictionary(data: dict) -> bool:
    """
    Check whether a dictionary is empty.
    """
    return len(data) == 0


def is_non_empty_dictionary(data: dict) -> bool:
    """
    Check whether a dictionary contains items.
    """
    return len(data) > 0


def is_empty_set(values: set) -> bool:
    """
    Check whether a set is empty.
    """
    return len(values) == 0


def is_none(value) -> bool:
    """
    Check whether the value is None.
    """
    return value is None


def has_content(value) -> bool:
    """
    Check whether a value contains meaningful data.
    """
    return bool(value)


def is_zero(number: int | float) -> bool:
    """
    Check whether a number is zero.
    """
    return number == 0


def has_records(records) -> bool:
    """
    Check whether query results contain records.
    """
    return bool(records)


def is_valid_username(username: str) -> bool:
    """
    Validate username.
    """
    return bool(username.strip())


def is_valid_password(password: str) -> bool:
    """
    Validate password.
    """
    return bool(password.strip())


def is_valid_api_response(response: dict) -> bool:
    """
    Check whether an API response contains data.
    """
    return bool(response.get("data"))


def should_load_default(config) -> bool:
    """
    Return True if default configuration should be loaded.
    """
    return config is None


def cart_has_items(cart: list) -> bool:
    """
    Check whether shopping cart contains items.
    """
    return bool(cart)


def can_process_file(content: str) -> bool:
    """
    Determine whether file content exists.
    """
    return bool(content)