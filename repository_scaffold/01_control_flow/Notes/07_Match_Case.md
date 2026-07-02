# Match-Case Statement in Python

## Learning Objectives

After completing this chapter, you will be able to:

- Understand the `match-case` statement.
- Learn how structural pattern matching works.
- Replace long `if-elif-else` chains using `match-case`.
- Write cleaner and more readable decision-making code.
- Understand when to use and when to avoid `match-case`.

---

# Introduction

The `match-case` statement was introduced in **Python 3.10**.

It provides a cleaner and more readable way to compare a value against multiple patterns.

It is often considered Python's modern alternative to long `if-elif-else` statements.

---

# Syntax

```python
match expression:
    case pattern1:
        statements

    case pattern2:
        statements

    case _:
        default_statements
```

The underscore (`_`) acts as the default case, similar to `else`.

---

# Basic Example

```python
day = 3

match day:
    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case _:
        print("Invalid Day")
```

Output

```
Wednesday
```

---

# Flow Diagram

```
          Expression
               │
      ┌────────┼────────┐
      │        │        │
   Case 1   Case 2   Case 3
      │        │        │
      └────────┴────────┘
               │
          Default (_)
```

---

# Multiple Patterns

You can match multiple values using the `|` operator.

Example

```python
day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")

    case _:
        print("Weekday")
```

Output

```
Weekend
```

---

# Matching Data Types

```python
value = 10

match value:
    case int():
        print("Integer")

    case str():
        print("String")

    case _:
        print("Unknown")
```

---

# Match with Guards

Guards allow additional conditions.

Example

```python
age = 20

match age:
    case x if x >= 18:
        print("Adult")

    case _:
        print("Minor")
```

---

# Real-World Examples

### Menu Selection

```python
choice = 2

match choice:
    case 1:
        print("Add Student")

    case 2:
        print("Update Student")

    case 3:
        print("Delete Student")

    case _:
        print("Invalid Choice")
```

---

### HTTP Status Codes

```python
status = 404

match status:
    case 200:
        print("Success")

    case 404:
        print("Not Found")

    case 500:
        print("Server Error")

    case _:
        print("Unknown Status")
```

---

### Calculator

```python
operator = "+"

match operator:
    case "+":
        print(10 + 20)

    case "-":
        print(10 - 20)

    case "*":
        print(10 * 20)

    case "/":
        print(10 / 20)

    case _:
        print("Invalid Operator")
```

---

# match-case vs if-elif

| if-elif | match-case |
|----------|------------|
| Best for conditions | Best for matching patterns |
| Can evaluate complex expressions | Matches values and structures |
| Available in all Python versions | Available from Python 3.10+ |
| Can become lengthy | Cleaner for multiple cases |

---

# Best Practices

- Use `match-case` when comparing one value against many possible values.
- Keep each case short and focused.
- Always include a default (`case _:`) block.
- Prefer `if-elif` for complex logical conditions.

---

# Common Mistakes

### Forgetting the Default Case

Wrong

```python
match value:
    case 1:
        print("One")
```

Better

```python
match value:
    case 1:
        print("One")

    case _:
        print("Unknown")
```

---

### Using match-case for Complex Conditions

Avoid replacing every `if-elif` with `match-case`.

Use `match-case` only when pattern matching improves readability.

---

# Interview Questions

1. What is `match-case`?
2. Which Python version introduced `match-case`?
3. What is structural pattern matching?
4. What is the purpose of `case _:`?
5. When should `match-case` be preferred over `if-elif`?
6. Can multiple patterns be matched in a single case?

---

# Practice Exercises

1. Build a menu-driven calculator.
2. Print the day of the week using `match-case`.
3. Handle HTTP status codes.
4. Create a simple ATM menu.
5. Build a traffic signal simulator using `match-case`.

---

# Summary

- `match-case` is a modern pattern matching feature introduced in Python 3.10.
- It improves readability when matching one value against multiple patterns.
- The `_` pattern acts as the default case.
- Use `match-case` for value and pattern matching, and `if-elif` for complex conditional logic.