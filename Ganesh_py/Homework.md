# Python Data Types: The Exhaustive Mastery Guide

This document is a complete, deep-dive reference manual and exercise sheet. It is designed to take junior developers from a basic understanding of Python to complete proficiency in primitives, introspection, collections, serialization, and object memory internals.

---

## Section 1: Primitives, Introspection, & Naming Conventions

In Python, **everything is an object**. There are no raw primitives like in C++ or Java; even the number `5` is an instance of the class `int`.

### 1.1 Deep-Dive Introspection
At runtime, you can inspect any object using Python's built-in tools:
* `type(obj)`: Returns the type object representing the class of `obj`.
* `dir(obj)`: Returns a list of all attribute and method names available on `obj`.
* `id(obj)`: Returns the unique integer identifier (memory address in CPython) of the object.

Example:
```python
x = 100
print(type(x))  # <class 'int'>
print(id(x))    # Unique memory address (e.g., 4355083920)
```

### 1.2 Dunder (Double Underscore) Methods & Operator Overloading
Operators in Python are shortcuts for calling magic methods. When you use an operator, Python translates it behind the scenes:

| Operator / Action | Equivalent Python Call |
| :--- | :--- |
| `a + b` | `a.__add__(b)` |
| `a - b` | `a.__sub__(b)` |
| `a * b` | `a.__mul__(b)` |
| `a == b` | `a.__eq__(b)` |
| `len(a)` | `a.__len__()` |
| `str(a)` | `a.__str__()` |
| `repr(a)` | `a.__repr__()` |

Example:
```python
# Standard syntax:
res1 = "hello" + " world"

# Dunder syntax:
res2 = "hello".__add__(" world")
```

### 1.3 Underscore Naming Conventions
Python has no access modifiers like `public`, `protected`, or `private`. It uses naming conventions:

1. **Single leading underscore (`_variable`)**:
   * Indicates an internal variable or method.
   * **Convention only:** Developers can still access it, but it signals: *"This is implementation detail. Do not touch."*
   * Prevents import when using `from module import *`.

2. **Double leading underscore (`__variable`)**:
   * Triggers **Name Mangling**.
   * Python automatically renames the attribute to `_ClassName__variable` in the background.
   * Used to prevent namespace collisions in inherited classes.

3. **Double leading and trailing underscore (`__dunder__`)**:
   * Reserved for Python's built-in system methods (like `__init__`, `__str__`). Never define your own.

---

### Exercises: Section 1
#### Exercise 1.1: The Dunder Rewrite
Rewrite the following standard Python operations using only dunder methods:
```python
# 1. Check if 15 is equal to 15
# Standard: 15 == 15
# Rewrite:
(15).__eq__(15)

# 2. Get the absolute value of -42
# Standard: abs(-42)
# Rewrite:
(-42).__abs__()

# 3. Check if "Py" is a substring of "Python"
# Standard: "Py" in "Python"
# Rewrite:
"Python".__contains__("Py")
```

#### Exercise 1.2: Introspection Public Scanner
Write a function `list_public_attributes(obj)` that returns a list of names of all attributes/methods of `obj` that are **public** (i.e., do not start with a single or double underscore).
```python
def list_public_attributes(obj):
    return [
        attribute
        for attribute in dir(obj)
        if not attribute.startswith("_")
    ]
```

---

## Section 2: Type Checking & Castin

### 2.1 `type()` vs `isinstance()`
* **`type(x) == class`**: Checks if `x` is *exactly* that class. It does not account for subclasses (inheritance).
* **`isinstance(x, class)`**: Returns `True` if `x` is that class or a subclass of it. Always use `isinstance()`.

```python
class Animal: pass
class Dog(Animal): pass

d = Dog()

print(type(d) == Animal)  # False (Strict match only)
print(isinstance(d, Animal))  # True (Accounts for inheritance)
```

