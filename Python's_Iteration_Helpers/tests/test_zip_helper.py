"""
Unit tests for zip_helper.py
"""

from model import Student
from zip_helper import compare_subject_marks
from zip_helper import compare_extra_subject


def test_compare_subject_marks(capsys):

    students = [
        Student("John", 90, 80),
        Student("Alice", 95, 92),
    ]

    compare_subject_marks(students)

    captured = capsys.readouterr()

    assert "Maths and Science Marks" in captured.out
    assert "Maths: 90, Science: 80" in captured.out
    assert "Maths: 95, Science: 92" in captured.out


def test_compare_extra_subject(capsys):

    compare_extra_subject()

    captured = capsys.readouterr()

    assert "John AI Project" in captured.out
    assert "Alice ML Project" in captured.out
    assert "Not Assigned Cloud Project" in captured.out