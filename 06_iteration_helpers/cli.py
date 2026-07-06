"""
Command-line interface for the iteration_helpers package.

This module allows users to execute demonstrations for individual
iteration helper topics.

Examples:
    python -m iteration_helpers.cli --list

    python -m iteration_helpers.cli --topic range

    python -m iteration_helpers.cli --topic enumerate

Author: Python Training
"""

from __future__ import annotations

import argparse
from collections.abc import Callable

from .demo import (
    demonstrate_any_all,
    demonstrate_enumerate,
    demonstrate_range,
    demonstrate_reversed_sorted,
    demonstrate_zip,
)

TOPICS: dict[str, Callable[[], None]] = {
    "range": demonstrate_range,
    "enumerate": demonstrate_enumerate,
    "zip": demonstrate_zip,
    "sorted": demonstrate_reversed_sorted,
    "any_all": demonstrate_any_all,
}


def create_parser() -> argparse.ArgumentParser:
    """
    Create the command-line argument parser.

    Returns:
        Configured ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(
        prog="iteration_helpers",
        description="Python Iteration Helpers Training Module",
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