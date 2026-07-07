"""
main.py

Entry point for the Iterators & Generators project.

Run:
    python main.py
"""

import iterators_generators


def display_menu() -> None:
    """Display available iterator and generator topics."""
    print("\n" + "=" * 60)
    print("    PYTHON ITERATORS & GENERATORS PLAYGROUND")
    print("=" * 60)
    print("1. Iterator Protocol")
    print("2. Generators with yield")
    print("3. Generator Expressions")
    print("4. Run All Examples")
    print("0. Exit")
    print("=" * 60)


def run_choice(choice: str) -> bool:
    """Run the selected example."""
    match choice:
        case "1":
            iterators_generators.IteratorExample([10, 20, 30])
            for value in iterators_generators.IteratorExample([10, 20, 30]):
                print(f"  -> {value}")
        case "2":
            iterators_generators.run()
        case "3":
            values = [1, 2, 3, 4]
            squares = iterators_generators.generator_expression_example(values)
            print("\nGenerator expression squares:")
            for value in squares:
                print(f"  -> {value}")
        case "4":
            iterators_generators.run()
        case "0":
            print("\nThanks for learning iterators and generators! Goodbye! 👋\n")
            return False
        case _:
            print("\n❌ Invalid choice. Please select a valid option.\n")
    return True


def main() -> None:
    """Start the interactive menu."""
    print("\nWelcome to Python Iterators & Generators Training!")
    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()
        if not run_choice(choice):
            break


if __name__ == "__main__":
    main()
