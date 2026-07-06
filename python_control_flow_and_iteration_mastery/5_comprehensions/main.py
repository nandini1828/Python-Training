"""
main.py

Entry point for Python Comprehensions.

Topics Covered:
- List Comprehensions
- Dictionary Comprehensions
- Set Comprehensions
- Nested Comprehensions
"""

import argparse

from comprehensions import (
    ListComprehensionExamples,
    DictionaryComprehensionExamples,
    SetComprehensionExamples,
    NestedComprehensionExamples
)


def demonstrate_list_comprehension() -> None:

    print("\n" + "=" * 50)
    print("LIST COMPREHENSIONS")
    print("=" * 50)

    print(
        ListComprehensionExamples.create_squares(
            [1, 2, 3, 4]
        )
    )

    print(
        ListComprehensionExamples.filter_even_numbers(
            [1, 2, 3, 4, 5, 6]
        )
    )

    print(
        ListComprehensionExamples.convert_to_uppercase(
            ["python", "ai"]
        )
    )

    print(
        ListComprehensionExamples.string_lengths(
            ["Python", "AI"]
        )
    )


def demonstrate_dictionary_comprehension() -> None:

    print("\n" + "=" * 50)
    print("DICTIONARY COMPREHENSIONS")
    print("=" * 50)

    print(
        DictionaryComprehensionExamples.square_dictionary(5)
    )

    print(
        DictionaryComprehensionExamples.word_lengths(
            ["Python", "AI"]
        )
    )

    print(
        DictionaryComprehensionExamples.even_square_dictionary(6)
    )


def demonstrate_set_comprehension() -> None:

    print("\n" + "=" * 50)
    print("SET COMPREHENSIONS")
    print("=" * 50)

    print(
        SetComprehensionExamples.lowercase_words(
            ["Python", "AI", "PYTHON"]
        )
    )

    print(
        SetComprehensionExamples.unique_even_numbers(
            [1, 2, 2, 4, 6]
        )
    )

    print(
        SetComprehensionExamples.square_set(
            [1, 2, 3]
        )
    )


def demonstrate_nested_comprehension() -> None:

    print("\n" + "=" * 50)
    print("NESTED COMPREHENSIONS")
    print("=" * 50)

    matrix = [
        [1, 2],
        [3, 4]
    ]

    print(
        NestedComprehensionExamples.flatten_matrix(matrix)
    )

    print(
        NestedComprehensionExamples.create_matrix(2, 3)
    )

    print(
        NestedComprehensionExamples.multiplication_table(3)
    )


def run_all() -> None:

    demonstrate_list_comprehension()
    demonstrate_dictionary_comprehension()
    demonstrate_set_comprehension()
    demonstrate_nested_comprehension()


def main() -> None:

    parser = argparse.ArgumentParser(
        description="Python Comprehensions"
    )

    parser.add_argument(
        "--section",
        default="all",
        choices=[
            "all",
            "list",
            "dictionary",
            "set",
            "nested"
        ]
    )

    args = parser.parse_args()

    if args.section == "all":
        run_all()

    elif args.section == "list":
        demonstrate_list_comprehension()

    elif args.section == "dictionary":
        demonstrate_dictionary_comprehension()

    elif args.section == "set":
        demonstrate_set_comprehension()

    elif args.section == "nested":
        demonstrate_nested_comprehension()

    print("\nProject Executed Successfully")


if __name__ == "__main__":
    main()