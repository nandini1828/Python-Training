# Continue Statement in Python

## Overview

The `continue` statement is used in loops to skip the current iteration and move to the next iteration of the loop.

Unlike `break`, which terminates the loop entirely, `continue` only skips the remaining code in the current iteration.

---

## Syntax

```python
for item in iterable:
    if condition:
        continue
    # remaining code
```

---

## Key Characteristics

* Skips current iteration only
* Does not terminate loop
* Works in both `for` and `while` loops
* Helps in filtering unwanted data

---

## Flow Explanation

1. Loop starts
2. Condition checked
3. If `continue` is encountered:

   * Skip remaining code in current iteration
   * Move to next iteration

---

## Examples

### Skip Even Numbers

```python
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i)
```

Output:

```
1 3 5
```

---

### Skip Invalid Inputs

```python
values = [10, -5, 20, -1]

for val in values:
    if val < 0:
        continue
    print(val)
```

Output:

```
10 20
```

---

## Difference Between break and continue

| Feature         | break           | continue           |
| --------------- | --------------- | ------------------ |
| Stops loop      | Yes             | No                 |
| Skips iteration | No              | Yes                |
| Use case        | Exit loop early | Skip unwanted data |

---

## When to Use

* Skipping invalid inputs
* Filtering datasets
* Ignoring unwanted cases
* Data cleaning operations
