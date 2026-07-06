"""Command-line interface examples for the mastery project."""

from __future__ import annotations

import argparse

try:
    from ..conditionals.if_else_examples import grade_student, simulate_atm_menu
    from ..loops.for_loop_examples import fibonacci_numbers
    from ..iteration.range_examples import describe_range
    from ..comprehensions.list_comprehension import square_numbers
    from ..iterators_generators.generators import count_up_to
except ImportError:  # pragma: no cover - supports direct script execution
    from conditionals.if_else_examples import grade_student, simulate_atm_menu
    from loops.for_loop_examples import fibonacci_numbers
    from iteration.range_examples import describe_range
    from comprehensions.list_comprehension import square_numbers
    from iterators_generators.generators import count_up_to


def build_parser() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(description="Explore Python control flow concepts.")
    parser.add_argument(
        "--module",
        choices=["conditionals", "loops", "iteration", "collections", "comprehensions", "generators", "all"],
        default="all",
        help="Choose which module demonstration to run.",
    )
    return parser


def run_demo(module_name: str) -> None:
    """Run the selected demonstration module.

    Args:
        module_name: The selected module name.
    """
    if module_name in {"conditionals", "all"}:
        print("Conditionals demo:")
        print(f"Grade student: {grade_student(88)}")
        print(f"ATM menu: {simulate_atm_menu(120.0, 'withdraw')}")
    if module_name in {"loops", "all"}:
        print("Loops demo:")
        print(f"Fibonacci numbers: {fibonacci_numbers(5)}")
    if module_name in {"iteration", "all"}:
        print("Iteration demo:")
        print(f"Range description: {describe_range(5)}")
    if module_name in {"collections", "all"}:
        print("Collections demo:")
        print("List iteration example is available in the module.")
    if module_name in {"comprehensions", "all"}:
        print("Comprehensions demo:")
        print(f"Squared values: {square_numbers([1, 2, 3])}")
    if module_name in {"generators", "all"}:
        print("Generators demo:")
        print(f"Generated values: {list(count_up_to(5))}")
