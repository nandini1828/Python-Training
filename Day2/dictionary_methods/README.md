# Dictionary Methods

## What this folder contains
This folder explains dictionaries, which store data as key-value pairs. Dictionaries are one of the most important data structures in Python because they allow fast lookup by name or key.

## What the code demonstrates
The dictionary utilities show how to:
- add new key-value pairs
- retrieve values safely
- remove keys
- update existing data
- list all keys, values, or items
- merge dictionaries
- filter values by a condition

## Why this is important
Dictionaries are used in Python for configuration files, API responses, user data, and many other real-world tasks.

## Example
```python
from dictionary_methods.dictionary_utils import add_item, get_value

student = {"name": "Ada"}
add_item(student, "age", 21)
age = get_value(student, "age")
```

## What a viewer should understand after reading this folder
A viewer should understand that dictionaries are perfect for storing related pieces of data using meaningful names.
