# If, Elif and Else

## Learning Objectives

After completing this chapter, you will be able to:

- Understand decision making in Python.
- Use `if`, `elif`, and `else` effectively.
- Write nested conditional statements.
- Apply conditional logic in real-world applications.
- Avoid common mistakes while writing conditions.

---

# Introduction

In real-world applications, decisions are made continuously.

Examples:

- Can a user log in?
- Is the customer eligible for a loan?
- Is a student passed or failed?
- Is a product in stock?

Python uses the `if`, `elif`, and `else` statements to make such decisions.

---

# What is an if Statement?

The `if` statement executes a block of code only when a condition evaluates to **True**.

Syntax

```python
if condition:
    statements
```

Example

```python
age = 20

if age >= 18:
    print("Eligible to vote")
```

Output

```
Eligible to vote
```

---

# Flow Diagram

```
        Condition
            │
      ┌─────┴─────┐
      │           │
    True       False
      │           │
 Execute       Skip
      │
 Continue
```

---

# Comparison Operators

| Operator | Meaning |
|----------|----------|
| == | Equal |
| != | Not Equal |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal |
| <= | Less Than or Equal |

Example

```python
x = 15

if x > 10:
    print("Greater than 10")
```

---

# if...else

The `else` block executes when the condition is False.

Syntax

```python
if condition:
    statements
else:
    statements
```

Example

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Output

```
Minor
```

---

# if...elif...else

When multiple conditions need to be checked, use `elif`.

Syntax

```python
if condition1:
    ...

elif condition2:
    ...

elif condition3:
    ...

else:
    ...
```

Example

```python
marks = 82

if marks >= 90:
    grade = "A"

elif marks >= 75:
    grade = "B"

elif marks >= 60:
    grade = "C"

else:
    grade = "Fail"

print(grade)
```

Output

```
B
```

---

# Order of Evaluation

Python evaluates conditions from top to bottom.

Once a condition becomes True, the remaining conditions are skipped.

Example

```python
number = 20

if number > 0:
    print("Positive")

elif number > 10:
    print("Greater than 10")
```

Output

```
Positive
```

The second condition is never checked.

---

# Nested if Statements

An `if` statement can be placed inside another `if`.

Example

```python
age = 25
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to Vote")
```

Output

```
Eligible to Vote
```

---

# Real World Example

### ATM Withdrawal

```python
balance = 10000
amount = 2500

if amount <= balance:
    print("Transaction Successful")
else:
    print("Insufficient Balance")
```

---

### Login System

```python
username = "admin"
password = "python"

if username == "admin":
    if password == "python":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Invalid Username")
```

---

### Student Grade

```python
marks = 91

if marks >= 90:
    print("Grade A")

elif marks >= 80:
    print("Grade B")

elif marks >= 70:
    print("Grade C")

elif marks >= 60:
    print("Grade D")

else:
    print("Fail")
```

---

# Best Practices

✅ Keep conditions simple.

```python
if age >= 18:
```

Instead of

```python
if age >= 18 == True:
```

---

Use meaningful variable names.

Good

```python
is_logged_in = True
```

Bad

```python
x = True
```

---

Avoid deep nesting.

Instead of

```python
if user:

    if user.active:

        if user.admin:

            print("Access")
```

Prefer

```python
if not user:
    return

if not user.active:
    return

if not user.admin:
    return

print("Access")
```

---

# Common Mistakes

### Using = instead of ==

Wrong

```python
if age = 18:
```

Correct

```python
if age == 18:
```

---

### Forgetting Colon

Wrong

```python
if age > 18
```

Correct

```python
if age > 18:
```

---

### Incorrect Indentation

Wrong

```python
if age > 18:
print("Adult")
```

Correct

```python
if age > 18:
    print("Adult")
```

---

# Interview Questions

1. Difference between `if` and `elif`.
2. Can an `if` statement exist without `else`?
3. Can there be multiple `elif` blocks?
4. Can `else` exist without `if`?
5. What is nested `if`?
6. In what order are conditions evaluated?
7. What happens when all conditions are False?

---

# Practice Exercises

1. Check whether a number is positive or negative.
2. Check whether a student passed or failed.
3. Build a simple login system.
4. Find the largest of three numbers.
5. Determine leap year.
6. Create a simple calculator using `if-elif`.

---

# Summary

- `if` executes code when a condition is True.
- `else` executes when the condition is False.
- `elif` checks additional conditions.
- Conditions are evaluated from top to bottom.
- Only the first matching condition executes.
- Proper indentation is mandatory in Python.