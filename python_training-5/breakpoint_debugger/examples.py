"""
Examples of Breakpoint Debugging
"""


# Example 1

print("Example 1")


def add(a, b):
    result = a + b

    breakpoint()

    return result


print(add(10, 20))


# -------------------------------

print("\nExample 2")


numbers = [10, 20, 30, 40]

total = 0

for number in numbers:

    total += number

    breakpoint()

print(total)


# -------------------------------

print("\nExample 3")


student = {
    "name": "Nandini",
    "marks": 95
}

breakpoint()

print(student)


# -------------------------------

print("\nExample 4")


def divide(a, b):

    breakpoint()

    return a / b


print(divide(20, 5))


# -------------------------------

print("\nExample 5")


employees = [
    {"name": "Alice", "salary": 50000},
    {"name": "Bob", "salary": 60000},
]

for employee in employees:

    breakpoint()

    print(employee)