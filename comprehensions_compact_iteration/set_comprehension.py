def unique_departments(employees):

    print("\nUnique Departments")

    departments = {

        employee.department.lower()

        for employee in employees

    }

    print(departments)