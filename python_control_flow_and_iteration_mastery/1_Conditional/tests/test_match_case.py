"""
Tests for match_case.py
"""

from conditionals import MatchCaseExamples


def test_day():
    assert (
        MatchCaseExamples.day_name(1)
        == "Monday"
    )


def test_signal():
    assert (
        MatchCaseExamples.traffic_signal("green")
        == "Go"
    )


def test_addition():
    assert (
        MatchCaseExamples.calculator(
            10,
            20,
            "+"
        )
        == 30
    )


def test_http_status():
    assert (
        MatchCaseExamples.http_status(404)
        == "Not Found"
    )


def test_grade():
    assert (
        MatchCaseExamples.grade("A")
        == "Excellent"
    )


def test_role():
    assert (
        MatchCaseExamples.employee_role(
            "admin"
        )
        == "Full Access"
    )