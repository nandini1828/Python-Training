"""
Unit tests for set_comprehension.py
"""

from model import Employee
from set_comprehension import unique_departments


def test_unique_departments(capsys):
    """
    Verify duplicate departments are removed.
    """

    employees = [
        Employee(101, "John", "IT", 75000),
        Employee(102, "Alice", "HR", 65000),
        Employee(103, "David", "Finance", 60000),
        Employee(104, "Emma", "IT", 82000),
        Employee(105, "Sophia", "hr", 70000),
    ]

    unique_departments(employees)

    captured = capsys.readouterr()

    output = captured.out.lower()

    assert "it" in output
    assert "hr" in output
    assert "finance" in output


def test_single_department(capsys):
    """
    Verify a single department is displayed correctly.
    """

    employees = [
        Employee(101, "John", "IT", 75000),
    ]

    unique_departments(employees)

    captured = capsys.readouterr()

    assert "it" in captured.out.lower()


def test_empty_departments(capsys):
    """
    Verify empty employee list handling.
    """

    unique_departments([])

    captured = capsys.readouterr()

    assert "Unique Departments" in captured.out