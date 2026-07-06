def salary_lookup(employees):

    print("\nEmployee Salary Dictionary")

    salaries = {

        employee.name: employee.salary

        for employee in employees

    }

    print(salaries)