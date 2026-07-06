"""
Command-line interface for the loop_foundations package.

This module allows users to execute demonstrations for individual
loop-related topics.

Examples:
    python -m loop_foundations.cli --list

    python -m loop_foundations.cli --topic loops

    python -m loop_foundations.cli --topic break

    python -m loop_foundations.cli --topic else

Author: Python Training
"""

from __future__ import annotations

import argparse
from collections.abc import Callable

from .demo import (
    demonstrate_break_continue,
    demonstrate_for_else_while_else,
    demonstrate_for_loops,
    demonstrate_while_loops,
)

TOPICS: dict[str, Callable[[], None]] = {
    "loops": demonstrate_for_loops,
    "while": demonstrate_while_loops,
    "break": demonstrate_break_continue,
    "else": demonstrate_for_else_while_else,
}


def create_parser() -> argparse.ArgumentParser:
    """
    Create the command-line argument parser.

    Returns:
        Configured ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(
        prog="loop_foundations",
        description="Python Loop Foundations Training Module",
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