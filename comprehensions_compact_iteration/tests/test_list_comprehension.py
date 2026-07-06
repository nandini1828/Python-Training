"""
Unit tests for list_comprehension.py
"""

from model import Employee
from list_comprehension import employee_names
from list_comprehension import high_salary


def test_employee_names(capsys):
    """
    Verify that all employee names are displayed.
    """

    employees = [
        Employee(101, "John", "IT", 75000),
        Employee(102, "Alice", "HR", 65000),
        Employee(103, "David", "Finance", 55000),
    ]

    employee_names(employees)

    captured = capsys.readouterr()

    assert "Employee Names" in captured.out
    assert "John" in captured.out
    assert "Alice" in captured.out
    assert "David" in captured.out


def test_high_salary(capsys):
    """
    Verify employees earning above ₹60,000 are displayed.
    """

    employees = [
        Employee(101, "John", "IT", 75000),
        Employee(102, "Alice", "HR", 65000),
        Employee(103, "David", "Finance", 55000),
        Employee(104, "Emma", "IT", 82000),
    ]

    high_salary(employees)

    captured = capsys.readouterr()

    assert "John" in captured.out
    assert "Alice" in captured.out
    assert "Emma" in captured.out
    assert "David" not in captured.out


def test_empty_employee_list(capsys):
    """
    Verify empty employee list handling.
    """

    employee_names([])

    captured = capsys.readouterr()

    assert "Employee Names" in captured.out