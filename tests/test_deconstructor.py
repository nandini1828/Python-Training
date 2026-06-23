from classes.computer import Computer
from classes.object_deconstructor import deconstruct_object
from classes.student import Student


def test_deconstruct_object_with_nested_instances():
    cpu = Student("CPU", [4])
    computer = Computer("Dell", cpu)
    result = deconstruct_object(computer)
    assert result == {"brand": "Dell", "cpu": {"name": "CPU", "grades": [4]}}
