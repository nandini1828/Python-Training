"""General helper utilities used by the project."""

from app.models.employee import Employee


def get_employee_full_name(employee: Employee) -> str:
    """Return a formatted full name for an employee."""
    return f"{employee.first_name} {employee.last_name}".strip()


def is_truthy(value: object) -> bool:
    """Demonstrate truthy and falsy behavior in a readable helper."""
    return bool(value)
