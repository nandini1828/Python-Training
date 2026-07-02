from utils.printer import title

from control_flow.if_else import demo as if_demo
from control_flow.truthy_falsy import demo as truth_demo
from control_flow.logical_operators import demo as logical_demo
from control_flow.short_circuit import demo as short_demo
from control_flow.ternary import demo as ternary_demo
from control_flow.match_case import demo as match_demo

from loops.for_loop import demo as for_demo
from loops.while_loop import demo as while_demo
from loops.break_continue_pass import demo as break_demo
from loops.loop_else import demo as else_demo

from iteration_helpers.range_examples import demo as range_demo
from iteration_helpers.enumerate_examples import demo as enum_demo
from iteration_helpers.zip_examples import demo as zip_demo
from iteration_helpers.reversed_sorted import demo as reverse_demo
from iteration_helpers.any_all import demo as any_demo

from data_structures.lists import demo as list_demo
from data_structures.list_modification import demo as modification_demo
from data_structures.dictionaries import demo as dictionary_demo
from data_structures.dictionary_safety import demo as dictionary_safety_demo
from data_structures.sets import demo as set_demo

from comprehensions.list_comprehension import demo as list_comp_demo
from comprehensions.dictionary_comprehension import demo as dict_comp_demo
from comprehensions.set_comprehension import demo as set_comp_demo
from comprehensions.nested_comprehension import demo as nested_comp_demo

from iterators_generators.iterator_protocol import demo as iterator_demo
from iterators_generators.generators import demo as generator_demo
from iterators_generators.generator_expression import demo as generator_expression_demo


def main():

    title("Part 1: Conditional Control Flow & Decision Making")

    if_demo()
    truth_demo()
    logical_demo()
    short_demo()
    ternary_demo()
    match_demo()

    title("Part 2: Loop Foundations & Basic Iteration")

    for_demo()
    while_demo()
    break_demo()
    else_demo()

    title("Part 3: Python's Iteration Helpers")

    range_demo()
    enum_demo()
    zip_demo()
    reverse_demo()
    any_demo()

    title("Part 4: Data Structure Iteration & Safety")

    list_demo()
    modification_demo()
    dictionary_demo()
    dictionary_safety_demo()
    set_demo()

    title("Part 5: Comprehensions (Compact Iteration)")

    list_comp_demo()
    dict_comp_demo()
    set_comp_demo()
    nested_comp_demo()

    title("Part 6: Iterators & Generators (Under the Hood)")

    iterator_demo()
    generator_demo()
    generator_expression_demo()


if __name__ == "__main__":
    main()