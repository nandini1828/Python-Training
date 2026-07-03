# 03_iteration_helpers

## What this project is about
This project shows useful Python tools for working with lists and other repeated data. These tools make your code shorter and easier to read.

## Why this topic matters
When you handle many values, you often need to:
- go through them one by one
- know their position
- sort them
- check if some or all values match a rule

## Topic notes

### 1. range()
`range()` creates a sequence of numbers.

```python
for number in range(5):
    print(number)
```

You can think of it as a simple list of numbers.

### 2. enumerate()
`enumerate()` gives both the index and the value while looping.

```python
students = ["Asha", "Ravi"]
for index, name in enumerate(students, start=1):
    print(index, name)
```

This is useful when you need the position of each item.

### 3. zip()
`zip()` joins items from two or more lists.

```python
names = ["Asha", "Ravi"]
marks = [88, 72]
paired = list(zip(names, marks))
```

It helps combine related information.

### 4. reversed()
`reversed()` gives items from the end to the beginning.

```python
for item in reversed([1, 2, 3]):
    print(item)
```

### 5. sorted()
`sorted()` creates a new sorted list.

```python
numbers = [5, 2, 8]
print(sorted(numbers))
```

### 6. any() and all()
These check whether something is true for at least one item or for every item.

```python
marks = [80, 70, 90]
print(any(mark < 50 for mark in marks))
print(all(mark >= 50 for mark in marks))
```

- `any()` checks if at least one condition is true
- `all()` checks if every condition is true

## What this project demonstrates
- How to loop over data more clearly
- How to pair related values together
- How to sort and reverse data
- How to summarize results with `any()` and `all()`

## How to run
From this folder, run:

```bash
python3 main.py
```

## Learning goals
- Learn helpful built-in tools for iteration
- Practice working with student records
- Understand how small helpers can simplify code