### 2.2 Truthiness (Truthy vs Falsy)
Any value in Python can be checked for its boolean value.
* **Falsy values (evaluate to `False`)**:
  * `None`
  * `False`
  * Zero of any numeric type: `0`, `0.0`, `0j`
  * Empty sequences/collections: `""`, `[]`, `()`, `{}`, `set()`
* **Truthy values**: Anything else.

### 2.3 Safe Casting & Edge Cases
Casting converts data types. You must be aware of truncation and format requirements:
* `int(9.999)` $\rightarrow$ `9` (Decimals are truncated/dropped, not rounded).
* `int("-5")` $\rightarrow$ `-5` (Negative integers cast fine).
* `int("12.3")` $\rightarrow$ Raises `ValueError` because the string doesn't look like an integer.
* `float("inf")` and `float("-inf")` $\rightarrow$ Valid representations of infinity.

---

### Exercises: Section 2
#### Exercise 2.1: Safe Conversions
Implement `safe_cast(value, target_type, default=None)` to convert `value` to `target_type`. If conversion fails, return `default`.
```python
def safe_cast(value, target_type, default=None):
    try:
        return target_type(value)
    except (ValueError, TypeError):
        return default

# Test cases:
# safe_cast("12.5", float) -> 12.5
# safe_cast("12.5", int) -> None (or default)
# safe_cast("abc", int, default=0) -> 0
```

#### Exercise 2.2: The Truthiness Auditor
Write a function `count_truthy_falsy(items)` that takes a list of various items and returns a dictionary with the count of truthy and falsy values.
```python
def count_truthy_falsy(items):
    result = {"truthy": 0, "falsy": 0}

    for item in items:
        if item:
            result["truthy"] += 1
        else:
            result["falsy"] += 1

    return result

# Input: [0, "hello", [], None, True, 3.14]
# Output: {"truthy": 3, "falsy": 3}
```

---

## Section 3: Lists, Tuples, & Sets (Exhaustive)

### 3.1 Lists (Mutable Sequences)
Here is every public list method with a clear example:

* **`append(x)`**: Adds item `x` to the very end.
  ```python
  x = [1, 2]
  x.append(3)  # x is now [1, 2, 3]
  ```
* **`extend(iterable)`**: Appends elements from another iterable (e.g., list, set, tuple).
  ```python
  x = [1, 2]
  x.extend([3, 4])  # x is now [1, 2, 3, 4]
  ```
* **`insert(index, x)`**: Inserts `x` at a specific `index`.
  ```python
  x = [1, 3]
  x.insert(1, 2)  # x is now [1, 2, 3]
  ```
* **`remove(x)`**: Removes the *first* occurrence of value `x`. Raises `ValueError` if not found.
  ```python
  x = [1, 2, 3, 2]
  x.remove(2)  # x is now [1, 3, 2]
  ```
* **`pop(index=-1)`**: Removes and returns the item at `index`. If no index specified, removes the last item.
  ```python
  x = [10, 20, 30]
  val = x.pop(0)  # val = 10, x = [20, 30]
  ```
* **`clear()`**: Removes all items from the list.
  ```python
  x = [1, 2]
  x.clear()  # x is now []
  ```
* **`index(x, [start, [stop]])`**: Returns the index of the first item equal to `x`.
  ```python
  x = ["a", "b", "c"]
  print(x.index("b"))  # 1
  ```
* **`count(x)`**: Returns the number of times `x` appears.
  ```python
  x = [1, 2, 2, 3]
  print(x.count(2))  # 2
  ```
* **`sort(key=None, reverse=False)`**: Sorts the list in-place.
  ```python
  x = [3, 1, 2]
  x.sort()  # x is now [1, 2, 3]
  ```
* **`reverse()`**: Reverses list elements in-place.
  ```python
  x = [1, 2, 3]
  x.reverse()  # x is now [3, 2, 1]
  ```
* **`copy()`**: Returns a shallow copy of the list.
  ```python
  x = [1, 2]
  y = x.copy()
  ```

### 3.2 Tuples (Immutable Sequences)
Tuples cannot be modified after creation. They only have two methods:
* **`count(x)`**: Returns occurrences of `x`.
* **`index(x)`**: Returns first index of `x`.

