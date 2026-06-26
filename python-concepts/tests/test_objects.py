from oop_memory.exercises import (
    deconstruct_object
)


class CPU:

    def __init__(self, cores):
        self.cores = cores


class Computer:

    def __init__(
        self,
        brand,
        cpu
    ):
        self.brand = brand
        self.cpu = cpu


def test_deconstruct_object():

    pc = Computer(
        "Dell",
        CPU(8)
    )

    result = deconstruct_object(pc)

    assert result["brand"] == "Dell"

    assert (
        result["cpu"]["cores"]
        == 8
    )