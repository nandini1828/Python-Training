from model import Employee

from utils import print_title

from list_comprehension import employee_names, high_salary
from dictionary_comprehension import salary_lookup
from set_comprehension import unique_departments
from nested_comprehension import flatten_office, seating_layout


def main():

    employees = [

        Employee(101,"John","IT",75000),
        Employee(102,"Alice","HR",65000),
        Employee(103,"David","Finance",55000),
        Employee(104,"Emma","IT",82000),
        Employee(105,"Sophia","hr",70000)

    ]

    print_title("Employee Management System")

    employee_names(employees)

    high_salary(employees)

    salary_lookup(employees)

    unique_departments(employees)

    flatten_office()

    seating_layout()


if __name__ == "__main__":

    main()