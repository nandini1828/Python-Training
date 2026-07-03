"""
main.py

Entry point for Python Iteration Helpers.

Topics Covered:
- range()
- enumerate()
- zip()
- reversed()
- sorted()
- any()
- all()
"""

import argparse

from iterations import (
    RangeExamples,
    EnumerateExamples,
    ZipExamples,
    ReversedExamples,
    SortedExamples,
    AnyAllExamples
)


def demonstrate_range() -> None:
    """Demonstrates range()."""

    print("\n" + "=" * 50)
    print("RANGE")
    print("=" * 50)

    print("Basic Range      :", RangeExamples.basic_range())
    print("Start Stop       :", RangeExamples.start_stop())
    print("Start Stop Step  :", RangeExamples.start_stop_step())
    print("Reverse Range    :", RangeExamples.reverse_range())


def demonstrate_enumerate() -> None:
    """Demonstrates enumerate()."""

    print("\n" + "=" * 50)
    print("ENUMERATE")
    print("=" * 50)

    print(
        "Default :",
        EnumerateExamples.enumerate_list(
            ["Python", "AI", "ML"]
        )
    )

    print(
        "Start=1 :",
        EnumerateExamples.enumerate_with_start(
            ["Python", "AI", "ML"]
        )
    )


def demonstrate_zip() -> None:
    """Demonstrates zip()."""

    print("\n" + "=" * 50)
    print("ZIP")
    print("=" * 50)

    print(
        ZipExamples.zip_lists(
            ["Alice", "Bob"],
            [90, 80]
        )
    )

    print(
        ZipExamples.zip_longest_lists(
            ["Alice"],
            [90, 80]
        )
    )


def demonstrate_reversed() -> None:
    """Demonstrates reversed()."""

    print("\n" + "=" * 50)
    print("REVERSED")
    print("=" * 50)

    print(
        ReversedExamples.reverse_list(
            [10, 20, 30]
        )
    )

    print(
        ReversedExamples.reverse_string(
            "Python"
        )
    )


def demonstrate_sorted() -> None:
    """Demonstrates sorted()."""

    print("\n" + "=" * 50)
    print("SORTED")
    print("=" * 50)

    print(
        SortedExamples.sort_numbers(
            [5, 2, 8, 1]
        )
    )

    print(
        SortedExamples.sort_reverse(
            [5, 2, 8, 1]
        )
    )

    print(
        SortedExamples.sort_by_length(
            ["Python", "AI", "ML"]
        )
    )


def demonstrate_any_all() -> None:
    """Demonstrates any() and all()."""

    print("\n" + "=" * 50)
    print("ANY & ALL")
    print("=" * 50)

    print(
        "Any Positive :",
        AnyAllExamples.any_positive(
            [-5, 2, -3]
        )
    )

    print(
        "All Positive :",
        AnyAllExamples.all_positive(
            [2, 4, 6]
        )
    )

    print(
        "Any True :",
        AnyAllExamples.any_true(
            [False, False, True]
        )
    )

    print(
        "All True :",
        AnyAllExamples.all_true(
            [True, True, True]
        )
    )


def run_all() -> None:
    """Runs all demonstrations."""

    demonstrate_range()
    demonstrate_enumerate()
    demonstrate_zip()
    demonstrate_reversed()
    demonstrate_sorted()
    demonstrate_any_all()


def main() -> None:
    """Parses command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Python Iteration Helpers"
    )

    parser.add_argument(
        "--section",
        default="all",
        choices=[
            "all",
            "range",
            "enumerate",
            "zip",
            "reversed",
            "sorted",
            "anyall"
        ],
        help="Run a specific iteration helper."
    )

    args = parser.parse_args()

    if args.section == "all":
        run_all()

    elif args.section == "range":
        demonstrate_range()

    elif args.section == "enumerate":
        demonstrate_enumerate()

    elif args.section == "zip":
        demonstrate_zip()

    elif args.section == "reversed":
        demonstrate_reversed()

    elif args.section == "sorted":
        demonstrate_sorted()

    elif args.section == "anyall":
        demonstrate_any_all()

    print("\nProject Executed Successfully")


if __name__ == "__main__":
    main()