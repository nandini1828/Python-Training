"""Search and filter services."""

from typing import List

from models.employee import Employee


class SearchService:
    """Search employees by department, name, or salary."""

    @staticmethod
    def search_by_department(employees: List[Employee], department: str) -> List[Employee]:
        return [employee for employee in employees if employee.department.lower() == department.lower()]

    @staticmethod
    def search_by_name(employees: List[Employee], name: str) -> List[Employee]:
        return [employee for employee in employees if name.lower() in employee.name.lower()]

    @staticmethod
    def filter_by_salary(employees: List[Employee], minimum_salary: float) -> List[Employee]:
        return [employee for employee in employees if employee.salary >= minimum_salary]
