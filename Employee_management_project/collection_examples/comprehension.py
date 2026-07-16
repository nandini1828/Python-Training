"""Employee data comprehensions."""

employee_names = ["Ava", "Leo", "Mina"]
department_names = ["Engineering", "HR", "Finance"]
employee_lookup = {name: department for name, department in zip(employee_names, department_names)}

department_summary = {
    department: [name for name, assigned_department in employee_lookup.items() if assigned_department == department]
    for department in sorted(set(employee_lookup.values()))
}
