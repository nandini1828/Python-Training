# any() and all()

---

## 📌 Overview

- `any()` → returns True if at least one element is True
- `all()` → returns True only if all elements are True

---

## 📌 Syntax

```python
any(iterable)
all(iterable)
```

---

## 📌 any() Example

```python
values = [False, False, True]

print(any(values))
```

### Output
```
True
```

👉 Because at least one value is True

---

## 📌 all() Example

```python
values = [True, True, False]

print(all(values))
```

### Output
```
False
```

👉 Because one value is False

---

## 📌 Working with Numbers

```python
nums = [0, 0, 5]

print(any(nums))   # True (5 is True)
print(all(nums))   # False (0 is False)
```

---

## 📌 Truthy & Falsy Concept

| Value      | Boolean |
|-----------|--------|
| 0         | False  |
| ""        | False  |
| []        | False  |
| None      | False  |
| others    | True   |

---

## 📌 Using with Conditions

```python
nums = [1, 2, 3, 4]

result = any(n > 3 for n in nums)
print(result)
```

### Output
```
True
```

---

## 📌 all() with Condition

```python
nums = [2, 4, 6]

result = all(n % 2 == 0 for n in nums)
print(result)
```

### Output
```
True
```

---

## 📌 Real-world Usage

### Check if any error exists

```python
errors = [0, 0, 1]

if any(errors):
    print("Error found")
```

---

### Check if all tasks completed

```python
tasks = [True, True, True]

if all(tasks):
    print("All tasks done")
```

---

## 📌 Difference

| Feature | any() | all() |
|--------|------|------|
| Condition | at least one True | all must be True |
| Empty iterable | False | True |

---

## 📌 Important Points

- Works with any iterable
- Short-circuits (stops early)
- Very useful with generators

---

## 📌 Common Mistake

```python
values = []

print(any(values))  # False
print(all(values))  # True
```

👉 Empty case behavior is tricky

---

## 📌 Summary

- any() → at least one True
- all() → all True
- useful in validations
- commonly used in real-world checks