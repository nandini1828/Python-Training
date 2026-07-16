"""Employee list helpers."""

employee_ids = [101, 102, 103]


def add_employee_id(employee_id: int) -> list[int]:
    if employee_id not in employee_ids:
        employee_ids.append(employee_id)
    return employee_ids


def get_employee_ids() -> list[int]:
    return list(employee_ids)
