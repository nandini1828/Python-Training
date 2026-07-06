"""
Examples demonstrating Python's short-circuit evaluation.

Short-circuit evaluation allows Python to stop evaluating an expression
as soon as the final result is known.

Topics covered:
- and short-circuit
- or short-circuit
- Lazy evaluation
- Safe attribute access
- Default values
- Cache lookup
- Configuration loading

Author: Python Training
"""

from __future__ import annotations

from typing import Any


def expensive_database_call() -> str:
    """
    Simulate an expensive database operation.

    Returns:
        Database result.
    """
    return "Database Result"


def cached_value_example(cached_value: str | None) -> str:
    """
    Return a cached value if available.

    Demonstrates the 'or' short-circuit operator.

    Args:
        cached_value:
            Cached value.

    Returns:
        Cached value or database result.
    """
    return cached_value or expensive_database_call()


def get_cached_value(
    cached_value: Any,
    fallback: Any,
) -> Any:
    """
    Return the cached value if it exists.

    Args:
        cached_value:
            Cached object.
        fallback:
            Fallback value.

    Returns:
        Cached value or fallback.
    """
    return cached_value or fallback


def is_authorized(
    is_logged_in: bool,
    is_admin: bool,
) -> bool:
    """
    Check administrative access.

    The second condition is evaluated only if the
    first condition is True.

    Args:
        is_logged_in:
            Authentication status.
        is_admin:
            Administrative privilege.

    Returns:
        True if authorized.
    """
    return is_logged_in and is_admin


def safe_upper(text: str | None) -> str:
    """
    Safely convert text to uppercase.

    Args:
        text:
            Input text.

    Returns:
        Uppercase string or empty string.
    """
    return text and text.upper() or ""


def safe_length(collection: list[Any] | None) -> int:
    """
    Safely calculate collection length.

    Args:
        collection:
            Input collection.

    Returns:
        Length of the collection.
    """
    return collection and len(collection) or 0


def get_username(
    username: str | None,
) -> str:
    """
    Return a default username.

    Args:
        username:
            User name.

    Returns:
        Username or Guest.
    """
    return username or "Guest"


def get_configuration(
    env_value: str | None,
    config_file_value: str | None,
    default_value: str,
) -> str:
    """
    Return the first available configuration.

    Priority:
        Environment
        Configuration file
        Default

    Args:
        env_value:
            Environment variable.

        config_file_value:
            Configuration file value.

        default_value:
            Default configuration.

    Returns:
        Selected configuration.
    """
    return env_value or config_file_value or default_value


def validate_user(
    username: str,
    password: str,
) -> bool:
    """
    Demonstrate short-circuit evaluation.

    Password comparison occurs only if the username matches.

    Args:
        username:
            Username.

        password:
            Password.

    Returns:
        Authentication result.
    """
    return username == "admin" and password == "python123"


def should_process(
    data: list[Any] | None,
) -> bool:
    """
    Determine whether data should be processed.

    Args:
        data:
            Input data.

    Returns:
        True if data exists.
    """
    return bool(data and len(data) > 0)


def first_non_empty(*values: Any) -> Any:
    """
    Return the first truthy value.

    Args:
        *values:
            Candidate values.

    Returns:
        First truthy value or None.
    """
    for value in values:
        if value:
            return value

    return None


def has_permission(
    is_admin: bool,
    permissions: set[str],
) -> bool:
    """
    Determine whether write access exists.

    Args:
        is_admin:
            Administrator status.

        permissions:
            Assigned permissions.

    Returns:
        True if access is granted.
    """
    return is_admin or "write" in permissions


def get_nested_value(
    data: dict[str, Any] | None,
    key: str,
) -> Any:
    """
    Safely retrieve a dictionary value.

    Args:
        data:
            Dictionary object.

        key:
            Dictionary key.

    Returns:
        Dictionary value or None.
    """
    return data and data.get(key)


def email_domain(
    email: str | None,
) -> str | None:
    """
    Safely retrieve an email domain.

    Args:
        email:
            Email address.

    Returns:
        Domain name or None.
    """
    return email and email.split("@")[-1]


def positive_number(
    number: int,
) -> bool:
    """
    Determine whether a number is positive.

    Args:
        number:
            Integer value.

    Returns:
        True if positive.
    """
    return number > 0


def is_even(
    number: int,
) -> bool:
    """
    Determine whether a number is even.

    Args:
        number:
            Integer value.

    Returns:
        True if even.
    """
    return number % 2 == 0


def positive_even_number(
    number: int,
) -> bool:
    """
    Demonstrate 'and' short-circuit evaluation.

    Args:
        number:
            Integer value.

    Returns:
        True if positive and even.
    """
    return positive_number(number) and is_even(number)


__all__ = [
    "expensive_database_call",
    "cached_value_example",
    "get_cached_value",
    "is_authorized",
    "safe_upper",
    "safe_length",
    "get_username",
    "get_configuration",
    "validate_user",
    "should_process",
    "first_non_empty",
    "has_permission",
    "get_nested_value",
    "email_domain",
    "positive_number",
    "is_even",
    "positive_even_number",
]