# Introduction to Comprehensions & Generators

---

# Learning Objectives

After completing this chapter, you will understand:

- What comprehensions are
- Different types of comprehensions
- What generators are
- Why generators are memory efficient
- Iterator Protocol overview
- Enterprise use cases

---

# Why Comprehensions?

Python follows the philosophy:

> "Simple is better than complex."

Comprehensions allow us to write cleaner and shorter code for creating collections.

Instead of writing several lines of loops, we can create collections using a single expression.

---

# Types of Comprehensions

Python provides three comprehension types:

- List Comprehensions
- Dictionary Comprehensions
- Set Comprehensions

Nested comprehensions can also be used for multidimensional data.

---

# Why Generators?

Normally, Python creates an entire collection in memory.

Example

```python
numbers = [x for x in range(1_000_000)]
```

This consumes a large amount of memory.

Generators solve this problem by producing values one at a time.

---

# What is Lazy Evaluation?

Lazy evaluation means values are generated only when they are needed.

Instead of storing one million numbers, Python calculates the next value only when requested.

---

# Enterprise Use Cases

Comprehensions

- Data transformation
- API response processing
- Database query formatting
- Configuration mapping

Generators

- Large file processing
- Streaming data
- ETL pipelines
- Log analysis
- Machine Learning datasets

---

# Benefits

✔ Cleaner code

✔ Better readability

✔ Less memory usage

✔ Faster development

✔ Pythonic programming

---

# Summary

Comprehensions simplify collection creation, while generators provide memory-efficient lazy evaluation for large datasets.