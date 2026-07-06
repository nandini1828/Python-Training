from python_control_flow_mastery.loops.for_loop_examples import find_target, fibonacci_numbers
from python_control_flow_mastery.loops.while_loop_examples import countdown
from python_control_flow_mastery.loops.break_continue_pass import process_numbers
from python_control_flow_mastery.loops.loop_else_examples import search_value


def test_find_target_returns_index():
    assert find_target([4, 7, 9], 7) == 1


def test_find_target_returns_negative_one_when_missing():
    assert find_target([4, 7, 9], 11) == -1


def test_fibonacci_numbers_returns_expected_sequence():
    assert fibonacci_numbers(5) == [0, 1, 1, 2, 3]


def test_countdown_returns_expected_values():
    assert countdown(3) == [3, 2, 1, 0]


def test_process_numbers_skips_even_values():
    assert process_numbers([1, 2, 3, 4]) == [1, 3]


def test_search_value_reports_missing_value():
    assert search_value([2, 4, 6], 5) == "Value 5 not found."
