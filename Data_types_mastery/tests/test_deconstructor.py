import pytest

from classes.computer import Computer
from classes.object_deconstructor import deconstruct_object
from classes.student import Student


@pytest.fixture
def computer():
    cpu = Student("CPU", [4])
    return Computer("Dell", cpu)


def test_deconstruct_object_with_nested_instances(computer):
    result = deconstruct_object(computer)

    assert result == {
        "brand": "Dell",
        "cpu": {
            "name": "CPU",
            "grades": [4],
        },
    }