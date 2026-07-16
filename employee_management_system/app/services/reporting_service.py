"""Reporting helpers for salary and department summary calculations."""

from collections import defaultdict

from app.models.employee import Employee


class ReportingService:
    """Provide common reports for employee data."""

    @staticmethod
    def average_salary(employees: list[Employee]) -> float:
        """Return the average salary for a list of employees."""
        if not employees:
            return 0.0
        return round(sum(employee.salary for employee in employees) / len(employees), 2)

    @staticmethod
    def highest_salary(employees: list[Employee]) -> float:
        """Return highest salary from a list of employees."""
        if not employees:
            return 0.0
        return max(employee.salary for employee in employees)

    @staticmethod
    def lowest_salary(employees: list[Employee]) -> float:
        """Return lowest salary from a list of employees."""
        if not employees:
            return 0.0
        return min(employee.salary for employee in employees)

    @staticmethod
    def employees_per_department(employees: list[Employee]) -> dict[str, int]:
        """Count employees in each department."""
        counts: dict[str, int] = defaultdict(int)
        for employee in employees:
            counts[employee.department_id] += 1
        return dict(counts)
