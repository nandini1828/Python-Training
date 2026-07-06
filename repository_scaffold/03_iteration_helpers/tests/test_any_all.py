"""
Unit tests for any_all utilities.
"""

from any_all.utils import (
    all_even,
    all_passwords_valid,
    all_positive,
    all_truthy,
    any_empty_string,
    any_positive,
    any_text_file,
    any_truthy,
    has_permissions,
    has_required_fields,
)


def test_any_truthy():
    assert any_truthy([0, 0, 5]) is True
    assert any_truthy([0, False, None]) is False


def test_all_truthy():
    assert all_truthy([1, "Python", True]) is True
    assert all_truthy([1, "", True]) is False


def test_any_positive():
    assert any_positive([-3, -1, 5]) is True
    assert any_positive([-5, -2, 0]) is False


def test_all_positive():
    assert all_positive([1, 2, 3]) is True
    assert all_positive([1, -2, 3]) is False


def test_all_even():
    assert all_even([2, 4, 6, 8]) is True
    assert all_even([2, 3, 6]) is False


def test_any_empty_string():
    assert any_empty_string(["Python", "", "Code"]) is True
    assert any_empty_string(["Python", "Code"]) is False


def test_all_passwords_valid():
    passwords = ["Password1", "Secure123", "Python@123"]
    assert all_passwords_valid(passwords) is True

    passwords = ["short", "Secure123"]
    assert all_passwords_valid(passwords) is False


def test_any_text_file():
    files = ["report.pdf", "notes.txt", "image.png"]
    assert any_text_file(files) is True

    files = ["report.pdf", "image.png"]
    assert any_text_file(files) is False


def test_has_required_fields():
    data = {
        "id": 101,
        "name": "Ganesh",
        "email": "ganesh@example.com",
    }

    assert has_required_fields(
        data,
        ["id", "name", "email"],
    ) is True

    assert has_required_fields(
        data,
        ["id", "phone"],
    ) is False


def test_has_permissions():
    permissions = ["read", "write", "execute"]

    assert has_permissions(
        permissions,
        ["read", "write"],
    ) is True

    assert has_permissions(
        permissions,
        ["read", "admin"],
    ) is False