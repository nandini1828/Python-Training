# Composition

## What this folder contains
This folder demonstrates composition, a design idea where a class uses other objects to perform its work instead of doing everything alone.

## What the code demonstrates
The composition example shows how smaller objects can be combined to form larger systems such as:
- employees inside departments
- departments inside a company
- related objects working together in one model

## Why this is important
Composition helps make code more modular, easier to maintain, and easier to expand later. It is a common pattern in professional Python projects.

## Example
```python
from composition.composition_utils import Employee, Department, Company

engineer = Employee("Ada", "Engineer")
department = Department("Engineering", [engineer])
company = Company("Acme", [department])
```

## What a viewer should understand after reading this folder
A viewer should understand that composition is a cleaner way to build programs by combining smaller, focused objects.
