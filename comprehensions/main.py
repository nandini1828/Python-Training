"""
main.py

Entry point for the Comprehensions project.

Run:
    python main.py
"""

import comprehensions


def display_menu() -> None:
    """Display available comprehension topics."""
    print("\n" + "=" * 60)
    print("    PYTHON COMPREHENSIONS PLAYGROUND")
    print("=" * 60)
    print("1. List Comprehensions")
    print("2. Dictionary Comprehensions")
    print("3. Set Comprehensions")
    print("4. Nested Comprehensions")
    print("5. Run All Examples")
    print("0. Exit")
    print("=" * 60)


def run_choice(choice: str) -> bool:
    """Run the selected example."""
    match choice:
        case "1":
            comprehensions.list_comprehension_example()
        case "2":
            comprehensions.dictionary_comprehension_example()
        case "3":
            comprehensions.set_comprehension_example()
        case "4":
            comprehensions.nested_comprehension_example()
        case "5":
            comprehensions.run()
        case "0":
            print("\nThanks for learning comprehensions! Goodbye! 👋\n")
            return False
        case _:
            print("\n❌ Invalid choice. Please select a valid option.\n")
    return True


def main() -> None:
    """Start the interactive menu."""
    print("\nWelcome to Python Comprehensions Training!")
    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()
        if not run_choice(choice):
            break


if __name__ == "__main__":
    main()
