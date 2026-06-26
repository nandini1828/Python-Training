from type_casting.exercises import (
    safe_cast,
    count_truthy_falsy
)


def test_safe_cast_int():

    assert safe_cast(
        "123",
        int
    ) == 123


def test_safe_cast_default():

    assert safe_cast(
        "abc",
        int,
        0
    ) == 0


def test_truthy_falsy():

    result = count_truthy_falsy(
        [0, "", 1, "hello"]
    )

    assert result["truthy"] == 2
    assert result["falsy"] == 2