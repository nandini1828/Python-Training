# Match Case (Structural Pattern Matching)

## Overview

`match-case` is a modern control flow feature introduced in **Python 3.10** that provides **Structural Pattern Matching**.

It allows programs to compare an object against one or more patterns and execute the matching block of code.

Unlike traditional `if-elif-else`, `match-case` is more expressive, readable, and scalable when handling multiple conditions or complex data structures.

It is conceptually similar to the **switch-case** statement found in languages such as Java, C#, Go, and JavaScript, but is significantly more powerful because it supports pattern matching rather than simple equality checks.

---

# Learning Objectives

After completing this module, you will be able to:

- Understand Structural Pattern Matching.
- Write cleaner alternatives to long if-elif chains.
- Match literals and constants.
- Match multiple values.
- Use wildcard patterns.
- Capture variables.
- Match sequences.
- Match dictionaries.
- Match objects.
- Apply guards using `if`.
- Build enterprise-level decision systems using `match-case`.

---

# Prerequisites

- Python 3.10 or later
- Variables
- Functions
- if-elif-else
- Tuples
- Lists
- Dictionaries
- Classes

---

# Folder Structure

```text
match_case/
│
├── README.md
├── __init__.py
├── demo.py
└── utils.py
```

---

# Syntax

```python
match expression:

    case pattern_1:
        ...

    case pattern_2:
        ...

    case _:
        ...
```

---

# Execution Flow

```text
            Expression
                 │
                 ▼
        Compare with Case 1
          │          │
     Match?        No Match
       │               │
       ▼               ▼
 Execute Block    Compare Case 2
                      │
                      ▼
                  Continue...
                      │
                      ▼
                Wildcard (_)
```

---

# Why Match Case?

Suppose we have:

```python
if day == 1:
    ...
elif day == 2:
    ...
elif day == 3:
    ...
elif day == 4:
    ...
elif day == 5:
    ...
```

This quickly becomes difficult to maintain.

Instead,

```python
match day:

    case 1:
        ...

    case 2:
        ...

    case 3:
        ...

    case 4:
        ...

    case 5:
        ...
```

The code becomes cleaner and easier to extend.

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
        print("Invalid")
```

Output

```
Wednesday
```

---

# Matching Multiple Values

```python
match grade:

    case "A" | "A+":
        print("Excellent")

    case "B" | "B+":
        print("Very Good")

    case _:
        print("Others")
```

---

# Wildcard Pattern

```python
case _:
```

Equivalent to

```
default
```

in other programming languages.

---

# Variable Capture

```python
match value:

    case x:
        print(x)
```

Python stores the matched value inside `x`.

---

# Guard Conditions

Guards allow additional conditions.

```python
match age:

    case age if age >= 18:
        print("Adult")

    case _:
        print("Minor")
```

---

# Matching Lists

```python
numbers = [10,20]

match numbers:

    case [a,b]:
        print(a,b)
```

---

# Matching Tuples

```python
point = (5,7)

match point:

    case (0,0):
        print("Origin")

    case (x,y):
        print(x,y)
```

---

# Matching Dictionaries

```python
employee = {
    "name":"Ganesh",
    "role":"Developer"
}

match employee:

    case {"role":"Developer"}:
        print("Software Developer")
```

---

# Matching Objects

```python
match employee:

    case Employee(name=name):
        print(name)
```

---

# Enterprise Use Cases

Structural Pattern Matching is commonly used in

- API Routers
- Command Line Interfaces
- Protocol Parsers
- Authentication Systems
- Payment Processing
- Message Brokers
- Chatbots
- AI Agent Routing
- Workflow Engines
- Event Processing Systems

---

# Advantages

- Cleaner than long if-elif chains.
- Easier maintenance.
- Better readability.
- Supports nested structures.
- Supports sequences.
- Supports dictionaries.
- Supports objects.
- Supports guards.

---

# Limitations

- Requires Python 3.10+
- Not ideal for very simple two-condition decisions.
- Can become difficult if patterns are overly complex.

---

# Best Practices

✔ Prefer `match-case` when handling many discrete values.

✔ Keep patterns simple.

✔ Always include a wildcard (`case _`).

✔ Use guards only when necessary.

✔ Prefer meaningful variable names.

---

# Common Mistakes

❌ Forgetting the wildcard case.

❌ Using Python versions below 3.10.

❌ Writing extremely deep nested patterns.

❌ Using match-case for simple boolean checks.

---

# Comparison

| if-elif | match-case |
|----------|------------|
| Sequential checks | Pattern matching |
| Less readable | More readable |
| Hard to maintain | Easier to maintain |
| Equality only | Structural matching |
| No sequence matching | Supports sequences |

---

# Interview Questions

1. What is Structural Pattern Matching?
2. When should you use match-case?
3. Difference between switch-case and match-case?
4. What is wildcard pattern?
5. What are guards?
6. Can match-case match lists?
7. Can it match dictionaries?
8. Can it match objects?
9. Which Python version introduced match-case?
10. What are the advantages over if-elif?

---

# Practice Exercises

1. Build a calculator using match-case.
2. Build a command parser.
3. Build a login menu.
4. Build an ATM menu.
5. Build a REST API router.
6. Build a chatbot intent matcher.

---

# Summary

`match-case` is one of the most significant additions to modern Python. It enables expressive, readable, and maintainable decision-making through Structural Pattern Matching. It is especially useful in enterprise applications that involve routing, parsing, state machines, AI workflows, and complex decision trees.