import pytest
from python_control_flow_mastery.conditionals.if_else_examples import (
    grade_student,
    simulate_atm_menu,
    validate_login,
)
from python_control_flow_mastery.conditionals.truthy_falsy import describe_truthiness
from python_control_flow_mastery.conditionals.logical_operators import check_access
from python_control_flow_mastery.conditionals.short_circuit import safe_divide
from python_control_flow_mastery.conditionals.ternary_operator import choose_discount
from python_control_flow_mastery.conditionals.match_case_examples import handle_command


def test_grade_student_returns_expected_letter():
    assert grade_student(92) == "A"
    assert grade_student(74) == "C"


def test_validate_login_accepts_valid_credentials():
    assert validate_login("admin", "secret123") == "Login successful."


def test_validate_login_rejects_missing_credentials():
    assert validate_login("", "secret123") == "Username is required."


def test_simulate_atm_menu_balance_and_withdraw_paths():
    assert simulate_atm_menu(100.0, "balance") == "Your balance is $100.00."
    assert simulate_atm_menu(40.0, "withdraw") == "Insufficient funds."
    assert simulate_atm_menu(100.0, "deposit") == "Deposit service is available."


@pytest.mark.parametrize("value, expected", [(0, "falsy"), ("hello", "truthy"), ([], "falsy")])
def test_describe_truthiness(value, expected):
    assert describe_truthiness(value) == expected


def test_check_access_for_admin():
    assert check_access("admin", True, True) == "Full access granted."


def test_check_access_for_guest_and_denied_users():
    assert check_access("guest", True, True) == "Limited access."
    assert check_access("member", True, False) == "Access denied."


def test_safe_divide_returns_none_for_zero_divisor():
    result, message = safe_divide(10, 0)
    assert result is None
    assert message == "Cannot divide by zero."


def test_safe_divide_returns_quotient_for_valid_input():
    result, message = safe_divide(10, 2)
    assert result == 5.0
    assert message == "Division successful."


def test_choose_discount_for_members():
    assert choose_discount(True) == 20


def test_handle_command_switches():
    assert handle_command("start") == "Starting the workflow."
    assert handle_command("unknown") == "Unknown command."
