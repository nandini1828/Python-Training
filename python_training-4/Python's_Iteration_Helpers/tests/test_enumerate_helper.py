"""
Unit tests for enumerate_helper.py
"""

from model import Student
from enumerate_helper import display_students


def test_display_students(capsys):

    students = [
        Student("John", 90, 80),
        Student("Alice", 85, 95),
        Student("David", 70, 75),
    ]

    display_students(students)

    captured = capsys.readouterr()

    assert "Student Attendance" in captured.out
    assert "1. John" in captured.out
    assert "2. Alice" in captured.out
    assert "3. David" in captured.out


def test_empty_student_list(capsys):

    display_students([])

    captured = capsys.readouterr()

    assert "Student Attendance" in captured.out