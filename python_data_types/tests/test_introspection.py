from introspection import (
    get_type,
    get_id,
    get_public_attributes
)


def test_get_type(dog):
    assert get_type(dog).__name__ == "Dog"


def test_get_id(dog):
    assert isinstance(get_id(dog), int)


def test_public_attributes(dog):
    attrs = get_public_attributes(dog)
    assert "bark" in attrs