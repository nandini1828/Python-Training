"""
Command-line interface for the iteration_safety package.

Run:

    python -m iteration_safety.cli --list

Author: Python Training
"""

from __future__ import annotations

import argparse
from collections.abc import Callable

from .demo import (
    demonstrate_copy_vs_reference,
    demonstrate_defensive_iteration,
    demonstrate_mutation_patterns,
    demonstrate_safe_dictionary_iteration,
    demonstrate_safe_list_iteration,
    demonstrate_safe_set_iteration,
)

TOPICS: dict[str, Callable[[], None]] = {
    "list": demonstrate_safe_list_iteration,
    "dictionary": demonstrate_safe_dictionary_iteration,
    "set": demonstrate_safe_set_iteration,
    "copy": demonstrate_copy_vs_reference,
    "mutation": demonstrate_mutation_patterns,
    "defensive": demonstrate_defensive_iteration,
}


def create_parser() -> argparse.ArgumentParser:
    """
    Create and configure the command-line parser.

    Returns:
        Configured ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(
        prog="iteration_safety",
        description="Python Iteration Safety Training Module",
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
    """Display all available topics."""
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