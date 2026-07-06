# Ternary Operator in Python

## Learning Objectives

After completing this chapter, you will be able to:

- Understand the Ternary Operator.
- Write concise conditional expressions.
- Compare Ternary Operator with traditional `if-else`.
- Apply the Ternary Operator in real-world scenarios.
- Follow best practices for readability.

---

# Introduction

The **Ternary Operator** allows you to write a simple `if-else` statement in a single line.

It is useful when assigning a value based on a condition.

Instead of writing multiple lines, the same logic can often be expressed more concisely.

---

# Syntax

```python
value_if_true if condition else value_if_false
```

---

# Basic Example

Traditional `if-else`

```python
age = 20

if age >= 18:
    status = "Adult"
else:
    status = "Minor"

print(status)
```

Using Ternary Operator

```python
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)
```

Output

```
Adult
```

---

# Flow Diagram

```
          Condition
              │
      ┌───────┴────────┐
      │                │
    True             False
      │                │
Value if True    Value if False
      │
   Assignment
```

---

# Multiple Examples

### Check Even or Odd

```python
number = 8

result = "Even" if number % 2 == 0 else "Odd"

print(result)
```

---

### Maximum of Two Numbers

```python
a = 15
b = 30

maximum = a if a > b else b

print(maximum)
```

---

### Login Status

```python
is_logged_in = True

message = "Welcome" if is_logged_in else "Please Login"

print(message)
```

---

### Pass or Fail

```python
marks = 65

result = "Pass" if marks >= 40 else "Fail"

print(result)
```

---

# Nested Ternary Operator

Nested ternary operators are possible but should be used carefully.

Example

```python
marks = 82

grade = (
    "A" if marks >= 90 else
    "B" if marks >= 75 else
    "C" if marks >= 60 else
    "Fail"
)

print(grade)
```

Output

```
B
```

---

# Real-World Examples

### Discount

```python
is_member = True

discount = 20 if is_member else 5

print(discount)
```

---

### Shipping

```python
amount = 1200

shipping = "Free" if amount >= 1000 else "Paid"

print(shipping)
```

---

### Employee Bonus

```python
rating = 5

bonus = 10000 if rating >= 5 else 3000

print(bonus)
```

---

# Best Practices

✅ Use the Ternary Operator only for simple conditions.

Good

```python
status = "Adult" if age >= 18 else "Minor"
```

Avoid writing long nested ternary expressions that reduce readability.

---

# Common Mistakes

### Incorrect Syntax

Wrong

```python
status = if age >= 18 "Adult" else "Minor"
```

Correct

```python
status = "Adult" if age >= 18 else "Minor"
```

---

### Overusing Nested Ternary Operators

If the logic becomes difficult to understand, use a normal `if-elif-else` statement instead.

---

# When to Use

Use the Ternary Operator when:

- Assigning values.
- Returning values.
- Writing short conditional expressions.

Avoid using it for large blocks of code.

---

# Interview Questions

1. What is the Ternary Operator?
2. What is its syntax?
3. When should you use it?
4. Can it replace every `if-else` statement?
5. What are the disadvantages of nested ternary operators?

---

# Practice Exercises

1. Find the larger of two numbers.
2. Check whether a number is even or odd.
3. Determine pass or fail.
4. Assign grades using nested ternary operators.
5. Display login status using the Ternary Operator.

---

# Summary

- The Ternary Operator provides a concise way to write simple conditional expressions.
- It is best suited for value assignment.
- Avoid excessive nesting.
- Prefer normal `if-else` statements for complex logic.