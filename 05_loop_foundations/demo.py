"""
Demonstration script for the loop_foundations package.

Run:

    python -m loop_foundations.demo

Author: Python Training
"""

from __future__ import annotations

from break_continue import (
    find_first_even,
    first_duplicate,
    first_positive_number,
    placeholder_example,
    process_orders,
    process_valid_scores,
    remove_invalid_entries,
    search_student,
    skip_empty_strings,
    skip_negative_numbers,
    stop_at_value,
    validate_usernames,
)

from for_else_while_else import (
    authenticate_user,
    find_employee,
    first_divisible,
    is_prime,
    login_attempts,
    process_queue,
    retry_connection,
    search_item,
    validate_inventory,
    wait_for_service,
)

from loops import (
    countdown,
    count_characters,
    count_occurrences,
    factorial,
    fibonacci,
    filter_even_numbers,
    find_maximum,
    find_minimum,
    generate_range,
    iterate_dictionary,
    iterate_list,
    iterate_set,
    iterate_string,
    iterate_tuple,
    multiplication_table,
    nested_loop_grid,
    product_numbers,
    repeat_text,
    reverse_string,
    search_element,
    square_numbers,
    sum_numbers,
    while_sum,
)

from utils import (
    print_banner,
    print_result,
)


def demonstrate_for_loops() -> None:
    """Demonstrate basic for loops."""

    print_banner("For Loops")

    print_result(
        "Iterate List",
        iterate_list([1, 2, 3]),
    )

    print_result(
        "Iterate Tuple",
        iterate_tuple(("Python", "Django")),
    )

    print_result(
        "Iterate Set",
        iterate_set({"A", "B", "C"}),
    )

    print_result(
        "Iterate String",
        iterate_string("Python"),
    )

    print_result(
        "Iterate Dictionary",
        iterate_dictionary(
            {
                "name": "Alice",
                "age": 25,
            },
        ),
    )

    print_result(
        "Range",
        generate_range(1, 6),
    )

    print_result(
        "Sum",
        sum_numbers([1, 2, 3, 4, 5]),
    )

    print_result(
        "Product",
        product_numbers([1, 2, 3, 4]),
    )

    print_result(
        "Character Count",
        count_characters("Python"),
    )

    print_result(
        "Occurrences",
        count_occurrences(
            [1, 2, 2, 3, 2],
            2,
        ),
    )

    print_result(
        "Squares",
        square_numbers([1, 2, 3, 4]),
    )

    print_result(
        "Even Numbers",
        filter_even_numbers(
            [1, 2, 3, 4, 5, 6],
        ),
    )

    print_result(
        "Reverse",
        reverse_string("Python"),
    )


def demonstrate_while_loops() -> None:
    """Demonstrate while loops."""

    print_banner("While Loops")

    print_result(
        "Factorial",
        factorial(5),
    )

    print_result(
        "Countdown",
        countdown(5),
    )

    print_result(
        "Fibonacci",
        fibonacci(10),
    )

    print_result(
        "While Sum",
        while_sum(10),
    )

    print_result(
        "Repeat",
        repeat_text("Python", 3),
    )

    print_result(
        "Find Maximum",
        find_maximum(
            [2, 10, 8, 1],
        ),
    )

    print_result(
        "Find Minimum",
        find_minimum(
            [2, 10, 8, 1],
        ),
    )

    print_result(
        "Search Element",
        search_element(
            [1, 2, 3, 4],
            3,
        ),
    )

    print_result(
        "Multiplication Table",
        multiplication_table(5),
    )

    print_result(
        "Nested Grid",
        nested_loop_grid(2, 3),
    )
def demonstrate_break_continue() -> None:
    """Demonstrate break, continue, and pass."""

    print_banner("Break, Continue and Pass")

    print_result(
        "First Even",
        find_first_even([1, 3, 5, 8, 10]),
    )

    print_result(
        "Stop At Value",
        stop_at_value(
            [1, 2, 3, 4, 5],
            4,
        ),
    )

    print_result(
        "Skip Negatives",
        skip_negative_numbers(
            [5, -2, 8, -7, 10],
        ),
    )

    print_result(
        "Skip Empty Strings",
        skip_empty_strings(
            ["Python", "", "Django", ""],
        ),
    )

    print_result(
        "Search Student",
        search_student(
            ["Alice", "Bob", "Charlie"],
            "Bob",
        ),
    )

    print_result(
        "Valid Scores",
        process_valid_scores(
            [95, 120, 80, -5, 70],
        ),
    )

    orders = [
        {"id": 101, "active": True},
        {"id": 102, "active": False},
        {"id": 103, "active": True},
    ]

    print_result(
        "Processed Orders",
        process_orders(orders),
    )

    print_result(
        "First Positive",
        first_positive_number(
            [-10, -5, 7, 12],
        ),
    )

    print_result(
        "Remove Invalid",
        remove_invalid_entries(
            [None, "", "Python", 100],
        ),
    )

    print_result(
        "Validate Usernames",
        validate_usernames(
            [
                "john",
                "python_dev",
                "hello world",
                "alice123",
            ],
        ),
    )

    print_result(
        "First Duplicate",
        first_duplicate(
            [1, 3, 5, 3, 8],
        ),
    )

    print_result(
        "Pass Statement",
        placeholder_example(),
    )


def demonstrate_for_else_while_else() -> None:
    """Demonstrate for-else and while-else."""

    print_banner("For-Else and While-Else")

    print_result(
        "Search Item",
        search_item(
            ["Python", "Django", "FastAPI"],
            "Django",
        ),
    )

    print_result(
        "Find Employee",
        find_employee(
            ["Alice", "Bob", "Charlie"],
            "Alice",
        ),
    )

    print_result(
        "Prime Number",
        is_prime(29),
    )

    print_result(
        "Login Attempts",
        login_attempts(
            [
                "password",
                "python123",
                "admin",
            ],
            "admin",
        ),
    )

    print_result(
        "Retry Connection",
        retry_connection(
            success_on_attempt=3,
            maximum_attempts=5,
        ),
    )

    print_result(
        "Wait For Service",
        wait_for_service(
            ready_after=2,
            timeout=5,
        ),
    )

    print_result(
        "First Divisible",
        first_divisible(
            [5, 7, 11, 18, 23],
            3,
        ),
    )

    print_result(
        "Validate Inventory",
        validate_inventory(
            [10, 5, 8, 12],
        ),
    )

    print_result(
        "Process Queue",
        process_queue(
            [
                "Task-1",
                "Task-2",
                "STOP",
                "Task-3",
            ],
            "STOP",
        ),
    )

    print_result(
        "Authenticate User",
        authenticate_user(
            [
                "alice",
                "bob",
                "charlie",
            ],
            "charlie",
        ),
    )


def main() -> None:
    """Run all demonstrations."""

    print_banner("Loop Foundations")

    demonstrate_for_loops()

    demonstrate_while_loops()

    demonstrate_break_continue()

    demonstrate_for_else_while_else()

    print_banner("Demo Completed")


if __name__ == "__main__":
    main()   