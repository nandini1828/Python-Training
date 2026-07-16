"""Employee statistics helpers."""

from typing import List

from models.employee import Employee


class StatisticsService:
    """Provide basic statistics."""

    @staticmethod
    def average_salary(employees: List[Employee]) -> float:
        if not employees:
            return 0.0
        return sum(employee.salary for employee in employees) / len(employees)

    @staticmethod
    def highest_salary(employees: List[Employee]) -> float:
        return max((employee.salary for employee in employees), default=0.0)

    @staticmethod
    def department_counts(employees: List[Employee]) -> dict[str, int]:
        counts: dict[str, int] = {}
        for employee in employees:
            counts[employee.department] = counts.get(employee.department, 0) + 1
        return counts
