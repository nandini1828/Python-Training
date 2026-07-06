# Structural Pattern Matching (`match-case`)

---

# Learning Objectives

After completing this chapter, you will understand:

- Why `match-case` was introduced
- Difference between `if-elif-else` and `match-case`
- Literal patterns
- OR patterns
- Wildcard patterns
- Variable capture
- Sequence patterns
- Mapping patterns
- Guards
- Class patterns
- Enterprise use cases

---

# Introduction

Python 3.10 introduced **Structural Pattern Matching** through the `match-case` statement.

It allows you to compare the **structure** of data instead of writing long chains of `if-elif-else`.

General Syntax

```python
match expression:
    case pattern1:
        ...
    case pattern2:
        ...
    case _:
        ...
```

---

# Why was match-case introduced?

Consider this code.

```python
status = 404

if status == 200:
    print("OK")
elif status == 404:
    print("Not Found")
elif status == 500:
    print("Internal Server Error")
else:
    print("Unknown")
```

The same logic becomes cleaner.

```python
match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown")
```

---

# Literal Patterns

Literal values match exactly.

```python
match day:
    case "Monday":
        print("Weekday")

    case "Sunday":
        print("Holiday")
```

---

# OR Patterns

Multiple values can match the same block.

```python
match extension:
    case "jpg" | "png" | "jpeg":
        print("Image")
```

Equivalent if statement

```python
if extension in ("jpg", "png", "jpeg"):
    ...
```

---

# Wildcard Pattern

The underscore (`_`) matches everything.

```python
match status:
    case 200:
        ...
    case _:
        print("Unknown")
```

Think of `_` as the default case.

---

# Variable Capture

Variables automatically capture matched values.

```python
match command:

    case ["delete", filename]:
        print(filename)
```

Input

```
["delete", "notes.txt"]
```

Output

```
notes.txt
```

---

# Sequence Patterns

Lists and tuples can be matched.

```python
match values:

    case [x]:
        print("Single Value")

    case [x, y]:
        print("Two Values")

    case [first, *remaining]:
        print(first)
```

---

# Tuple Pattern

```python
point = (10, 20)

match point:

    case (0, 0):
        print("Origin")

    case (x, y):
        print(x, y)
```

---

# Mapping Pattern

Dictionaries can also be matched.

```python
match response:

    case {"status": "success", "data": data}:
        print(data)

    case {"status": "error", "message": msg}:
        print(msg)
```

---

# Guards

Guards are additional conditions.

```python
match number:

    case n if n < 0:
        print("Negative")

    case n if n % 2 == 0:
        print("Even")

    case _:
        print("Odd")
```

---

# Class Pattern

Pattern matching also works with classes.

```python
@dataclass
class User:

    role: str

    active: bool
```

```python
match user:

    case User(role="admin", active=True):
        print("Administrator")
```

Python automatically checks object attributes.

---

# Enterprise Examples

## HTTP Status

```python
match status:

    case 200:
        ...

    case 404:
        ...

    case 500:
        ...
```

---

## API Response

```python
match response:

    case {
        "status": "success",
        "data": data
    }:
        process(data)

    case {
        "status": "error",
        "message": message
    }:
        log(message)
```

---

## CLI Parser

```python
match command:

    case ["copy", src, dst]:
        ...

    case ["delete", filename]:
        ...

    case _:
        ...
```

---

# Advantages

- Cleaner than long if-elif chains
- Easier to maintain
- More expressive
- Supports nested structures
- Excellent for APIs and parsers

---

# Limitations

Use `match-case` only when matching **structure**.

Simple comparisons often remain clearer with `if`.

Example

```python
if age >= 18:
```

is better than

```python
match age:
```

---

# Best Practices

✔ Prefer `match-case` for structured data.

✔ Use `_` for default handling.

✔ Keep patterns simple.

✔ Don't replace every `if` statement with `match-case`.

---

# Summary

Structural Pattern Matching is one of Python's most powerful language features.

It simplifies complex decision trees by matching values, sequences, dictionaries, and even objects.