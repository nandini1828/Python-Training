from collections import defaultdict

# Employees stored as tuples: (name, department)
employees = defaultdict(list)


def add_employee():
    """Add a new employee and automatically create the department group."""
    name = input("Enter employee name: ").strip()
    department = input("Enter department name: ").strip()

    if not name or not department:
        print("Name and department cannot be empty.")
        return

    employees[department].append((name, department))
    print(f"Added {name} to {department}.")


def view_all_departments():
    """Show all departments currently available."""
    if not employees:
        print("No departments available.")
        return

    print("Departments:")
    for department in sorted(employees.keys()):
        print(f"- {department}")


def view_employees_in_department():
    """Show employees in a chosen department."""
    department = input("Enter department name: ").strip()
    department_members = employees[department]

    if not department_members:
        print(f"No employees found in {department}.")
        return

    print(f"Employees in {department}:")
    for name, dept in department_members:
        print(f"- {name} ({dept})")


def search_employee():
    """Find an employee and display their department."""
    name = input("Enter employee name to search: ").strip()
    found = False

    for department, members in employees.items():
        for employee_name, employee_department in members:
            if employee_name.lower() == name.lower():
                print(f"{employee_name} works in {employee_department}.")
                found = True
                break
        if found:
            break

    if not found:
        print("Employee not found.")


def display_employee_count_by_department():
    """Show the number of employees in each department."""
    if not employees:
        print("No employee records available.")
        return

    print("Employee count by department:")
    for department in sorted(employees.keys()):
        print(f"- {department}: {len(employees[department])}")


def main():
    """Run the employee directory menu."""
    while True:
        print("\n=== Employee Directory ===")
        print("1. Add Employee")
        print("2. View All Departments")
        print("3. View Employees in a Department")
        print("4. Search Employee")
        print("5. Display Employee Count by Department")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_all_departments()
        elif choice == "3":
            view_employees_in_department()
        elif choice == "4":
            search_employee()
        elif choice == "5":
            display_employee_count_by_department()
        elif choice == "6":
            print("Exiting Employee Directory. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
