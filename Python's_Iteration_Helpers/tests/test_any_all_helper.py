"""
Unit tests for any_all_helper.py
"""

from model import Student
from any_all_helper import distinction
from any_all_helper import all_pass


def test_any_distinction_true(capsys):

    students = [
        Student("John", 95, 95),
        Student("Alice", 60, 65),
    ]

    distinction(students)

    captured = capsys.readouterr()

    assert "True" in captured.out


def test_any_distinction_false(capsys):

    students = [
        Student("John", 70, 70),
        Student("Alice", 60, 65),
    ]

    distinction(students)

    captured = capsys.readouterr()

    assert "False" in captured.out


def test_all_students_pass(capsys):

    students = [
        Student("John", 90, 90),
        Student("Alice", 70, 80),
    ]

    all_pass(students)

    captured = capsys.readouterr()

    assert "True" in captured.out


def test_student_failed(capsys):

    students = [
        Student("John", 90, 90),
        Student("Alice", 20, 80),
    ]

    all_pass(students)

    captured = capsys.readouterr()

    assert "False" in captured.out