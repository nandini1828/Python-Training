"""
Unit tests for dictionary_comprehension.py
"""

from model import Employee
from dictionary_comprehension import salary_lookup


def test_salary_lookup(capsys):
    """
    Verify employee salary dictionary creation.
    """

    employees = [
        Employee(101, "John", "IT", 75000),
        Employee(102, "Alice", "HR", 65000),
    ]

    salary_lookup(employees)

    captured = capsys.readouterr()

    assert "Employee Salary Dictionary" in captured.out
    assert "John" in captured.out
    assert "75000" in captured.out
    assert "Alice" in captured.out
    assert "65000" in captured.out


def test_empty_salary_lookup(capsys):
    """
    Verify dictionary comprehension handles empty lists.
    """

    salary_lookup([])

    captured = capsys.readouterr()

    assert "Employee Salary Dictionary" in captured.out
    assert "{}" in captured.out