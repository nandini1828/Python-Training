# Python Iteration Helpers

A beginner-friendly Python project that demonstrates the fundamentals of Python iteration helper functions using a real-world **inventory and order management system**.

---

## About the Project

This module explains how to use Python's built-in iteration helpers in practical scenarios. It covers:

- `range(start, stop, step)`
- `enumerate()`
- `zip()`
- `zip_longest()` from `itertools`
- `reversed()`
- `sorted()` with custom `key`
- `any()`
- `all()`

---

## Project Structure

```text
iteration_helpers/
│
├── main.py
├── readme.md
├── __init__.py
├── iteration_helpers.py
└── tests/
    ├── __init__.py
    └── test_iteration_helpers.py
```

---

## Topics Covered

### `range(start, stop, step)`
Generate numeric sequences efficiently for batch processing, action scheduling, and progress iteration.

### `enumerate()`
Retrieve both the index and value of elements side-by-side, useful for labeled inventory listings and position tracking.

### `zip()`
Iterate over multiple lists in parallel, keeping related elements matched together.

### `zip_longest()`
Handle lists of unequal lengths safely by filling missing elements with a default value.

### `reversed()`
Loop backwards through a collection without modifying it in place.

### `sorted()`
Iterate over sorted collections with custom keys, such as sorting by price or date.

### `any()` and `all()`
Check if any or all items in an iterable satisfy a condition, useful for audits and readiness checks.

---

## Running the Project

### Interactive Menu
```bash
cd /Users/wallstreet/Python-Training/iteration_helpers
python main.py
```

### Direct Module Execution
```bash
python iteration_helpers.py
```

---

## Real-World Examples

This project uses practical inventory and order examples:

- Generating daily order batches
- Indexing inventory items
- Matching products with quantities
- Reviewing recent shipments
- Sorting products by price
- Sorting orders by date
- Checking low-stock conditions
- Verifying order readiness

---

## How to Use

1. Run the interactive menu
2. Choose the helper you want to explore
3. Study the example output
4. Open `iteration_helpers.py` to read the implementation
5. Run tests to confirm behavior

---

## Notes

- The examples are intentionally simple and easy to extend.
- Custom `key` functions show real-world sorting logic.
- `zip_longest()` is used to safely iterate over unequal lists.
- `any()` and `all()` demonstrate boolean aggregation patterns.
