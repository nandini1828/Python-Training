"""
comprehensions package

Topics covered:
- List comprehensions
- Dictionary comprehensions
- Set comprehensions
- Nested comprehensions
"""

from .list_comprehensions import list_comprehension_example
from .dictionary_comprehensions import dictionary_comprehension_example
from .set_comprehensions import set_comprehension_example
from .nested_comprehensions import nested_comprehension_example

__all__ = [
    "list_comprehension_example",
    "dictionary_comprehension_example",
    "set_comprehension_example",
    "nested_comprehension_example",
    "run",
]


def run() -> None:
    """Run all comprehension examples."""
    list_comprehension_example()
    dictionary_comprehension_example()
    set_comprehension_example()
    nested_comprehension_example()
