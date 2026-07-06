"""
Main entry point for the Iterators & Generators module.

Run this file to execute demonstrations from all concepts.
"""

from generator_expressions.demo import main as generator_expr_demo
from generators.demo import main as generator_demo
from iterator_protocol.demo import main as iterator_demo


def main():
    print("=" * 80)
    print("PYTHON ITERATORS & GENERATORS MODULE")
    print("=" * 80)

    iterator_demo()
    generator_demo()
    generator_expr_demo()

    print("\nAll Iterators & Generators demonstrations completed successfully.")


if __name__ == "__main__":
    main()
