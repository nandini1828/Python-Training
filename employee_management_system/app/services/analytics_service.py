"""Analytics helpers for basic employee summaries."""

from app.models.employee import Employee
from app.services.reporting_service import ReportingService


class AnalyticsService:
    """Small analytics service built on top of reporting helpers."""

    @staticmethod
    def department_wise_employee_count(employees: list[Employee]) -> dict[str, int]:
        """Return the number of employees in each department."""
        return ReportingService.employees_per_department(employees)
