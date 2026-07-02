"""
main.py

Entry point for the Control Flow project.

Run:
    python main.py
"""

import conditionals
import truthy_falsy
import logical_operators
import short_circuit
import ternary_operator
import pattern_matching


def display_menu() -> None:
    """Displays the available topics."""

    print("\n" + "=" * 45)
    print("      PYTHON CONTROL FLOW PLAYGROUND")
    print("=" * 45)
    print("1. Conditionals")
    print("2. Truthy & Falsy")
    print("3. Logical Operators")
    print("4. Short-Circuit Evaluation")
    print("5. Ternary Operator")
    print("6. Pattern Matching")
    print("7. Run All Examples")
    print("0. Exit")
    print("=" * 45)


def run_choice(choice: str) -> bool:
    """
    Executes the selected module.

    Returns:
        False -> Exit Program
        True  -> Continue Program
    """

    match choice:

        case "1":
            conditionals.run()

        case "2":
            truthy_falsy.run()

        case "3":
            logical_operators.run()

        case "4":
            short_circuit.run()

        case "5":
            ternary_operator.run()

        case "6":
            pattern_matching.run()

        case "7":
            print("\nRunning All Modules...\n")

            conditionals.run()
            truthy_falsy.run()
            logical_operators.run()
            short_circuit.run()
            ternary_operator.run()
            pattern_matching.run()

        case "0":
            print("\nThank you for learning Python Control Flow!")
            return False

        case _:
            print("\nInvalid choice. Please try again.")

    return True


def main() -> None:
    """Main application loop."""

    while True:

        display_menu()

        choice = input("Enter your choice: ").strip()

        if not run_choice(choice):
            break


if __name__ == "__main__":
    main()