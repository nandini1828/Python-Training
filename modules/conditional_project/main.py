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


def main():

    while True:

        menu()

        choice = input("\nEnter Choice: ")

        match choice:

            case "1":
                marks = int(input("Marks: "))
                print("Grade:", calculate_grade(marks))

            case "2":
                age = int(input("Age: "))
                salary = int(input("Salary: "))
                print("Eligible:", loan_eligibility(age, salary))

            case "3":
                items = input("Enter items separated by commas: ")

                cart = (
                    [item.strip() for item in items.split(",")]
                    if items.strip()
                    else []
                )

                print(cart_status(cart))

            case "4":
                a = int(input("Numerator: "))
                b = int(input("Denominator: "))
                print(safe_division(a, b))

            case "5":
                number = int(input("Number: "))
                print(even_or_odd(number))

            case "6":
                day = int(input("Enter day number (1-7): "))
                print(day_name(day))

            case "7":
                a = int(input("First Number: "))
                b = int(input("Second Number: "))
                op = input("Operator (+,-,*,/): ")
                print(calculator(a, b, op))

            case "8":
                print("Thank you!")
                break

            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()