"""
Main demo for the Python Loops Mastery project.

This script imports and exercises loop-related modules
in a single runnable demonstration.
"""

from loops.for_loops import (
    iterate_list,
    iterate_string,
    iterate_range,
)
from loops.while_loops import (
    count_with_while,
    sum_until_limit,
)
from loops.break_continue import (
    find_first_even,
    skip_even_numbers,
)
from loops.pass_statement import (
    pass_in_loop_demo,
    pass_in_condition_demo,
)
from loops.loop_else import (
    search_number_with_for_else,
    count_with_while_else,
)


def main() -> None:
    """
    Runs demo operations for all loop modules.
    """
    print("Python Loops Mastery Demo")
    print("=" * 72)

    print("\n1. FOR LOOPS")
    print("   iterate_list(['Python', 'Java', 'C']):", iterate_list(["Python", "Java", "C"]))
    print("   iterate_string('Karthik'):", iterate_string("Karthik"))
    print("   iterate_range(1, 6):", iterate_range(1, 6))

    print("\n2. WHILE LOOPS")
    print("   count_with_while(5):", count_with_while(5))
    print("   sum_until_limit(5):", sum_until_limit(5))

    print("\n3. BREAK / CONTINUE")
    print("   find_first_even([1, 3, 7, 8, 10]):", find_first_even([1, 3, 7, 8, 10]))
    print("   skip_even_numbers([1, 2, 3, 4, 5, 6]):", skip_even_numbers([1, 2, 3, 4, 5, 6]))

    print("\n4. PASS STATEMENT")
    print("   pass_in_loop_demo():", pass_in_loop_demo())
    print("   pass_in_condition_demo(10):", pass_in_condition_demo(10))

    print("\n5. FOR-ELSE / WHILE-ELSE")
    print("   search_number_with_for_else([10, 20, 30], 20):", search_number_with_for_else([10, 20, 30], 20))
    print("   search_number_with_for_else([10, 20, 30], 99):", search_number_with_for_else([10, 20, 30], 99))
    print("   count_with_while_else(3):", count_with_while_else(3))


if __name__ == "__main__":
    main()