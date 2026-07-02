"""
Entry point for Loop examples.
"""

from loops.for_loop import demo as for_demo
from loops.while_loop import demo as while_demo
from loops.break_continue_pass import demo as break_continue_demo
from loops.loop_else import demo as loop_else_demo


def title(text):
    print("\n" + "=" * 70)
    print(text.upper().center(70))
    print("=" * 70)


def subtitle(text):
    print("\n" + "-" * 70)
    print(text)
    print("-" * 70)


def main():

    title("Loop Foundations & Basic Iteration")

    subtitle("For Loop")
    for_demo()

    subtitle("While Loop")
    while_demo()

    subtitle("Break, Continue and Pass")
    break_continue_demo()

    subtitle("For-Else & While-Else")
    loop_else_demo()


if __name__ == "__main__":
    main()