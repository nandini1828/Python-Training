"""
Unit tests for sorted_helper.py
"""

from model import Student
from sorted_helper import sort_students


def test_sorted_students(capsys):
    """
    Verify students are sorted by average marks
    in descending order.
    """

    students = [
        Student("David", 70, 70),
        Student("John", 95, 90),
        Student("Alice", 80, 85),
    ]

    sort_students(students)

    captured = capsys.readouterr()

    output = captured.out

    assert "John" in output
    assert "Alice" in output
    assert "David" in output

    assert output.index("John") < output.index("Alice")
    assert output.index("Alice") < output.index("David")