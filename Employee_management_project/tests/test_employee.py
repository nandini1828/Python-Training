from models.employee import Employee


def test_employee_creation():
    employee = Employee(1, "Alice", "Engineering", 7000)
    assert employee.name == "Alice"
    assert employee.department == "Engineering"
