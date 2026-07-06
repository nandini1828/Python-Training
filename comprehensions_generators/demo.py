"""
Demonstration script for the comprehensions_generators package.

Run:

    python -m comprehensions_generators.demo

Author: Python Training
"""

from __future__ import annotations

from dictionary_comprehensions import (
    employee_salary_map,
    even_square_map,
    filter_positive,
    grade_book,
    invert_dictionary,
    lowercase_values,
    number_squares,
    uppercase_keys,
    word_lengths as dictionary_word_lengths,
)

from generators import (
    alphabet_generator,
    countdown,
    even_numbers as generator_even_numbers,
    fibonacci,
    generator_expression,
    infinite_counter,
    lazy_range,
    odd_numbers as generator_odd_numbers,
    pipeline,
    reverse_generator,
    running_total,
    square_generator,
)

from iterators import (
    AlphabetIterator,
    CountdownIterator,
    EmployeeIterator,
    NumberIterator,
    consume_iterator,
    iterator_max,
    iterator_sum,
    iterator_to_list,
    manual_iteration,
)

from list_comprehensions import (
    even_numbers,
    filter_long_words,
    flatten_matrix,
    lowercase_words,
    multiplication_table,
    odd_numbers,
    remove_none,
    square_numbers,
    uppercase_words,
    word_lengths,
)

from nested_comprehensions import (
    cartesian_product,
    chessboard_coordinates,
    coordinate_grid,
    even_matrix,
    flatten_strings,
    identity_matrix,
    multiplication_grid,
    transpose_matrix,
)

from set_comprehensions import (
    positive_numbers,
    unique_characters,
    unique_even_numbers,
    unique_first_letters,
    unique_lowercase_words,
    unique_remainders,
    unique_word_lengths,
    vowels,
)

from utils import (
    print_banner,
    print_result,
)


def demonstrate_list_comprehensions() -> None:
    """Demonstrate list comprehensions."""

    print_banner("List Comprehensions")

    numbers = [1, 2, 3, 4, 5, 6]

    words = [
        "Python",
        "django",
        "API",
        "Enterprise",
    ]

    matrix = [
        [1, 2],
        [3, 4],
    ]

    print_result(
        "Squares",
        square_numbers(numbers),
    )

    print_result(
        "Even Numbers",
        even_numbers(numbers),
    )

    print_result(
        "Odd Numbers",
        odd_numbers(numbers),
    )

    print_result(
        "Uppercase",
        uppercase_words(words),
    )

    print_result(
        "Lowercase",
        lowercase_words(words),
    )

    print_result(
        "Long Words",
        filter_long_words(words),
    )

    print_result(
        "Word Lengths",
        word_lengths(words),
    )

    print_result(
        "Remove None",
        remove_none(
            [1, None, 2, None, 3],
        ),
    )

    print_result(
        "Flatten Matrix",
        flatten_matrix(matrix),
    )

    print_result(
        "Multiplication Table",
        multiplication_table(5),
    )


def demonstrate_dictionary_comprehensions() -> None:
    """Demonstrate dictionary comprehensions."""

    print_banner("Dictionary Comprehensions")

    print_result(
        "Number Squares",
        number_squares(6),
    )

    print_result(
        "Word Lengths",
        dictionary_word_lengths(
            [
                "Python",
                "Django",
                "FastAPI",
            ],
        ),
    )

    print_result(
        "Employee Salaries",
        employee_salary_map(
            ["Alice", "Bob"],
            [60000, 70000],
        ),
    )

    print_result(
        "Even Squares",
        even_square_map(10),
    )

    print_result(
        "Uppercase Keys",
        uppercase_keys(
            {
                "name": "Alice",
                "city": "London",
            },
        ),
    )

    print_result(
        "Lowercase Values",
        lowercase_values(
            {
                "Language": "PYTHON",
            },
        ),
    )

    print_result(
        "Invert Dictionary",
        invert_dictionary(
            {
                "A": "Apple",
                "B": "Banana",
            },
        ),
    )

    print_result(
        "Positive Values",
        filter_positive(
            {
                "A": 10,
                "B": -5,
                "C": 25,
            },
        ),
    )

    print_result(
        "Grades",
        grade_book(
            {
                "Alice": 90,
                "Bob": 25,
            },
        ),
    )


