# sorted()

---

## 📌 Overview

`sorted()` returns a new sorted list from any iterable.

It does NOT modify the original data.

---

## 📌 Syntax

```python
sorted(iterable, key=None, reverse=False)
```

---

## 📌 Basic Example

```python
nums = [3, 1, 2]

result = sorted(nums)
print(result)
```

### Output
```
[1, 2, 3]
```

---

## 📌 Original List is NOT Modified

```python
nums = [3, 1, 2]

sorted(nums)

print(nums)
```

### Output
```
[3, 1, 2]
```

---

## 📌 Reverse Sorting

```python
nums = [3, 1, 2]

result = sorted(nums, reverse=True)
print(result)
```

### Output
```
[3, 2, 1]
```

---

## 📌 Sorting Strings

```python
words = ["banana", "apple", "cherry"]

print(sorted(words))
```

### Output
```
['apple', 'banana', 'cherry']
```

---

## 📌 Sorting using key

### Example: sort by length

```python
words = ["apple", "kiwi", "banana"]

result = sorted(words, key=len)
print(result)
```

### Output
```
['kiwi', 'apple', 'banana']
```

---

## 📌 Sorting Dictionary Data

```python
data = [
    {"name": "A", "age": 25},
    {"name": "B", "age": 20}
]

result = sorted(data, key=lambda x: x["age"])

print(result)
```

---

## 📌 sorted() vs list.sort()

| Feature        | sorted()        | list.sort() |
|---------------|----------------|------------|
| Returns value | Yes            | No         |
| Modifies list | No             | Yes        |
| Works on any iterable | Yes    | No         |

---

## 📌 Important Points

- Works with list, tuple, string, dict keys
- Returns new list
- Supports custom sorting using key
- Stable sort (maintains order of equal elements)

---

## 📌 Common Mistake

```python
nums = [3, 1, 2]

sorted(nums)
print(nums)
```

👉 nums remains unchanged

---

## 📌 Real-world Usage

```python
students = [
    ("A", 90),
    ("B", 80),
    ("C", 85)
]

result = sorted(students, key=lambda x: x[1])

print(result)
```

---

## 📌 Summary

- returns new sorted list
- does not modify original
- supports key and reverse
- very commonly used