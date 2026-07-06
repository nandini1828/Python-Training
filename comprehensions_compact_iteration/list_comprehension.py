def employee_names(employees):

    print("\nEmployee Names")

    names = [

        employee.name

        for employee in employees

    ]

    print(names)


def high_salary(employees):

    print("\nEmployees With Salary Above ₹60,000")

    result = [

        employee.name

        for employee in employees

        if employee.salary > 60000

    ]

    print(result)