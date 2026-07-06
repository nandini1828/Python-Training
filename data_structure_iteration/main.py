"""
main.py

Entry point for the Data Structure Iteration project.

This script provides an interactive menu for learning safe iteration
patterns with lists, dictionaries, and sets.

Run:
    python main.py
"""

from data_structure_iteration import (
    dictionary_iteration,
    dictionary_key_protection,
    list_iteration_and_slicing,
    list_modification_trap,
    run as data_structure_run,
    set_membership_and_looping,
)


def display_menu() -> None:
    """Displays the available topics."""
    print("\n" + "=" * 60)
    print("    PYTHON DATA STRUCTURE ITERATION PLAYGROUND")
    print("=" * 60)
    print("1. Lists: iteration and slicing")
    print("2. List Modification Trap")
    print("3. Dictionaries: keys, values, items")
    print("4. Dictionary Key Protection")
    print("5. Sets: membership and looping")
    print("6. Run All Examples")
    print("0. Exit")
    print("=" * 60)


def run_choice(choice: str) -> bool:
    """
    Executes the selected module.

    Args:
        choice: User's menu selection

    Returns:
        False -> Exit Program
        True  -> Continue Program
    """
    products = ["Laptop", "Mouse", "Monitor", "Keyboard"]

    match choice:

        case "1":
            print("\n" + "=" * 60)
            print("LISTS: Iteration and slicing")
            print("=" * 60)
            list_iteration_and_slicing(products)

        case "2":
            print("\n" + "=" * 60)
            print("LIST MODIFICATION TRAP")
            print("=" * 60)
            list_modification_trap()

        case "3":
            print("\n" + "=" * 60)
            print("DICTIONARIES: keys(), values(), items()")
            print("=" * 60)
            dictionary_iteration(products, [15, 0, 8, 25])

        case "4":
            print("\n" + "=" * 60)
            print("DICTIONARY KEY PROTECTION")
            print("=" * 60)
            dictionary_key_protection()

        case "5":
            print("\n" + "=" * 60)
            print("SETS: Membership and looping")
            print("=" * 60)
            set_membership_and_looping(products)

        case "6":
            print("\n" + "=" * 60)
            print("RUNNING ALL DATA STRUCTURE ITERATION EXAMPLES")
            print("=" * 60)
            data_structure_run()

        case "0":
            print("\nThanks for learning data structure iteration! Goodbye! 👋\n")
            return False

        case _:
            print("\n❌ Invalid choice. Please select a valid option.\n")

    return True


def main() -> None:
    """
    Main loop for the interactive menu.
    """
    print("\n" + "=" * 60)
    print("Welcome to Python Data Structure Iteration Training!")
    print("=" * 60)
    print("\nThis project demonstrates safe iteration patterns with lists,")
    print("dictionaries, and sets.")

    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()
        if not run_choice(choice):
            break


if __name__ == "__main__":
    main()
