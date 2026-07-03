"""
main.py

Entry point for the Loops and Iteration project.

This script provides an interactive menu to explore different loop concepts
through real-world inventory management examples.

Run:
    python main.py
"""

import for_loops
import while_loops
import break_continue_pass
import for_else_while_else


def display_menu() -> None:
    """Displays the available topics."""

    print("\n" + "=" * 50)
    print("   PYTHON LOOPS & ITERATION PLAYGROUND")
    print("=" * 50)
    print("1. For Loops (Iteration over sequences)")
    print("2. While Loops (Conditional iteration)")
    print("3. Break, Continue, Pass Statements")
    print("4. For-Else & While-Else Clauses")
    print("5. Run All Examples")
    print("0. Exit")
    print("=" * 50)


def run_choice(choice: str) -> bool:
    """
    Executes the selected module.

    Args:
        choice: User's menu selection

    Returns:
        False -> Exit Program
        True  -> Continue Program
    """

    match choice:

        case "1":
            print("\n" + "=" * 50)
            print("FOR LOOPS: Iterating over sequences")
            print("=" * 50)
            for_loops.run()

        case "2":
            print("\n" + "=" * 50)
            print("WHILE LOOPS: Conditional iteration")
            print("=" * 50)
            while_loops.run()

        case "3":
            print("\n" + "=" * 50)
            print("BREAK, CONTINUE, PASS: Loop control")
            print("=" * 50)
            break_continue_pass.run()

        case "4":
            print("\n" + "=" * 50)
            print("FOR-ELSE & WHILE-ELSE: Conditional execution")
            print("=" * 50)
            for_else_while_else.run()

        case "5":
            print("\n" + "=" * 50)
            print("RUNNING ALL EXAMPLES")
            print("=" * 50)
            
            print("\n--- FOR LOOPS ---")
            for_loops.run()
            
            print("\n\n--- WHILE LOOPS ---")
            while_loops.run()
            
            print("\n\n--- BREAK, CONTINUE, PASS ---")
            break_continue_pass.run()
            
            print("\n\n--- FOR-ELSE & WHILE-ELSE ---")
            for_else_while_else.run()

        case "0":
            print("\nThank you for learning Python loops! Goodbye! 👋\n")
            return False

        case _:
            print("\n❌ Invalid choice. Please select a valid option.\n")

    return True


def main() -> None:
    """
    Main loop for the interactive menu.
    """

    print("\n" + "=" * 50)
    print("Welcome to Python Loops & Iteration Training!")
    print("=" * 50)
    print("\nThis project demonstrates loop concepts through")
    print("a real-world Inventory Management System.")

    while True:
        display_menu()
        
        choice = input("\nEnter your choice: ").strip()
        
        if not run_choice(choice):
            break


if __name__ == "__main__":
    main()