def demonstrate_set_comprehensions() -> None:
    """Demonstrate set comprehensions."""

    print_banner("Set Comprehensions")

    print_result(
        "Lowercase Words",
        unique_lowercase_words(
            [
                "Python",
                "python",
                "Django",
            ],
        ),
    )

    print_result(
        "First Letters",
        unique_first_letters(
            [
                "Python",
                "Programming",
                "Django",
            ],
        ),
    )

    print_result(
        "Word Lengths",
        unique_word_lengths(
            [
                "Python",
                "Java",
                "C",
            ],
        ),
    )

    print_result(
        "Unique Even Numbers",
        unique_even_numbers(
            [2, 4, 2, 6, 8, 4],
        ),
    )

    print_result(
        "Unique Remainders",
        unique_remainders(
            [10, 15, 20, 25],
            3,
        ),
    )

    print_result(
        "Positive Numbers",
        positive_numbers(
            [-1, 5, 10, -7],
        ),
    )

    print_result(
        "Characters",
        unique_characters(
            "Enterprise",
        ),
    )

    print_result(
        "Vowels",
        vowels(
            "Artificial Intelligence",
        ),
    )
def demonstrate_nested_comprehensions() -> None:
    """Demonstrate nested comprehensions."""

    print_banner("Nested Comprehensions")

    matrix = [
        [1, 2],
        [3, 4],
    ]

    print_result(
        "Multiplication Grid",
        multiplication_grid(4, 4),
    )

    print_result(
        "Transpose Matrix",
        transpose_matrix(matrix),
    )

    print_result(
        "Chessboard Coordinates",
        chessboard_coordinates()[:16],
    )

    print_result(
        "Coordinate Grid",
        coordinate_grid(3, 3),
    )

    print_result(
        "Cartesian Product",
        cartesian_product(
            ["A", "B"],
            ["1", "2"],
        ),
    )

    print_result(
        "Identity Matrix",
        identity_matrix(4),
    )

    print_result(
        "Even Matrix",
        even_matrix(3, 4),
    )

    print_result(
        "Flatten Strings",
        flatten_strings(
            [
                ["Python", "Django"],
                ["FastAPI", "Flask"],
            ],
        ),
    )


def demonstrate_iterators() -> None:
    """Demonstrate custom iterators."""

    print_banner("Iterator Protocol")

    print_result(
        "Number Iterator",
        consume_iterator(
            NumberIterator(5),
        ),
    )

    print_result(
        "Countdown Iterator",
        consume_iterator(
            CountdownIterator(5),
        ),
    )

    print_result(
        "Alphabet Iterator",
        list(AlphabetIterator()),
    )

    print_result(
        "Employee Iterator",
        list(
            EmployeeIterator(
                [
                    "Alice",
                    "Bob",
                    "Charlie",
                ],
            ),
        ),
    )

    print_result(
        "Manual Iteration",
        manual_iteration(
            [10, 20, 30],
        ),
    )

    print_result(
        "Iterator Sum",
        iterator_sum(
            NumberIterator(6),
        ),
    )

    print_result(
        "Iterator Max",
        iterator_max(
            NumberIterator(6),
        ),
    )

    print_result(
        "Iterator To List",
        iterator_to_list(
            NumberIterator(5),
        ),
    )


def demonstrate_generators() -> None:
    """Demonstrate generators."""

    print_banner("Generators")

    print_result(
        "Countdown",
        list(countdown(5)),
    )

    print_result(
        "Fibonacci",
        list(fibonacci(10)),
    )

    print_result(
        "Square Generator",
        list(
            square_generator(
                [1, 2, 3, 4],
            ),
        ),
    )

    print_result(
        "Reverse Generator",
        list(
            reverse_generator(
                [1, 2, 3, 4],
            ),
        ),
    )

    print_result(
        "Alphabet Generator",
        list(alphabet_generator()),
    )

    print_result(
        "Even Generator",
        list(
            generator_even_numbers(10),
        ),
    )

    print_result(
        "Odd Generator",
        list(
            generator_odd_numbers(10),
        ),
    )

    print_result(
        "Running Total",
        list(
            running_total(
                [10, 20, 30],
            ),
        ),
    )

    print_result(
        "Pipeline",
        list(
            pipeline(
                range(10),
            ),
        ),
    )

    print_result(
        "Generator Expression",
        list(
            generator_expression(
                [1, 2, 3, 4],
            ),
        ),
    )

    counter = infinite_counter()

    print_result(
        "Infinite Counter (First 5)",
        [next(counter) for _ in range(5)],
    )

    print_result(
        "Lazy Range",
        list(
            lazy_range(10, 15),
        ),
    )


def main() -> None:
    """Run every demonstration."""

    print_banner(
        "Comprehensions & Generators"
    )

    demonstrate_list_comprehensions()

    demonstrate_dictionary_comprehensions()

    demonstrate_set_comprehensions()

    demonstrate_nested_comprehensions()

    demonstrate_iterators()

    demonstrate_generators()

    print_banner("Demo Completed")


if __name__ == "__main__":
    main()    