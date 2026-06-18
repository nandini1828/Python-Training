
# Employee Management System

## Overview

This project demonstrates core Python concepts including:

* Data Types
* Data Structures
* Object-Oriented Programming (OOP)
* Encapsulation
* Inheritance
* Abstraction
* Polymorphism
* Variable Positional Arguments (`*args`)
* Variable Keyword Arguments (`**kwargs`)
* Common Methods for String, List, Set, and Dictionary

The application models an Employee Management System where employee information, skills, projects, and additional details are maintained using different Python data structures.

---

## Concepts Covered

### Data Types

The program uses the following Python data types:

| Data Type | Example         |
| --------- | --------------- |
| Integer   | Employee ID     |
| String    | Employee Name   |
| Float     | Employee Salary |

Example:

```python
emp_id = 101
name = "Vyshnavi"
salary = 50000.0
```

---

### Data Structures

#### List

Used to store employee skills.

```python
self.skills = []
```

Methods Used:

```python
extend()
```

#### Set

Used to store employee projects.

```python
self.projects = set()
```

Methods Used:

```python
update()
```

Benefits:

* Stores unique values
* Automatically removes duplicates

#### Dictionary

Used to store additional employee details.

```python
self.details = {}
```

Methods Used:

```python
update()
items()
```

---

## Object-Oriented Programming Concepts

### Class

A class acts as a blueprint for creating objects.

```python
class Employee:
```

---

### Object

An object is an instance of a class.

```python
employee = Employee(...)
```

---

### Encapsulation

Sensitive data is protected using private variables.

```python
self.__emp_id
```

The employee ID cannot be directly accessed outside the class.

---

### Inheritance

The Employee class inherits from the Person class.

```python
class Employee(Person):
```

This promotes code reusability.

---

### Abstraction

Abstract classes define a contract that child classes must implement.

```python
class Person(ABC):

    @abstractmethod
    def display_info(self):
        pass
```

---

### Polymorphism

The Employee class provides its own implementation of the abstract method.

```python
def display_info(self):
```

---

## Variable Positional Arguments (*args)

The program uses *args to accept multiple values dynamically.

Example:

```python
employee.add_skills(
    "Python",
    "FastAPI",
    "Git"
)
```

Internally:

```python
skills = (
    "Python",
    "FastAPI",
    "Git"
)
```

---

## Variable Keyword Arguments (**kwargs)

The program uses **kwargs to accept dynamic key-value pairs.

Example:

```python
employee.update_details(
    age=22,
    city="Hyderabad"
)
```

Internally:

```python
{
    "age": 22,
    "city": "Hyderabad"
}
```

---

## Methods Demonstrated

### String Methods

```python
title()
```

Converts:

```python
"vyshnavi"
```

to:

```python
"Vyshnavi"
```

### List Methods

```python
extend()
```

### Set Methods

```python
update()
```

### Dictionary Methods

```python
update()
items()
```

---

## Program Flow

1. Create an Employee object.
2. Add multiple skills using *args.
3. Add multiple projects using *args.
4. Store employee details using **kwargs.
5. Display employee information.
6. Display data types and data structures used.

---

## Sample Output

```text
Employee Information
--------------------
Employee ID : 101
Name        : Vyshnavi
Salary      : 50000.0

Skills:
Python
FastAPI
Git

Projects:
CRM
Insurance Portal

Additional Details:
age : 22
city : Hyderabad
experience : Fresher
```

---

## Learning Outcomes

After completing this project, you will understand:

* Python Data Types
* Python Data Structures
* Classes and Objects
* Encapsulation
* Inheritance
* Abstraction
* Polymorphism
* *args and **kwargs
* Common collection methods
* Real-world OOP implementation in Python

```
```
