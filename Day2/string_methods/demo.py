from __future__ import annotations

from string_methods.string_utils import (
    count_character,
    ends_with,
    lowercase_text,
    replace_text,
    split_text,
    starts_with,
    strip_text,
    uppercase_text,
)


def run_string_demo() -> None:
    """Show simple string operations for beginners."""

    text = "Hello Python"
    print("Uppercase:", uppercase_text(text))
    print("Lowercase:", lowercase_text(text))
    print("Words:", split_text(text))
    print("Count of l:", count_character(text, "l"))
    print("Replaced:", replace_text(text, "Python", "World"))
    print("Trimmed:", strip_text("  Hello  "))
    print("Starts with H:", starts_with(text, "Hello"))
    print("Ends with n:", ends_with(text, "n"))
