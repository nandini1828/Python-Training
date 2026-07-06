# 📌 Introduction to Iteration Helpers

---

## 🧠 What are Iteration Helpers?

Iteration helpers are **built-in Python tools** that make looping:

- cleaner
- shorter
- more readable
- more efficient

Instead of writing complex loops manually, Python provides helpers like:

- `range()`
- `enumerate()`
- `zip()`
- `reversed()`
- `sorted()`
- `any()` / `all()`

---

## 🔥 Why do we need them?

Without helpers, loops become:

❌ long  
❌ error-prone  
❌ harder to read  

Example without helper:

```python
i = 0
data = ["a", "b", "c"]

while i < len(data):
    print(i, data[i])
    i += 1



    # Iteration Helpers in Python

---

## 1. range()

### Overview
Generates a sequence of numbers.

### Syntax
```python
range(stop)
range(start, stop)
range(start, stop, step)
```

### Examples
```python
for i in range(5):
    print(i)
```

```python
for i in range(2, 6):
    print(i)
```

```python
for i in range(0, 10, 2):
    print(i)
```

### Key Points
- stop is exclusive
- supports negative step
- memory efficient

```python
range(5, 0, -1)
```

---

## 2. enumerate()

### Overview
Returns index and value.

### Syntax
```python
enumerate(iterable, start=0)
```

### Example
```python
data = ["a", "b", "c"]

for i, val in enumerate(data):
    print(i, val)
```

### Custom Start
```python
for i, val in enumerate(data, start=1):
    print(i, val)
```

### Key Points
- better than range(len())
- improves readability

---

## 3. zip()

### Overview
Combines multiple iterables.

### Syntax
```python
zip(iter1, iter2, ...)
```

### Example
```python
names = ["A", "B"]
scores = [10, 20]

for n, s in zip(names, scores):
    print(n, s)
```

### Stops at shortest
```python
zip([1,2,3], [4])
```

### Create dictionary
```python
keys = ["name", "age"]
values = ["Ganesh", 22]

dict(zip(keys, values))
```

### Unzip
```python
pairs = [("a",1), ("b",2)]
a, b = zip(*pairs)
```

### Key Points
- returns iterator
- stops at shortest

---

## 4. reversed()

### Overview
Returns reversed iterator.

### Syntax
```python
reversed(iterable)
```

### Example
```python
for i in reversed([1,2,3]):
    print(i)
```

### Difference
```python
data[::-1]   # new list
reversed()   # iterator
```

---

## 5. sorted()

### Overview
Returns sorted list.

### Syntax
```python
sorted(iterable, key=None, reverse=False)
```

### Example
```python
sorted([3,1,2])
```

### Reverse
```python
sorted([3,1,2], reverse=True)
```

### Key
```python
words = ["apple", "banana", "kiwi"]
sorted(words, key=len)
```

---

## 6. any()

### Overview
True if any element is True.

### Example
```python
any([False, False, True])
```

### Use
```python
nums = [0, 0, 5]

if any(nums):
    print("At least one non-zero")
```

---

## 7. all()

### Overview
True if all elements are True.

### Example
```python
all([True, True, False])
```

### Use
```python
nums = [1, 2, 3]

if all(nums):
    print("All are non-zero")
```

---

## Summary

| Function    | Purpose            |
|------------|--------------------|
| range()     | numbers            |
| enumerate() | index + value      |
| zip()       | combine iterables  |
| reversed()  | reverse iteration  |
| sorted()    | sorting            |
| any()       | any True           |
| all()       | all True           |

---

## Final Notes

- Cleaner code
- Less errors
- Widely used