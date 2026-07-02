"""
Tests for truthy_falsy.py
"""

from conditionals import TruthyFalsyExamples


def test_truthy():
    assert TruthyFalsyExamples.is_truthy([1, 2])


def test_falsy():
    assert TruthyFalsyExamples.is_falsy([])


def test_empty_collection():
    assert (
        TruthyFalsyExamples.check_collection([])
        == "Collection Is Empty"
    )


def test_non_empty_collection():
    assert (
        TruthyFalsyExamples.check_collection([1])
        == "Collection Contains Data"
    )


def test_username():
    assert (
        TruthyFalsyExamples.check_username("Bhavya")
        == "Username Entered"
    )


def test_default_name():
    assert (
        TruthyFalsyExamples.get_default_name("")
        == "Guest"
    )


def test_login_validation():
    assert (
        TruthyFalsyExamples.validate_login(
            "admin",
            "123"
        )
        == "Login Request Accepted"
    )