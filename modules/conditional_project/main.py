from modules.conditional_project.conditions.if_else import *
from modules.conditional_project.conditions.logical import *
from modules.conditional_project.conditions.truthy import *
from modules.conditional_project.conditions.short_circuit import *
from modules.conditional_project.conditions.ternary import *
from modules.conditional_project.conditions.match_case import *


def menu():
    print("\n========== Conditional Control Flow ==========")
    print("1. Grade Calculator")
    print("2. Loan Eligibility")
    print("3. Shopping Cart")
    print("4. Safe Division")
    print("5. Even or Odd")
    print("6. Day Name")
    print("7. Calculator")
    print("8. Exit")


def grade():
    marks = int(input("Marks: "))
    print("Grade:", calculate_grade(marks))


def loan():
    age = int(input("Age: "))
    salary = int(input("Salary: "))
    print("Eligible:", loan_eligibility(age, salary))


def cart():
    items = input("Enter items separated by commas: ")

    if items.strip():
        shopping_cart = [item.strip() for item in items.split(",")]
    else:
        shopping_cart = []

    print(cart_status(shopping_cart))


def division():
    numerator = int(input("Numerator: "))
    denominator = int(input("Denominator: "))
    print(safe_division(numerator, denominator))


def even_odd():
    number = int(input("Number: "))
    print(even_or_odd(number))


def day():
    day_number = int(input("Enter day number (1-7): "))
    print(day_name(day_number))


def calc():
    first = int(input("First Number: "))
    second = int(input("Second Number: "))
    operator = input("Operator (+,-,*,/): ")
    print(calculator(first, second, operator))


def main():

    actions = {
        "1": grade,
        "2": loan,
        "3": cart,
        "4": division,
        "5": even_odd,
        "6": day,
        "7": calc
    }

    while True:
        menu()

        choice = input("\nEnter Choice: ")

        if choice == "8":
            print("Thank you!")
            break

        action = actions.get(choice)

        if action:
            action()
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()