"""
demo.py

Practical demonstrations of Python Structural Pattern Matching
introduced in Python 3.10.

Run:
    python demo.py
"""


def day_of_week(day):
    print("\n===== Day of Week =====")

    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Invalid Day")


def calculator(a, b, operator):
    print("\n===== Calculator =====")

    match operator:
        case "+":
            print(f"Result: {a + b}")
        case "-":
            print(f"Result: {a - b}")
        case "*":
            print(f"Result: {a * b}")
        case "/":
            if b != 0:
                print(f"Result: {a / b}")
            else:
                print("Division by Zero")
        case _:
            print("Invalid Operator")


def http_status(code):
    print("\n===== HTTP Status =====")

    match code:
        case 200:
            print("OK")
        case 201:
            print("Created")
        case 400:
            print("Bad Request")
        case 401:
            print("Unauthorized")
        case 404:
            print("Not Found")
        case 500:
            print("Internal Server Error")
        case _:
            print("Unknown Status")


def user_role(role):
    print("\n===== User Role =====")

    match role:
        case "admin":
            print("Full Access")
        case "manager":
            print("Manager Dashboard")
        case "employee":
            print("Employee Portal")
        case "guest":
            print("Limited Access")
        case _:
            print("Unknown Role")


def grade_system(grade):
    print("\n===== Grade System =====")

    match grade:
        case "A" | "A+":
            print("Excellent")
        case "B" | "B+":
            print("Very Good")
        case "C":
            print("Good")
        case "D":
            print("Average")
        case _:
            print("Fail")


def tuple_matching(point):
    print("\n===== Tuple Matching =====")

    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y-Axis : {y}")
        case (x, 0):
            print(f"X-Axis : {x}")
        case (x, y):
            print(f"Point ({x}, {y})")


def list_matching(numbers):
    print("\n===== List Matching =====")

    match numbers:
        case []:
            print("Empty List")
        case [x]:
            print(f"Single Element : {x}")
        case [x, y]:
            print(f"Two Elements : {x}, {y}")
        case [first, *remaining]:
            print(f"First : {first}")
            print(f"Remaining : {remaining}")


def dictionary_matching(student):
    print("\n===== Dictionary Matching =====")

    match student:
        case {"name": name, "age": age}:
            print(f"Name : {name}")
            print(f"Age : {age}")
        case _:
            print("Invalid Dictionary")


def age_category(age):
    print("\n===== Guard Condition =====")

    match age:
        case age if age < 18:
            print("Minor")
        case age if age < 60:
            print("Adult")
        case _:
            print("Senior Citizen")


def command_parser(command):
    print("\n===== Command Parser =====")

    match command.lower():
        case "start":
            print("Application Started")
        case "stop":
            print("Application Stopped")
        case "restart":
            print("Application Restarted")
        case "exit":
            print("Good Bye")
        case _:
            print("Unknown Command")


def main():
    print("=" * 60)
    print("MATCH CASE DEMONSTRATIONS")
    print("=" * 60)

    day_of_week(3)
    calculator(20, 5, "+")
    http_status(404)
    user_role("manager")
    grade_system("A+")
    tuple_matching((10, 20))
    list_matching([1, 2, 3, 4])
    dictionary_matching({"name": "Ganesh", "age": 22})
    age_category(65)
    command_parser("restart")

    print("\nAll demonstrations completed successfully.")


if __name__ == "__main__":
    main()