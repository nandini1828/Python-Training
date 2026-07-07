"""
iterators_generators package

Topics covered:
- Iterator protocol with __iter__ and __next__
- Generators with yield
- Generator expressions
"""

from .iterator_protocol import IteratorExample
from .generators import generate_numbers, generate_even_numbers, run as run_generators
from .generator_expressions import generator_expression_example, run as run_generator_expressions

__all__ = [
    "IteratorExample",
    "generate_numbers",
    "generate_even_numbers",
    "generator_expression_example",
    "run",
]


def run() -> None:
    """Run all iterator and generator examples."""
    run_generators()
    run_generator_expressions()
