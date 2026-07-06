"""
Unit tests for short_circuit utilities.
"""

from short_circuit.utils import (
    authenticate,
    can_access_system,
    cart_has_items,
    get_cached_value,
    get_display_name,
    get_file_content,
    get_user_name,
    load_configuration,
    safe_division,
    validate_age,
)


def test_safe_division():
    assert safe_division(10, 2) == 5
    assert safe_division(10, 0) is False


def test_get_display_name():
    assert get_display_name("Ganesh") == "Ganesh"
    assert get_display_name("") == "Guest"


def test_authenticate():
    assert authenticate("admin", "python") is True
    assert authenticate("", "python") is False
    assert authenticate("admin", "") is False


def test_get_user_name():
    response = {
        "data": {
            "name": "Ganesh"
        }
    }

    assert get_user_name(response) == "Ganesh"
    assert get_user_name({}) is None


def test_load_configuration():
    assert load_configuration("User Config") == "User Config"
    assert load_configuration(None) == "Default Configuration"


def test_cart_has_items():
    assert cart_has_items(["Laptop"]) is True
    assert cart_has_items([]) is False


def test_get_file_content():
    assert get_file_content("Python") == "Python"
    assert get_file_content("") == "Using Backup File"


def test_can_access_system():
    assert can_access_system(True, True) is True
    assert can_access_system(True, False) is False
    assert can_access_system(False, True) is False


def test_get_cached_value():
    cache = {"python": "Programming Language"}

    assert get_cached_value(cache, "python") == "Programming Language"
    assert get_cached_value(cache, "java") == "Fetching from Database..."


def test_validate_age():
    assert validate_age(25) is True
    assert validate_age(16) is False
    assert validate_age(65) is False