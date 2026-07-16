"""Department lookup helpers."""

department_staff = {
    "Engineering": ["Ava", "Leo"],
    "HR": ["Mina"],
}


def add_employee_to_department(department: str, employee_name: str) -> dict[str, list[str]]:
    department_staff.setdefault(department, [])
    if employee_name not in department_staff[department]:
        department_staff[department].append(employee_name)
    return department_staff


def get_department_members(department: str) -> list[str]:
    return department_staff.get(department, [])
