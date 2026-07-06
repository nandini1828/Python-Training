# reversed()

---

## 📌 Overview

`reversed()` returns an iterator that accesses elements in reverse order.

It does NOT create a new list — it is memory efficient.

---

## 📌 Syntax

```python
reversed(iterable)
```

---

## 📌 Basic Example

```python
data = [1, 2, 3, 4]

for i in reversed(data):
    print(i)
```

### Output
```
4
3
2
1
```

---

## 📌 Using with list()

```python
data = [1, 2, 3]

rev = list(reversed(data))
print(rev)
```

### Output
```
[3, 2, 1]
```

---

## 📌 Using with string

```python
text = "hello"

for ch in reversed(text):
    print(ch)
```

---

## 📌 Difference: reversed() vs slicing

```python
data = [1, 2, 3]

rev1 = data[::-1]        # creates new list
rev2 = reversed(data)    # iterator
```

### Key Difference

| Feature        | slicing (`[::-1]`) | reversed() |
|---------------|------------------|-----------|
| Memory        | creates new list | no new list |
| Type          | list             | iterator |
| Performance   | slower           | faster |

---

## 📌 Important Points

- Works only with sequences (list, tuple, string)
- Returns an iterator
- Cannot be used directly on generators

---

## 📌 Common Mistake

```python
rev = reversed([1,2,3])
print(rev)
```

### Output
```
<list_reverseiterator object>
```

👉 Fix:

```python
print(list(rev))
```

---

## 📌 Real-world Usage

```python
names = ["A", "B", "C"]

for name in reversed(names):
    print(name)
```

---

## 📌 Summary

- reverses sequence
- returns iterator
- memory efficient
- better than slicing for large data