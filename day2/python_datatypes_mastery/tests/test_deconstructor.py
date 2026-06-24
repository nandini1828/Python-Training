from classes import (
    CPU,
    Computer,
    deconstruct_object
)


def test_object_deconstructor():

    computer = Computer(
        "Dell",
        CPU(8)
    )

    result = deconstruct_object(computer)

    assert result["brand"] == "Dell"

    assert result["cpu"]["cores"] == 8