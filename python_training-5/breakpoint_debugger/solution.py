"""
Solutions

Insert breakpoints at the suggested locations.
"""


# Exercise 1

numbers = [5, 10, 15]

total = 0

for number in numbers:

    breakpoint()

    total += number

print(total)


# ------------------------


def multiply(a, b):

    breakpoint()

    answer = a * b

    return answer


print(multiply(6, 8))


# ------------------------

person = {
    "name": "John",
    "age": 25
}

breakpoint()

print(person)