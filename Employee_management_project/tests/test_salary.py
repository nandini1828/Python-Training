from models.employee import Employee
from services.salary_service import SalaryService


def test_annual_salary():
    employee = Employee(1, "Alice", "Engineering", 7000)
    assert SalaryService.annual_salary(employee) == 84000
