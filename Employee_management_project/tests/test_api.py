from api.employee_api import EmployeeAPI
from models.employee import Employee


def test_employee_api_add_and_list():
    api = EmployeeAPI()
    employee = Employee(1, "Alice", "Engineering", 7000)
    api.add_employee(employee)
    assert api.list_employees()[0].name == "Alice"
