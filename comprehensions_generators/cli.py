"""
Command-line interface for the comprehensions_generators package.

This module allows users to execute demonstrations for individual
topics within the package.

Examples:
    python -m comprehensions_generators.cli --list

    python -m comprehensions_generators.cli --topic list

    python -m comprehensions_generators.cli --topic generators

Author: Python Training
"""

from __future__ import annotations

import argparse
from collections.abc import Callable

from .demo import (
    demonstrate_dictionary_comprehensions,
    demonstrate_generators,
    demonstrate_iterators,
    demonstrate_list_comprehensions,
    demonstrate_nested_comprehensions,
    demonstrate_set_comprehensions,
)

TOPICS: dict[str, Callable[[], None]] = {
    "list": demonstrate_list_comprehensions,
    "dictionary": demonstrate_dictionary_comprehensions,
    "set": demonstrate_set_comprehensions,
    "nested": demonstrate_nested_comprehensions,
    "iterators": demonstrate_iterators,
    "generators": demonstrate_generators,
}


def create_parser() -> argparse.ArgumentParser:
    """
    Create the command-line argument parser.

    Returns:
        Configured ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(
        prog="comprehensions_generators",
        description=(
            "Python Comprehensions & Generators "
            "Training Module"
        ),
    )

    parser.add_argument(
        "--topic",
        choices=sorted(TOPICS.keys()),
        help="Run a specific topic demonstration.",
    )

    parser.add_argument(
        "--list",
        action="store_true",
        help="List all available topics.",
    )

    return parser


def list_topics() -> None:
    """Display all available demonstration topics."""
    print("\nAvailable Topics:\n")

    for topic in sorted(TOPICS):
        print(f"  • {topic}")

    print()


def main() -> None:
    """CLI entry point."""
    parser = create_parser()

    args = parser.parse_args()

    if args.list:
        list_topics()
        return

    if args.topic:
        TOPICS[args.topic]()
        return

    parser.print_help()


if __name__ == "__main__":
    main()