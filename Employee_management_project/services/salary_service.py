"""Salary calculation helpers."""

from models.employee import Employee


class SalaryService:
    """Simple salary-related operations."""

    @staticmethod
    def monthly_salary(employee: Employee) -> float:
        return employee.salary

    @staticmethod
    def annual_salary(employee: Employee) -> float:
        return employee.salary * 12

    @staticmethod
    def salary_with_bonus(employee: Employee, bonus_percent: float = 0.1) -> float:
        return employee.salary * (1 + bonus_percent)
