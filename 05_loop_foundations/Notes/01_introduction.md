# Loop Foundations in Python

---

# Learning Objectives

After completing this module, you will understand:

- Why loops are required
- The difference between `for` and `while`
- When to use each loop
- How Python iterates over collections
- Loop control statements
- Enterprise use cases
- Best practices

---

# What is a Loop?

A loop allows a block of code to execute repeatedly.

Instead of writing

```python
print("Python")
print("Python")
print("Python")
print("Python")
print("Python")
```

we can write

```python
for _ in range(5):
    print("Python")
```

Output

```
Python
Python
Python
Python
Python
```

---

# Why Do We Need Loops?

Imagine processing

- 10 students
- 100 products
- 10,000 database records

Writing individual statements is impossible.

Loops allow Python to repeat work automatically.

---

# Types of Loops

Python provides two looping statements.

## for

Used when the number of iterations is known.

Example

```python
for number in range(5):
    print(number)
```

---

## while

Used when the stopping condition is unknown.

Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

# Loop Execution Flow

```
Start

↓

Condition

↓

True

↓

Execute Body

↓

Update

↓

Condition

↓

False

↓

Exit
```

---

# Common Uses

Loops are used for

- Reading files
- Processing APIs
- Database records
- Machine Learning datasets
- CSV files
- Automation
- Data validation

---

# Enterprise Examples

## Banking

```
Process every transaction
```

---

## E-Commerce

```
Generate invoices

for every order
```

---

## Authentication

```
Check login attempts
```

---

## Reporting

```
Generate reports

for every employee
```

---

# Summary

Loops reduce duplication and automate repetitive tasks.

Python mainly provides

- for
- while

along with loop control statements such as

- break
- continue
- pass