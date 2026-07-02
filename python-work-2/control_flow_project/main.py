"""
Entry point for the Control Flow project.
"""

from utils.printer import title, subtitle

from control_flow.if_else import demo as if_else_demo
from control_flow.logical_operators import demo as logical_operators_demo
from control_flow.short_circuit import demo as short_circuit_demo
from control_flow.ternary import demo as ternary_demo
from control_flow.match_case import demo as match_case_demo


def main():
    """Run all Control Flow examples."""

    title("Control Flow & Decision Making")

    subtitle("if - elif - else")
    if_else_demo()

    subtitle("Logical Operators")
    logical_operators_demo()

    subtitle("Short Circuit Evaluation")
    short_circuit_demo()

    subtitle("Ternary Operator")
    ternary_demo()

    subtitle("Match Case")
    match_case_demo()


if __name__ == "__main__":
    main()