"""
Main entry point for the Comprehensions module.

Run this file to execute demonstrations from all concepts.
"""

from dictionary_comprehension.demo import main as dict_demo
from list_comprehension.demo import main as list_demo
from nested_comprehension.demo import main as nested_demo
from set_comprehension.demo import main as set_demo


def main():
    print("=" * 80)
    print("PYTHON COMPREHENSIONS MODULE")
    print("=" * 80)

    list_demo()
    dict_demo()
    nested_demo()
    set_demo()

    print("\nAll Comprehension demonstrations completed successfully.")


if __name__ == "__main__":
    main()
