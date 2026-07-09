# range()

---

# Learning Objectives

After completing this chapter, you will understand:

- What range() is
- Different forms of range()
- Positive and negative steps
- Common use cases
- Best practices

---

# What is range()?

`range()` generates a sequence of integers.

It is commonly used with `for` loops.

---

# Syntax

```python
range(stop)
```

```python
range(start, stop)
```

```python
range(start, stop, step)
```

---

# Example

```python
for number in range(5):
    print(number)
```

Output

```
0
1
2
3
4
```

---

# Start and Stop

```python
for number in range(5, 10):
    print(number)
```

Output

```
5
6
7
8
9
```

---

# Using Step

```python
for number in range(0, 20, 2):
    print(number)
```

Output

```
0
2
4
6
...
18
```

---

# Reverse Counting

```python
for number in range(10, 0, -1):
    print(number)
```

Output

```
10
9
8
...
1
```

---

# Practical Uses

- Generate IDs
- Pagination
- Batch processing
- Countdown timers
- Multiplication tables

---

# Common Mistakes

Incorrect

```python
range(1, 10, 0)
```

Raises

```
ValueError
```

---

# Best Practices

✔ Use meaningful variable names.

✔ Prefer range() over manually incrementing counters.

✔ Use negative steps for reverse iteration.

---

# Summary

`range()` is an efficient way to generate integer sequences without storing all values in memory.