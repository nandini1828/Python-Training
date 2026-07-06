"""
main.py

Entry point for Python Iterators & Generators.

Topics Covered:
- Iterator Protocol
- Generators
- Generator Expressions
"""

import argparse

from Iterators import (
    IteratorExamples,
    GeneratorExamples,
    GeneratorExpressionExamples
)


def demonstrate_iterator() -> None:

    print("\n" + "=" * 50)
    print("ITERATOR")
    print("=" * 50)

    iterator = IteratorExamples.create_iterator(
        [10, 20, 30]
    )

    print("Iterator :", iterator)

    print(
        "First Element :",
        IteratorExamples.next_element(
            [10, 20, 30]
        )
    )

    print(
        "Manual Iteration :",
        IteratorExamples.iterate_manually(
            [1, 2, 3]
        )
    )

    print(
        "Custom Iterator :",
        IteratorExamples.custom_iterator(5)
    )


def demonstrate_generator() -> None:

    print("\n" + "=" * 50)
    print("GENERATORS")
    print("=" * 50)

    print(
        list(
            GeneratorExamples.count_numbers(5)
        )
    )

    print(
        list(
            GeneratorExamples.square_numbers(
                [1, 2, 3]
            )
        )
    )

    print(
        list(
            GeneratorExamples.even_numbers(6)
        )
    )


def demonstrate_generator_expression() -> None:

    print("\n" + "=" * 50)
    print("GENERATOR EXPRESSIONS")
    print("=" * 50)

    print(
        list(
            GeneratorExpressionExamples.square_generator(
                [1, 2, 3]
            )
        )
    )

    print(
        list(
            GeneratorExpressionExamples.filter_even(
                [1, 2, 3, 4, 5]
            )
        )
    )

    print(
        list(
            GeneratorExpressionExamples.string_lengths(
                ["Python", "AI"]
            )
        )
    )


def run_all() -> None:

    demonstrate_iterator()
    demonstrate_generator()
    demonstrate_generator_expression()


def main() -> None:

    parser = argparse.ArgumentParser(
        description="Python Iterators & Generators"
    )

    parser.add_argument(
        "--section",
        default="all",
        choices=[
            "all",
            "iterator",
            "generator",
            "expression"
        ]
    )

    args = parser.parse_args()

    if args.section == "all":
        run_all()

    elif args.section == "iterator":
        demonstrate_iterator()

    elif args.section == "generator":
        demonstrate_generator()

    elif args.section == "expression":
        demonstrate_generator_expression()

    print("\nProject Executed Successfully")


if __name__ == "__main__":
    main()