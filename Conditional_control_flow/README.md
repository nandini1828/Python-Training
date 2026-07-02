# 01_conditional_control_flow

## What this project is about
This project teaches you how Python makes decisions. A program often needs to ask, “What should I do next?” and conditions help answer that question.

## Why this topic matters
Every real program uses decisions. For example:
- Should a student pass or fail?
- Should a user see one menu or another?
- Should a result be marked as eligible or not eligible?

## Topic notes

### 1. if, elif, else
These are the main decision tools in Python.

```python
marks = 75
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
else:
    grade = "C"
```

Think of it like this: Python checks the first condition. If it is true, it uses that path. If not, it moves to the next one.

### 2. Truthy and falsy values
Python treats some values as true and others as false.

```python
name = "Asha"
if name:
    print("Name exists")
```

In this example, a non-empty string is considered truthy.

### 3. and, or, not
These operators help combine conditions.

```python
age = 20
passed = True
if passed and age >= 18:
    print("Eligible")
```

- `and` means both conditions must be true
- `or` means at least one condition must be true
- `not` reverses the result

### 4. Short-circuit evaluation
Python does not always check every part of a condition if it already knows the result.

```python
is_student = False
if is_student and marks > 90:
    print("Excellent")
```

Because `is_student` is false, Python does not need to check the second part.

### 5. Ternary operator
This is a short way to write a simple `if-else` statement.

```python
result = "PASS" if marks >= 40 else "FAIL"
```

It is useful when the decision is very small.

### 6. match-case
`match` and `case` are used when a value should be checked against several possible options.

```python
choice = "2"
match choice:
    case "1":
        print("Option 1")
    case "2":
        print("Option 2")
    case _:
        print("Invalid")
```

This is very helpful for simple menus.

## What this project demonstrates
- How Python makes choices
- How logical conditions work
- How to write clear decision logic
- How to use pattern matching for menus

## How to run
From this folder, run:

```bash
python3 main.py
```

## Learning goals
- Understand how decisions are made in a program
- Practice using conditions in a simple project
- Learn when to use `if`, `match`, and logical operators