### 3.3 Sets (Unordered Collections of Unique Elements)
Sets cannot contain duplicates. They are highly optimized for membership testing (`x in my_set`).

* **`add(x)`**: Adds element `x`.
  ```python
  s = {1, 2}
  s.add(3)  # s is now {1, 2, 3}
  ```
* **`remove(x)`**: Removes `x`. Raises `KeyError` if `x` is not present.
* **`discard(x)`**: Removes `x`. Does not raise an error if `x` is missing.
* **`pop()`**: Removes and returns an arbitrary element. Raises `KeyError` on empty set.
* **`clear()`**: Clears all elements.
* **`union(*others)`** (or `|`): Combines multiple sets.
  ```python
  {1, 2}.union({2, 3})  # {1, 2, 3}
  ```
* **`intersection(*others)`** (or `&`): Finds common elements.
  ```python
  {1, 2}.intersection({2, 3})  # {2}
  ```
* **`difference(*others)`** (or `-`): Elements in first set but not in others.
  ```python
  {1, 2} - {2, 3}  # {1}
  ```
* **`symmetric_difference(other)`** (or `^`): Elements in either set but not both.
  ```python
  {1, 2} ^ {2, 3}  # {1, 3}
  ```
* **`issubset(other)`**: Checks if all elements are in `other`.
* **`issuperset(other)`**: Checks if all elements of `other` are in this set.
* **`isdisjoint(other)`**: Returns `True` if sets have no common elements.

---

### Exercises: Section 3
#### Exercise 3.1: The Custom Queue (List methods)
Write a class `SimpleQueue` that uses a list internally:
* `enqueue(item)`: Adds to the end of the list.
* `dequeue()`: Removes and returns from the front of the list.
* `size()`: Returns current size.
```python
class SimpleQueue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.items:
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def size(self):
        return len(self.items)
```

#### Exercise 3.2: Tag Merger (Sets)
Write a function `merge_tags(tags_a, tags_b)` that takes two lists of strings, converts them to lowercase, removes duplicates, and returns:
1. A sorted list of all unique tags.
2. A sorted list of tags that are shared by both.
3. A sorted list of tags present in `tags_a` but not in `tags_b`.
```python
def merge_tags(tags_a, tags_b):
    set_a = {tag.lower() for tag in tags_a}
    set_b = {tag.lower() for tag in tags_b}

    return (
        sorted(set_a | set_b),
        sorted(set_a & set_b),
        sorted(set_a - set_b)
    )
```

---

## Section 4: Dictionaries & JSON

### 4.1 Dictionary Methods (Exhaustive)
* **`get(key, default=None)`**: Safely retrieves the value of a key.
  ```python
  d = {"a": 1}
  print(d.get("b", 0))  # 0 (Doesn't crash!)
  ```
* **`setdefault(key, default)`**: Returns value if key is present; otherwise inserts key with `default` and returns `default`.
  ```python
  d = {}
  d.setdefault("fruits", []).append("apple")  # d becomes {"fruits": ["apple"]}
  ```
* **`keys()`**: Returns a view of keys.
* **`values()`**: Returns a view of values.
* **`items()`**: Returns a view of `(key, value)` tuples.
* **`update(other_dict)`**: Updates dictionary in-place with key-value pairs from `other_dict`.
* **`pop(key, [default])`**: Removes key and returns its value. Raises `KeyError` if key is missing and no default is provided.
* **`popitem()`**: Removes and returns the last inserted `(key, value)` tuple.
* **`clear()`**: Clears all items.
* **`copy()`**: Shallow copy of dictionary.
* **`fromkeys(seq, [value])`**: Class method creating a new dictionary with keys from sequence and values set to `value`.

### 4.2 JSON Serialization vs Python Structures
JSON is a data format represented as a string. When Python's `json` library parses a JSON string, it maps elements to nested Python dictionaries, lists, and primitives.

