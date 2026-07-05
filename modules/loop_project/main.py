"""
Entry point for the Loop Project.
"""

from loops.for_loop import (
    print_numbers,
    even_numbers,
    square_numbers,
    character_count,
    find_max,
    multiplication_table,
    dictionary_keys,
    zip_names_scores,
    enumerate_subjects,
)

from loops.while_loop import *

from loops.loop_control import *

from loops.for_else import *

from loops.while_else import *


def run_for_loop() -> None:
    """Execute functions from the for_loop module."""
    print("\n========== FOR LOOP ==========")

    print("Numbers:", print_numbers(10))
    print("Even Numbers:", even_numbers(10))
    print("Squares:", square_numbers(5))
    print("Character Count:", character_count("Python"))
    print("Maximum:", find_max([5, 12, 8, 20, 15]))

    print("\nMultiplication Table:")
    for row in multiplication_table(5):
        print(row)

    student = {
        "name": "Alice",
        "age": 22,
        "course": "Python",
    }

    print("\nDictionary Keys:", dictionary_keys(student))

    print(
        "Names & Scores:",
        zip_names_scores(
            ["Alice", "Bob", "Charlie"],
            [90, 85, 95],
        ),
    )

    print(
        "Subjects:",
        enumerate_subjects(
            ["Python", "SQL", "Django"],
        ),
    )


def run_while_loop() -> None:
    """Execute functions from the while_loop module."""

    print("\n========== WHILE LOOP ==========")

    print("Countdown:", countdown(5))
    print("Factorial:", factorial(5))
    print("Reverse String:", reverse_string("Python"))
    print("Sum:", sum_numbers(10))
    print("Vowel Count:", count_vowels("Programming"))
    print("Power:", power(2, 5))
    print("Smallest:", find_smallest([15, 8, 22, 3, 10]))

def run_loop_control() -> None:
    """Execute functions from the loop_control module."""

    print("\n========== LOOP CONTROL ==========")

    transactions = [True, True, False, True]

    print(
        "First Failed Transaction:",
        find_first_failed_transaction(transactions),
    )

    customers = [
        {"name": "Alice", "active": True},
        {"name": "Bob", "active": False},
        {"name": "Charlie", "active": True},
    ]

    print(
        "Active Customers:",
        filter_active_customers(customers),
    )

    print(
        "Even Numbers:",
        collect_even_numbers([1, 2, 3, 4, 5, 6]),
    )

    print(
        "Positive Numbers:",
        skip_negative_numbers([-5, 3, -2, 8]),
    )

    print(
        "First High Sale:",
        first_high_value_sale([200, 300, 900, 1000], 500),
    )

    print(
        "Running Total:",
        calculate_running_total([10, 20, 30]),
    )


def run_for_else() -> None:
    """Execute functions from the for_else module."""

    print("\n========== FOR ELSE ==========")

    print(
        "Employee Found:",
        search_employee(["Alice", "Bob"], "Bob"),
    )

    print(
        "Policy Found:",
        search_policy([101, 102, 103], 102),
    )

    print(
        "Prime:",
        find_prime(17),
    )

    print(
        "Product Found:",
        locate_product(
            ["Laptop", "Phone", "Tablet"],
            "Phone",
        ),
    )


def run_while_else() -> None:
    """Execute functions from the while_else module."""

    print("\n========== WHILE ELSE ==========")

    print(
        "PIN Verified:",
        verify_pin(
            "1234",
            ["1111", "1234"],
        ),
    )

    print(
        "Number Found:",
        search_number(
            [5, 10, 15],
            10,
        ),
    )

    print(
        "Countdown Result:",
        countdown(5),
    )

    print(
        "Password Verified:",
        password_attempts(
            "admin",
            ["root", "admin"],
        ),
    )


def main() -> None:
    """Run the Loop Project."""

    print("=" * 60)
    print("             PYTHON LOOP PROJECT")
    print("=" * 60)

    run_for_loop()
    run_while_loop()
    run_loop_control()
    run_for_else()
    run_while_else()

    print("\nProject completed successfully.")


if __name__ == "__main__":
    main()