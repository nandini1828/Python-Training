"""Employee profile tuple helpers."""

employee_profile = ("Ava", "Engineering", "Senior")


def update_employee_profile(name: str, department: str, role: str) -> tuple[str, str, str]:
    global employee_profile
    employee_profile = (name, department, role)
    return employee_profile
