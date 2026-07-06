# Chapter 4: Introduction to Data Structure Iteration

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand why different data structures require different iteration styles.
- Identify when to iterate over values, indexes, keys, or key/value pairs.
- Explain the difference between ordered and unordered collections.
- Avoid common mistakes while modifying collections during iteration.
- Choose readable iteration patterns for lists, dictionaries, and sets.
- Build reusable helper functions that are easy to test.

---

# Introduction

Most useful programs work with collections of data.

Examples:

- A shopping cart contains many products.
- A bank account history contains many transactions.
- A student database contains many student records.
- A web application receives many form fields.
- A search engine processes many results.

To work with these collections, a program must visit each item one by one.

This process is called **iteration**.

---

# What is Data Structure Iteration?

Data structure iteration means traversing a collection and performing an action
for each element.

Example

```python
names = ["Asha", "Ravi", "Mira"]

for name in names:
    print(name)
```

Output

```text
Asha
Ravi
Mira
```

Python hides many internal details, but the idea is simple:

```text
Collection
    |
    v
Get first item
    |
    v
Run loop body
    |
    v
Get next item
    |
    v
Repeat until finished
```

---

# Why Data Shape Matters

Not every collection behaves the same way.

| Data Structure | Ordered | Allows Duplicates | Best Used For |
|---|---:|---:|---|
| List | Yes | Yes | Sequences of values |
| Dictionary | Yes | Keys are unique | Key/value lookups |
| Set | No meaningful order | No | Uniqueness and membership |

The correct iteration style depends on the data structure.

---

# Iterating Over Lists

Lists are ordered collections.

Use a simple `for` loop when only the value matters.

```python
prices = [100, 250, 80]

for price in prices:
    print(price)
```

Use `enumerate` when both index and value matter.

```python
for index, price in enumerate(prices):
    print(index, price)
```

Output

```text
0 100
1 250
2 80
```

---

# Iterating Over Dictionaries

Dictionaries contain key/value pairs.

```python
student = {
    "name": "Asha",
    "marks": 92,
    "city": "Pune",
}
```

Iterate over keys:

```python
for key in student:
    print(key)
```

Iterate over values:

```python
for value in student.values():
    print(value)
```

Iterate over key/value pairs:

```python
for key, value in student.items():
    print(key, value)
```

Use `.items()` when both sides are needed. It avoids repeated dictionary lookup.

---

# Iterating Over Sets

Sets store unique values.

```python
skills = {"python", "sql", "git"}

for skill in skills:
    print(skill)
```

Sets do not provide meaningful business order.

This means the output order should not be used for user-facing display or strict
list comparison.

When order matters:

```python
for skill in sorted(skills):
    print(skill)
```

---

# Real-World Example: E-Commerce Cart

```python
cart = [
    {"name": "Keyboard", "price": 1200},
    {"name": "Mouse", "price": 700},
    {"name": "Monitor", "price": 9000},
]

total = 0

for item in cart:
    total += item["price"]

print(total)
```

Output

```text
10900
```

Here the program iterates over a list of dictionaries.

This is common in real applications because data structures are often nested.

---

# Common Mistake: Modifying While Iterating

This looks reasonable but can behave incorrectly:

```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number % 2 == 0:
        numbers.remove(number)
```

The list changes while Python is still moving through it.

Safer approach:

```python
numbers = [1, 2, 3, 4, 5]
odd_numbers = []

for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)
```

Or with a comprehension:

```python
odd_numbers = [number for number in numbers if number % 2 != 0]
```

---

# Best Practices

- Use direct iteration when indexes are not needed.
- Use `enumerate` instead of manually tracking indexes.
- Use `.items()` when iterating over dictionary keys and values together.
- Do not rely on set iteration order.
- Avoid modifying a list or dictionary while iterating over it.
- Keep loop bodies short and readable.
- Move reusable logic into functions and test those functions.

---

# Practice Questions

1. Print every item in a list of cities.
2. Print each city with its index.
3. Print all key/value pairs in a student dictionary.
4. Count how many times each word appears in a list.
5. Remove duplicate values from a list while preserving order.
6. Print set values in sorted order.

---

# Summary

Data structure iteration is the foundation of real-world Python programming.

Lists, dictionaries, and sets all support iteration, but they represent data in
different ways. Good Python code chooses the iteration style that matches the
shape of the data.
