"""
Utility functions for the loop_foundations module.

Author: Python Training
"""

from __future__ import annotations

from typing import Any

SECTION_WIDTH = 70


def divider(character: str = "-") -> str:
    """
    Return a divider string.

    Args:
        character:
            Divider character.

    Returns:
        Divider.
    """
    return character * SECTION_WIDTH


def banner(title: str) -> str:
    """
    Return a formatted banner.

    Args:
        title:
            Section title.

    Returns:
        Banner string.
    """
    return (
        f"\n{divider('=')}\n"
        f"{title.upper():^{SECTION_WIDTH}}\n"
        f"{divider('=')}"
    )


def print_banner(title: str) -> None:
    """Print a banner."""
    print(banner(title))


def print_result(name: str, value: Any) -> None:
    """
    Print a formatted result.

    Args:
        name:
            Label.

        value:
            Value.
    """
    print(f"{name:<35}: {value}")