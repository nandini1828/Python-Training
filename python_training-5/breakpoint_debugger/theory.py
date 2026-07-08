"""
Breakpoint Debugging
--------------------

A breakpoint pauses the execution of a program.

While paused you can:

1. Inspect variables
2. Execute code
3. Step through lines
4. Change variable values
5. Understand program flow

Python provides:

breakpoint()

which launches the debugger.
"""


def calculate_total(price, quantity):
    total = price * quantity

    breakpoint()      # Program pauses here

    discount = total * 0.10

    return total - discount


result = calculate_total(100, 5)

print(result)