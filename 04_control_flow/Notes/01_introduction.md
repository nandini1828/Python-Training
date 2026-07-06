# Control Flow in Python

---

# Learning Objectives

After completing this module, you will be able to:

- Understand how Python executes code.
- Make decisions using conditional statements.
- Work with Truthy and Falsy values.
- Combine multiple conditions using logical operators.
- Understand Python's short-circuit evaluation.
- Write concise conditional expressions using the ternary operator.
- Use Python 3.10+ structural pattern matching (`match-case`).
- Write clean, readable, and maintainable decision-making code.

---

# What is Control Flow?

Control Flow refers to the order in which Python executes statements in a program.

By default, Python executes code from top to bottom.

Example:

```python
print("Start")
print("Learning Python")
print("End")
```

Output

```
Start
Learning Python
End
```

Execution Flow

```
Start
   │
   ▼
Statement 1
   │
   ▼
Statement 2
   │
   ▼
Statement 3
   │
   ▼
Program Ends
```

---

# Why Do We Need Control Flow?

Imagine building an ATM.

Should money always be withdrawn?

No.

Python must first check

- Is the PIN correct?
- Is the account active?
- Is there sufficient balance?

Only then should money be withdrawn.

Without conditions, every statement would execute regardless of correctness.

---

# Types of Control Flow

Python provides three major ways to control execution.

## 1. Sequential Execution

Code executes line by line.

```
Statement A
↓

Statement B
↓

Statement C
```

---

## 2. Selection

Choose one path among many.

```
            Condition
           /         \
        True         False
         |              |
         ▼              ▼
      Block A       Block B
```

Python uses

- if
- elif
- else
- match-case

---

## 3. Iteration

Repeat code multiple times.

Python provides

- for
- while

These will be covered in the next module.

---

# Real World Examples

Control Flow is used everywhere.

## Banking

```
If PIN is correct

↓

Check Balance

↓

Withdraw Money
```

---

## E-commerce

```
If Premium Customer

↓

Apply Discount

↓

Generate Invoice
```

---

## Authentication

```
Login Request

↓

Validate User

↓

Check Password

↓

Grant Access
```

---

## API

```
Receive Request

↓

Validate Data

↓

Process Request

↓

Return Response
```

---

# Summary

Control Flow determines how a program makes decisions and changes execution based on conditions.

Without Control Flow, programs would execute every statement sequentially, making software incapable of handling real-world scenarios.