from modules.conditional_project.conditions.logical import *


def test_loan_eligible():
    assert loan_eligibility(25, 50000) is True


def test_loan_not_eligible():
    assert loan_eligibility(18, 50000) is False


def test_login_success():
    assert login("admin", "python123") is True


def test_login_failure():
    assert login("admin", "wrong") is False


def test_weekend():
    assert weekend("Sunday") is True


def test_weekday():
    assert weekend("Monday") is False


def test_active():
    assert account_active(True) == "Account Active"


def test_disabled():
    assert account_active(False) == "Account Disabled"


def test_student_pass():
    assert student_passed(70, 90) is True


def test_student_fail():
    assert student_passed(70, 60) is False