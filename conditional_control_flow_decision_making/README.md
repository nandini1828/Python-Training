# Conditional Control Flow & Decision Making

## Overview

This module introduces the fundamentals of decision-making in Python. Every software application needs to make decisions based on different conditions, such as validating user input, checking permissions, processing payments, or determining business rules. Python provides several control flow statements that allow programs to execute different blocks of code depending on the outcome of conditions.

In this project, a **Food Delivery Order Processing System** was built to demonstrate how conditional statements are used in real-world applications. The system validates user login, checks whether the shopping cart contains items, verifies payment and delivery address information, applies coupons, calculates delivery charges, and displays the current order status.

---

## Concepts Covered

### if - elif - else

The `if`, `elif`, and `else` statements are the foundation of decision-making in Python. They allow programs to evaluate multiple conditions and execute the appropriate block of code.

### Truthy and Falsy Values

Python treats certain values such as `0`, `None`, empty strings, empty lists, empty dictionaries, and empty sets as **False**, while most other objects are considered **True**. Understanding truthy and falsy values allows developers to write cleaner and more Pythonic code.

### Logical Operators

Logical operators (`and`, `or`, and `not`) are used to combine multiple conditions into a single expression, making complex decision-making easier and more readable.

### Short-Circuit Evaluation

Python optimizes logical expressions by stopping evaluation as soon as the final result is known. This behavior helps improve performance and prevents unnecessary errors when accessing objects that may not exist.

### Ternary Operator

The ternary operator provides a concise way to assign values based on a condition using a single line of code, improving readability for simple decisions.

### match-case

Introduced in Python 3.10, `match-case` provides structural pattern matching, making it easier to replace long `if-elif` chains when comparing multiple values.

---

## What This Project Demonstrates

- Building decision trees using conditional statements
- Writing clean and readable business logic
- Combining multiple conditions safely
- Using Pythonic truthy and falsy evaluations
- Applying modern pattern matching with `match-case`

---

## Learning Outcomes

After completing this module, you will be able to design conditional workflows, validate application data, simplify decision-making logic, and write maintainable Python code commonly used in backend development.