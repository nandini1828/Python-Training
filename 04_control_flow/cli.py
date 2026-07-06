"""
Command-line interface for the control_flow package.

This module allows users to explore individual topics covered in the
control_flow package.

Examples:
    python -m control_flow.cli --topic conditionals

    python -m control_flow.cli --topic truthy

    python -m control_flow.cli --list
"""

from __future__ import annotations

import argparse

from .demo import (
    demonstrate_conditionals,
    demonstrate_logical_operators,
    demonstrate_pattern_matching,
    demonstrate_short_circuit,
    demonstrate_ternary,
    demonstrate_truthy_falsy,
)


TOPICS: dict[str, callable] = {
    "conditionals": demonstrate_conditionals,
    "truthy": demonstrate_truthy_falsy,
    "logical": demonstrate_logical_operators,
    "short": demonstrate_short_circuit,
    "ternary": demonstrate_ternary,
    "match": demonstrate_pattern_matching,
}


def create_parser() -> argparse.ArgumentParser:
    """
    Create the command-line argument parser.

    Returns:
        Configured ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(
        prog="control_flow",
        description="Python Control Flow Training Module",
    )

    parser.add_argument(
        "--topic",
        choices=TOPICS.keys(),
        help="Run a single topic demonstration.",
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

    for topic in TOPICS:
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