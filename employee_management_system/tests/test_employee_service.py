"""Tests for employee service behavior."""

from app.models.address import Address
from app.models.employee import Employee
from app.repositories.employee_repository import EmployeeRepository
from app.services.employee_service import EmployeeService


class DummyRepository:
    """Simple fake repository used for unit testing."""

    def __init__(self) -> None:
        self.employees: list[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)

    def list_employees(self) -> list[Employee]:
        return self.employees

    def get_employee_by_id(self, employee_id: str) -> Employee | None:
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None

    def update_employee(self, employee: Employee) -> None:
        for index, existing in enumerate(self.employees):
            if existing.employee_id == employee.employee_id:
                self.employees[index] = employee
                return

    def delete_employee(self, employee_id: str) -> bool:
        for index, employee in enumerate(self.employees):
            if employee.employee_id == employee_id:
                self.employees.pop(index)
                return True
        return False

    def search_employees(self, keyword: str) -> list[Employee]:
        return [employee for employee in self.employees if keyword.lower() in employee.first_name.lower()]

    def filter_employees(self, department_id: str | None = None, minimum_salary: float | None = None) -> list[Employee]:
        result = self.employees
        if department_id is not None:
            result = [employee for employee in result if employee.department_id == department_id]
        if minimum_salary is not None:
            result = [employee for employee in result if employee.salary >= minimum_salary]
        return result


def test_add_employee_uses_service():
    """Adding an employee stores a record in the repository."""
    repo = DummyRepository()
    service = EmployeeService(repository=repo)

    employee = service.add_employee(
        employee_id="E010",
        first_name="Grace",
        last_name="Lee",
        age=29,
        email="grace@example.com",
        department_id="D001",
        salary=50000,
        city="Boston",
        state="MA",
        country="USA",
        postal_code="02108",
    )

    assert employee.employee_id == "E010"
    assert len(repo.employees) == 1


def test_get_employee_by_id_returns_employee():
    """The service should return a saved employee by id."""
    repo = DummyRepository()
    service = EmployeeService(repository=repo)
    employee = Employee(
        employee_id="E011",
        first_name="Hank",
        last_name="Ford",
        age=32,
        email="hank@example.com",
        department_id="D001",
        salary=65000,
        address=Address(city="Seattle", state="WA", country="USA", postal_code="98101"),
    )
    repo.add_employee(employee)

    result = service.get_employee_by_id("E011")

    assert result is not None
    assert result.first_name == "Hank"
