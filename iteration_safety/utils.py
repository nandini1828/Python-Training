"""
Utility functions for the iteration_safety package.

Author: Python Training
"""

from __future__ import annotations

from typing import Any

LINE_WIDTH = 72


def divider(character: str = "-") -> str:
    """
    Create a divider line.

    Args:
        character:
            Divider character.

    Returns:
        Divider string.
    """
    return character * LINE_WIDTH


def banner(title: str) -> str:
    """
    Create a formatted banner.

    Args:
        title:
            Banner title.

    Returns:
        Formatted banner string.
    """
    return (
        f"\n{divider('=')}\n"
        f"{title.upper():^{LINE_WIDTH}}\n"
        f"{divider('=')}"
    )


def print_banner(title: str) -> None:
    """
    Print a formatted banner.

    Args:
        title:
            Banner title.
    """
    print(banner(title))


def section(title: str) -> None:
    """
    Print a section heading.

    Args:
        title:
            Section title.
    """
    print()
    print(divider())
    print(title)
    print(divider())


def print_result(
    label: str,
    value: Any,
) -> None:
    """
    Print a formatted result.

    Args:
        label:
            Description of the result.

        value:
            Value to display.
    """
    print(f"{label:<35}: {value}")


def print_collection(
    title: str,
    collection: list[Any],
) -> None:
    """
    Print a collection.

    Args:
        title:
            Collection title.

        collection:
            Collection values.
    """
    print(title)

    for item in collection:
        print(f"  • {item}")

    print()


def print_dictionary(
    title: str,
    data: dict[Any, Any],
) -> None:
    """
    Print a dictionary.

    Args:
        title:
            Dictionary title.

        data:
            Dictionary to display.
    """
    print(title)

    for key, value in data.items():
        print(f"  {key}: {value}")

    print()


def print_set(
    title: str,
    values: set[Any],
) -> None:
    """
    Print a set.

    Args:
        title:
            Set title.

        values:
            Set values.
    """
    print(title)

    for value in sorted(values, key=str):
        print(f"  • {value}")

    print()


def print_comparison(
    title: str,
    original: Any,
    modified: Any,
) -> None:
    """
    Print original and modified values.

    Args:
        title:
            Comparison title.

        original:
            Original value.

        modified:
            Modified value.
    """
    print(title)
    print(f"Original : {original}")
    print(f"Modified : {modified}")
    print()