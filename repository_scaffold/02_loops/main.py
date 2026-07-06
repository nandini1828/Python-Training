"""
Main entry point for the Loops module.
"""

from break_statement.demo import run_demo as break_demo
from continue_statement.demo import run_demo as continue_demo
from for_loop.demo import run_demo as for_demo
from loop_else.demo import run_demo as loop_else_demo
from pass_statement.demo import run_demo as pass_demo
from while_loop.demo import run_demo as while_demo


def main():
    print("=" * 80)
    print("PYTHON LOOPS MODULE")
    print("=" * 80)

    for_demo()
    while_demo()
    break_demo()
    continue_demo()
    pass_demo()
    loop_else_demo()

    print("\nAll Loops demonstrations completed successfully.")


if __name__ == "__main__":
    main()
