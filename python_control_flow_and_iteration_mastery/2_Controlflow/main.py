"""
main.py

Entry point for Python Loop Foundations.

Topics Covered:
- for Loop
- while Loop
- break
- continue
- pass
- for-else
- while-else
"""

import argparse

from loops import (
    ForLoopExamples,
    WhileLoopExamples,
    BreakContinueExamples,
    PassExamples,
    ForElseExamples,
    WhileElseExamples
)


def demonstrate_for_loop() -> None:
    """Demonstrates for loop examples."""

    print("\n" + "=" * 50)
    print("FOR LOOP")
    print("=" * 50)

    print(
        "Iterate List :",
        ForLoopExamples.iterate_list([10, 20, 30])
    )

    print(
        "Iterate String :",
        ForLoopExamples.iterate_string("Python")
    )

    print(
        "Range :",
        ForLoopExamples.iterate_range(1, 6)
    )

    print(
        "Sum :",
        ForLoopExamples.calculate_sum([10, 20, 30])
    )


def demonstrate_while_loop() -> None:
    """Demonstrates while loop examples."""

    print("\n" + "=" * 50)
    print("WHILE LOOP")
    print("=" * 50)

    print(
        "Count :",
        WhileLoopExamples.count_numbers(5)
    )

    print(
        "Countdown :",
        WhileLoopExamples.countdown(5)
    )

    print(
        "Sum :",
        WhileLoopExamples.calculate_sum(5)
    )


def demonstrate_break_continue() -> None:
    """Demonstrates break and continue."""

    print("\n" + "=" * 50)
    print("BREAK & CONTINUE")
    print("=" * 50)

    print(
        BreakContinueExamples.break_example(
            [10, 20, 30],
            20
        )
    )

    print(
        BreakContinueExamples.stop_at_five()
    )

    print(
        BreakContinueExamples.continue_example(
            [1, 2, 3, 4, 5, 6]
        )
    )

    print(
        BreakContinueExamples.skip_empty_strings(
            ["Python", "", "AI", "", "ML"]
        )
    )


def demonstrate_pass() -> None:
    """Demonstrates pass statement."""

    print("\n" + "=" * 50)
    print("PASS STATEMENT")
    print("=" * 50)

    print(
        PassExamples.empty_if(10)
    )

    print(
        PassExamples.empty_loop(5)
    )

    print(
        PassExamples.skip_even_numbers(
            [1, 2, 3, 4]
        )
    )

    print(
        PassExamples.placeholder_function()
    )


def demonstrate_for_else() -> None:
    """Demonstrates for-else."""

    print("\n" + "=" * 50)
    print("FOR ELSE")
    print("=" * 50)

    print(
        ForElseExamples.search_number(
            [10, 20, 30],
            20
        )
    )

    print(
        ForElseExamples.search_name(
            ["Alice", "Bob"],
            "Bob"
        )
    )


def demonstrate_while_else() -> None:
    """Demonstrates while-else."""

    print("\n" + "=" * 50)
    print("WHILE ELSE")
    print("=" * 50)

    print(
        WhileElseExamples.count(5)
    )

    print(
        WhileElseExamples.search_number(
            [10, 20, 30],
            40
        )
    )


def run_all() -> None:
    """Runs all loop demonstrations."""

    demonstrate_for_loop()
    demonstrate_while_loop()
    demonstrate_break_continue()
    demonstrate_pass()
    demonstrate_for_else()
    demonstrate_while_else()


def main() -> None:
    """
    Parses command-line arguments.
    """

    parser = argparse.ArgumentParser(
        description="Python Loop Foundations"
    )

    parser.add_argument(
        "--section",
        default="all",
        choices=[
            "all",
            "for",
            "while",
            "break",
            "pass",
            "forelse",
            "whileelse"
        ],
        help="Run a specific loop topic."
    )

    args = parser.parse_args()

    if args.section == "all":
        run_all()

    elif args.section == "for":
        demonstrate_for_loop()

    elif args.section == "while":
        demonstrate_while_loop()

    elif args.section == "break":
        demonstrate_break_continue()

    elif args.section == "pass":
        demonstrate_pass()

    elif args.section == "forelse":
        demonstrate_for_else()

    elif args.section == "whileelse":
        demonstrate_while_else()

    print("\nProject Executed Successfully")


if __name__ == "__main__":
    main()