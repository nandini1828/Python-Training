# Set Methods

## What this folder contains
This folder explains sets, which are used when you want to store unique values and perform mathematical set operations.

## What the code demonstrates
The set utilities show how to:
- add or remove items
- create a set from a list
- find common values between sets
- combine sets using union
- find differences between sets
- check whether one set is a subset or superset of another

## Why this is important
Sets are useful when you want to remove duplicates, compare groups of items, and work with membership logic efficiently.

## Example
```python
from set_methods.set_utils import unique_items, common_elements

values = unique_items([1, 1, 2, 3])
shared = common_elements({1, 2, 3}, {2, 3, 4})
```

## What a viewer should understand after reading this folder
A viewer should understand that sets are best used for uniqueness and fast comparison of groups of values.
