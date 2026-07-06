"""
comprehensions_generators package.

This package demonstrates Python comprehensions, iterators,
generators, and generator expressions.

Topics covered:

- List comprehensions
- Dictionary comprehensions
- Set comprehensions
- Nested comprehensions
- Iterator protocol
- Custom iterators
- Generators
- Generator expressions

Author: Python Training
"""

from .list_comprehensions import (
    even_numbers,
    filter_long_words,
    flatten_matrix,
    square_numbers,
)

from .dictionary_comprehensions import (
    employee_salary_map,
    number_squares,
    word_lengths,
)

from .set_comprehensions import (
    unique_first_letters,
    unique_lowercase_words,
    unique_remainders,
)

from .nested_comprehensions import (
    chessboard_coordinates,
    multiplication_grid,
    transpose_matrix,
)

from .iterators import (
    CountdownIterator,
    NumberIterator,
)

from .generators import (
    countdown,
    fibonacci,
    read_lines,
    square_generator,
)

__all__ = [
    "square_numbers",
    "even_numbers",
    "filter_long_words",
    "flatten_matrix",
    "number_squares",
    "word_lengths",
    "employee_salary_map",
    "unique_lowercase_words",
    "unique_remainders",
    "unique_first_letters",
    "multiplication_grid",
    "transpose_matrix",
    "chessboard_coordinates",
    "NumberIterator",
    "CountdownIterator",
    "countdown",
    "fibonacci",
    "square_generator",
    "read_lines",
]