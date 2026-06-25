# List Methods

## What this folder contains
This folder focuses on Python lists, which are one of the most common data structures in programming. The utilities here show how to work with lists in a simple and reusable way.

## What the code demonstrates
The list utilities include operations such as:
- adding items to a list
- inserting items at a chosen position
- removing items
- reversing and sorting the list
- counting duplicates
- splitting a list into smaller chunks
- calculating an average value

## Why this is important
Lists are used in real Python programs for storing collections of values, processing user input, handling data from files, and organizing tasks in order.

## Example
```python
from list_methods.list_utils import add_destination, chunk_list

cities = ["Paris", "London"]
add_destination(cities, "Rome")
chunks = chunk_list([1, 2, 3, 4], 2)
```

## What a viewer should understand after reading this folder
A viewer should understand that lists are ordered collections and that Python provides many built-in methods to modify and analyze them.
