"""
Main runner for Python Control Flow Mastery project.
"""

from conditionals.if_else import classify_number
from conditionals.truthy_falsy import evaluate_truthy_falsy
from conditionals.logical_operators import evaluate_logical_operations
from conditionals.short_circuit import get_first_truthy_value
from conditionals.ternary import get_voting_status
from conditionals.match_case import get_day_category


def run_examples() -> None:
    """
    Runs sample examples from the project.
    """
    print("=== IF ELSE ===")
    print(classify_number(10))
    print(classify_number(-5))
    print(classify_number(0))

    print("\n=== TRUTHY FALSY ===")
    print(evaluate_truthy_falsy())

    print("\n=== LOGICAL OPERATORS ===")
    print(evaluate_logical_operations(True, False))

    print("\n=== SHORT CIRCUIT ===")
    print(get_first_truthy_value("", "Fallback Value"))

    print("\n=== TERNARY ===")
    print(get_voting_status(21))

    print("\n=== MATCH CASE ===")
    print(get_day_category("Sunday"))


if __name__ == "__main__":
    run_examples()