from Introspection.introspection import (
    list_public_attributes
)


def test_public_attributes():

    result = list_public_attributes([])

    assert "append" in result

    assert "__len__" not in result