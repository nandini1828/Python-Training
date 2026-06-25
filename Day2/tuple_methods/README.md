# Tuple Methods

## What this folder contains
This folder explains tuples, which are similar to lists but cannot be changed once created. Tuples are useful when a program needs a fixed collection of values.

## What the code demonstrates
The tuple utilities show how to:
- access the first and last items
- count how many times a value appears
- find the position of an item
- convert a tuple into a list
- build a dictionary from two tuples

## Why this is important
Tuples are commonly used for fixed data such as coordinates, settings, and return values from functions. They help make code safer by preventing accidental changes.

## Example
```python
from tuple_methods.tuple_utils import access_first_item, tuple_to_dict

numbers = (1, 2, 3)
first = access_first_item(numbers)
mapping = tuple_to_dict(("name", "age"), ("Ada", 21))
```

## What a viewer should understand after reading this folder
A viewer should understand that tuples are immutable and are useful when data should stay constant.
