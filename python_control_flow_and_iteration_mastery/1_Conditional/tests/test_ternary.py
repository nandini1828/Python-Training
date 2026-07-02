"""
Tests for ternary.py
"""

from conditionals import TernaryExamples


def test_even():
    assert (
        TernaryExamples.even_or_odd(8)
        == "Even"
    )


def test_odd():
    assert (
        TernaryExamples.even_or_odd(7)
        == "Odd"
    )


def test_pass():
    assert (
        TernaryExamples.pass_or_fail(70)
        == "Pass"
    )


def test_fail():
    assert (
        TernaryExamples.pass_or_fail(20)
        == "Fail"
    )


def test_largest():
    assert (
        TernaryExamples.largest(20, 10)
        == 20
    )


def test_voting():
    assert (
        TernaryExamples.voting_status(25)
        == "Eligible"
    )


def test_login():
    assert (
        TernaryExamples.login_message(True)
        == "Welcome"
    )