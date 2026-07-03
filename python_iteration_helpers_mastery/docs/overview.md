# Iteration Helpers Overview

This module focuses on Python iteration helper functions.

## Implemented Topics

### 1. range(start, stop, step)
Implemented in:

- `iteration_helpers/range_helper.py`

Purpose:
- Generate sequence ranges efficiently.

---

### 2. enumerate()
Implemented in:

- `iteration_helpers/enumerate_helper.py`

Purpose:
- Retrieve both index and value side-by-side.

---

### 3. zip() and zip_longest()
Implemented in:

- `iteration_helpers/zip_helper.py`

Purpose:
- Iterate over multiple lists in parallel.
- Handle unequal length iterables using `zip_longest()`.

---

### 4. reversed() and sorted()
Implemented in:

- `iteration_helpers/reverse_sort_helper.py`

Purpose:
- Reverse collections without modifying them in-place.
- Sort values and records using default sorting or custom keys.

---

### 5. any() and all()
Implemented in:

- `iteration_helpers/any_all_helper.py`

Purpose:
- Check whether any or all values in an iterable satisfy a condition.

---

## Testing

Pytest files are available in the `tests/` folder for validating all helper modules.