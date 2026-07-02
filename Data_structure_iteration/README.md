# 04_data_structure_iteration

## What this project is about
This project is a small contact book. It shows how Python stores information in different data structures and how to work with that information.

## Why this topic matters
In programming, data is often stored in groups. You may need to:
- keep a list of names
- store details in a dictionary
- keep only unique values in a set

## Topic notes

### 1. Lists
A list stores values in order.

```python
contacts = ["Asha", "Ravi"]
```

Use a list when the order matters.

### 2. Dictionaries
A dictionary stores values as key-value pairs.

```python
person = {"name": "Asha", "city": "Delhi"}
```

This is useful when each item has a label.

### 3. Sets
A set stores unique values only.

```python
cities = {"Delhi", "Mumbai", "Delhi"}
```

If the same value appears again, it is kept only once.

### 4. Dictionary .get()
`.get()` helps you access a value safely.

```python
print(person.get("phone", "Not available"))
```

If the key does not exist, it gives a default value instead of failing.

### 5. Safe list modification while iterating
If you remove items while looping over a list, it can cause problems. A safe way is to loop over a copy.

```python
for item in list(contacts):
    if item == "Asha":
        contacts.remove(item)
```

## What this project demonstrates
- How lists, dictionaries, and sets are used
- How to search and update stored values
- How to remove items safely from a list

## How to run
From this folder, run:

```bash
python3 main.py
```

## Learning goals
- Understand the main built-in data structures
- Practice storing and reading data in a simple way
- Learn safe ways to modify lists while looping
