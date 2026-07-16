"""Leave eligibility rules for the employee management system."""

from app.models.employee import Employee


class LeavePolicy:
    """Determine whether an employee may request leave."""

    @staticmethod
    def is_eligible(employee: Employee) -> bool:
        """Employees with at least two years of service are eligible."""
        return employee.age >= 21
