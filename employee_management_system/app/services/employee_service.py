"""Service layer for employee operations."""

from app.models.address import Address
from app.models.employee import Employee
from app.repositories.employee_repository import EmployeeRepository


class EmployeeService:
    """Provide business operations for employees."""

    def __init__(self, repository: EmployeeRepository | None = None) -> None:
        self.repository = repository or EmployeeRepository()

    def add_employee(
        self,
        employee_id: str,
        first_name: str,
        last_name: str,
        age: int,
        email: str,
        department_id: str,
        salary: float,
        city: str,
        state: str,
        country: str,
        postal_code: str,
    ) -> Employee:
        """Add a new employee and persist the record."""
        employee = Employee(
            employee_id=employee_id,
            first_name=first_name,
            last_name=last_name,
            age=age,
            email=email,
            department_id=department_id,
            salary=salary,
            address=Address(city=city, state=state, country=country, postal_code=postal_code),
        )
        self.repository.add_employee(employee)
        return employee

    def get_employee_by_id(self, employee_id: str) -> Employee | None:
        """Return one employee if it exists."""
        return self.repository.get_employee_by_id(employee_id)

    def list_employees(self) -> list[Employee]:
        """Return all employees."""
        return self.repository.list_employees()

    def update_employee(self, employee: Employee) -> Employee:
        """Update an employee record."""
        self.repository.update_employee(employee)
        return employee

    def delete_employee(self, employee_id: str) -> bool:
        """Delete an employee by id."""
        return self.repository.delete_employee(employee_id)

    def search_employees(self, keyword: str) -> list[Employee]:
        """Search employees using a keyword."""
        return self.repository.search_employees(keyword)

    def filter_employees(self, department_id: str | None = None, minimum_salary: float | None = None) -> list[Employee]:
        """Filter employees by department and salary."""
        return self.repository.filter_employees(department_id=department_id, minimum_salary=minimum_salary)
