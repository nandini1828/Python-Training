from python_control_flow_mastery.iterators_generators.custom_iterator import CounterIterator
from python_control_flow_mastery.iterators_generators.generators import count_up_to
from python_control_flow_mastery.iterators_generators.generator_expressions import even_numbers


def test_counter_iterator_yields_expected_values():
    iterator = CounterIterator(3)
    assert list(iterator) == [0, 1, 2]


def test_count_up_to_returns_expected_values():
    assert list(count_up_to(4)) == [0, 1, 2, 3]


def test_even_numbers_generates_even_values():
    assert list(even_numbers(5)) == [0, 2, 4]
