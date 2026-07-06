"""
main.py

Entry point for Python Data Structure Iteration & Safety.

Topics Covered:
- Lists
- List Modification Trap
- Dictionaries
- Dictionary Safety
- Sets
"""

import argparse

from datastructures import (
    ListExamples,
    ListModificationExamples,
    DictionaryExamples,
    DictionarySafetyExamples,
    SetExamples
)


def demonstrate_lists() -> None:
    """Demonstrates list operations."""

    print("\n" + "=" * 50)
    print("LIST EXAMPLES")
    print("=" * 50)

    numbers = [10, 20, 30, 40, 50]

    print("Iterate List :", ListExamples.iterate_list(numbers))
    print("Index 2      :", ListExamples.access_index(numbers, 2))
    print("Slice        :", ListExamples.slice_list(numbers))
    print("First        :", ListExamples.first_element(numbers))
    print("Last         :", ListExamples.last_element(numbers))


def demonstrate_list_modification() -> None:
    """Demonstrates list modification."""

    print("\n" + "=" * 50)
    print("LIST MODIFICATION")
    print("=" * 50)

    numbers = [1, 2, 3, 4, 5, 6]

    print(
        "Wrong Way   :",
        ListModificationExamples.remove_even_wrong(numbers)
    )

    print(
        "Correct Way :",
        ListModificationExamples.remove_even_correct(numbers)
    )


def demonstrate_dictionary() -> None:
    """Demonstrates dictionary iteration."""

    print("\n" + "=" * 50)
    print("DICTIONARY")
    print("=" * 50)

    student = {
        "name": "Bhavya",
        "age": 22,
        "course": "Python"
    }

    print("Keys   :", DictionaryExamples.iterate_keys(student))
    print("Values :", DictionaryExamples.iterate_values(student))
    print("Items  :", DictionaryExamples.iterate_items(student))


def demonstrate_dictionary_safety() -> None:
    """Demonstrates safe dictionary access."""

    print("\n" + "=" * 50)
    print("DICTIONARY SAFETY")
    print("=" * 50)

    student = {
        "name": "Bhavya"
    }

    print(
        "Safe Get Existing :",
        DictionarySafetyExamples.safe_get(
            student,
            "name"
        )
    )

    print(
        "Safe Get Missing :",
        DictionarySafetyExamples.safe_get(
            student,
            "city"
        )
    )

    print(
        "Default Dict :",
        DictionarySafetyExamples.default_dictionary()
    )

    print(
        "Key Exists :",
        DictionarySafetyExamples.check_key(
            student,
            "name"
        )
    )


def demonstrate_sets() -> None:
    """Demonstrates set operations."""

    print("\n" + "=" * 50)
    print("SET EXAMPLES")
    print("=" * 50)

    values = {1, 2, 3}

    print(
        "Iterate Set :",
        SetExamples.iterate_set(values)
    )

    print(
        "Membership :",
        SetExamples.check_membership(values, 2)
    )

    print(
        "Remove Duplicates :",
        SetExamples.remove_duplicates(
            [1, 2, 2, 3, 3, 4]
        )
    )

    print(
        "Add Element :",
        SetExamples.add_element(values, 4)
    )


def run_all() -> None:
    """Runs all demonstrations."""

    demonstrate_lists()
    demonstrate_list_modification()
    demonstrate_dictionary()
    demonstrate_dictionary_safety()
    demonstrate_sets()


def main() -> None:
    """Parses command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Python Data Structure Iteration & Safety"
    )

    parser.add_argument(
        "--section",
        default="all",
        choices=[
            "all",
            "lists",
            "listmodification",
            "dictionary",
            "dictsafety",
            "sets"
        ],
        help="Run a specific topic."
    )

    args = parser.parse_args()

    if args.section == "all":
        run_all()

    elif args.section == "lists":
        demonstrate_lists()

    elif args.section == "listmodification":
        demonstrate_list_modification()

    elif args.section == "dictionary":
        demonstrate_dictionary()

    elif args.section == "dictsafety":
        demonstrate_dictionary_safety()

    elif args.section == "sets":
        demonstrate_sets()

    print("\nProject Executed Successfully")


if __name__ == "__main__":
    main()