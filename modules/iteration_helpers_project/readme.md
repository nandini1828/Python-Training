# Iteration Helpers Project (Python)

A structured Python learning project that demonstrates core iteration utilities and functional tools used in real-world Python development.

This project focuses on understanding how Python handles iteration internally and how these utilities are used in backend systems, data processing, and automation scripts.

---

# 📌 Project Overview

This project is designed to strengthen understanding of Python iteration tools:

- range()
- enumerate()
- zip()
- reversed()
- sorted()
- any()
- all()

Each concept is implemented as a separate module with:
- Clean functions
- Unit tests
- Type hints
- Modular architecture

---

# 📁 Project Structure


iteration_helpers_project/
│
├── main.py # Entry point of application
├── pytest.ini # Pytest configuration
├── requirements.txt # Dependencies
│
├── iterators/ # Core logic modules
│ ├── init.py
│ ├── range_ops.py
│ ├── enumerate_ops.py
│ ├── zip_ops.py
│ ├── reversed_ops.py
│ ├── sorted_ops.py
│ ├── boolean_ops.py
│
└── tests/ # Unit tests
├── test_range_ops.py
├── test_enumerate_ops.py
├── test_zip_ops.py
├── test_reversed_ops.py
├── test_sorted_ops.py
├── test_boolean_ops.py


---

# 🚀 Features Covered

## 1. range()

Generates sequences of numbers efficiently without manually creating lists.

### Example usage:
```python
range(1, 10, 2)
# Output: [1, 3, 5, 7, 9]
## 2. enumerate()

Used to access both index and value while iterating.

Example usage:
["a", "b", "c"]
# Output: [(0, 'a'), (1, 'b'), (2, 'c')]
3. zip()

Combines multiple iterables element-wise.

Example usage:
[1, 2], ["x", "y"]
# Output: [(1, 'x'), (2, 'y')]
4. reversed()

Iterates over a sequence in reverse order without modifying original data.

Example usage:
[1, 2, 3]
# Output: [3, 2, 1]
5. sorted()

Sorts data with optional custom keys.

Example usage:
[3, 1, 2]
# Output: [1, 2, 3]
6. any() and all()

Used for boolean evaluation across iterables.

any()

Returns True if at least one value is True.

all()

Returns True only if all values are True.