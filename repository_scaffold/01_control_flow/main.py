"""
Main entry point for the Control Flow module.

Run this file to execute demonstrations from all concepts.
"""

from if_else.demo import main as if_else_demo
from truthy_falsy.demo import main as truthy_falsy_demo
from logical_operators.demo import main as logical_demo
from short_circuit.demo import main as short_circuit_demo
from ternary_operator.demo import main as ternary_demo
from match_case.demo import main as match_case_demo


def main():
    print("=" * 80)
    print("PYTHON CONTROL FLOW MODULE")
    print("=" * 80)

    if_else_demo()
    truthy_falsy_demo()
    logical_demo()
    short_circuit_demo()
    ternary_demo()
    match_case_demo()

    print("\nAll Control Flow demonstrations completed successfully.")


if __name__ == "__main__":
    main()