Consider a nested profile representing a person:
```json
{
  "name": "Jane",
  "hobbies": ["cooking", "reading"],
  "address": {
    "city": "Boston",
    "zip": 02111
  }
}
```

In Python, this is represented as:
```python
profile = {
    "name": "Jane",                    # str
    "hobbies": ["cooking", "reading"], # list of str
    "address": {                       # nested dict
        "city": "Boston",              # str
        "zip": 2111                    # int
    }
}
```
At the leaf level, every complex JSON structure is just primitive data types (`str`, `int`, `float`, `bool`, `None`).

---

### Exercises: Section 4
#### Exercise 4.1: Nested JSON Query Engine
Write a function `query_json(data_dict, path_str, default=None)` that queries a nested dictionary using a dot-separated path string.
```python
def query_json(data_dict, path_str, default=None):
    current = data_dict

    for key in path_str.split("."):
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default

    return current

# Example:
# data = {"user": {"profile": {"name": "Alice"}}}
# query_json(data, "user.profile.name") -> "Alice"
# query_json(data, "user.profile.age", 18) -> 18
```

#### Exercise 4.2: Vocabulary Word Count
Given a string of text, count the frequency of each word. Return a dictionary.
* Ignore case (convert words to lowercase).
* Ignore punctuation characters: `.`, `,`, `!`, `?`
* Use `setdefault` or `get`.
```python
def word_count(text):
    for symbol in ".,!?":
        text = text.replace(symbol, "")

    words = text.lower().split()
    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts
```

---

## Section 5: Classes, Composition, & `self`

### 5.1 Understanding Class Instances & Memory
A class is a blueprint. An instance is an allocated space in memory representing the object.
* `self` is a reference to the **instance itself in memory**.
* When you call `obj.my_method()`, Python passes `obj` as the first argument (`self`) under the hood: `MyClass.my_method(obj)`.

### 5.2 Everything boils down to Primitives & `__dict__`
No matter how complex classes get, their state is stored inside a standard Python dictionary: `instance.__dict__`.

Let's look at composition:
```python
class CPU:
    def __init__(self, cores):
        self.cores = cores  # int (primitive)

class Computer:
    def __init__(self, brand, cpu):
        self.brand = brand  # str (primitive)
        self.cpu = cpu      # CPU (composition)

my_pc = Computer("Dell", CPU(8))
```
If we inspect the instances:
```python
print(my_pc.__dict__)
# Output: {'brand': 'Dell', 'cpu': <__main__.CPU object at 0x104b38d30>}

print(my_pc.cpu.__dict__)
# Output: {'cores': 8}
```
Every object contains nested objects, but at the leaves, it boils down to the strings and integers: `"Dell"` and `8`.

---

### Exercises: Section 5
#### Exercise 5.1: Proving the Dict Underbelly
Create a simple class:
```python
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)
```
Write a script to:
1. Create a blank instance of `Student` without calling `Student("Name", [...])`. (Hint: Use `Student.__new__(Student)`).
2. Manually populate its `name` and `grades` attributes by writing directly to the instance's `__dict__`.
3. Call `average_grade` using unbound class syntax: `Student.average_grade(your_instance)`.
```python
student = Student.__new__(Student)

student.__dict__["name"] = "Ganesh"
student.__dict__["grades"] = [90, 95, 100]

print(Student.average_grade(student))
```

#### Exercise 5.2: Deep Object Deconstructor
Write a function `deconstruct_object(obj)` that takes any custom class instance and recursively converts it (including all nested objects) into nested dictionaries representing their `__dict__` state, leaving primitive types untouched.
```python
def deconstruct_object(obj):

    if isinstance(obj, (int, float, str, bool, type(None))):
        return obj

    if isinstance(obj, list):
        return [deconstruct_object(item) for item in obj]

    if isinstance(obj, dict):
        return {
            key: deconstruct_object(value)
            for key, value in obj.items()
        }

    if hasattr(obj, "__dict__"):
        return {
            key: deconstruct_object(value)
            for key, value in obj.__dict__.items()
        }

    return str(obj)
```
 