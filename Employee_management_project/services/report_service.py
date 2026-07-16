"""Report generation helpers."""

from typing import Any, List

from models.employee import Employee


class ReportService:
    """Simple report service."""

    @staticmethod
    def employee_report(employees: List[Employee]) -> List[str]:
        return [f"{employee.name}: {employee.department}" for employee in employees]

    @staticmethod
    def summary_report(employees: List[Employee]) -> dict[str, Any]:
        return {
            "employee_count": len(employees),
            "departments": sorted({employee.department for employee in employees}),
            "highest_salary": max((employee.salary for employee in employees), default=0.0),
        }
