# Iterators & Generators (Under the Hood)

## Overview

This module explores how iteration actually works inside Python. Every `for` loop relies on the Iterator Protocol, while generators provide a powerful mechanism for processing large datasets efficiently using lazy evaluation.

The concepts are demonstrated through an **Online Book Store** that processes books, coupons, and pricing information without loading unnecessary data into memory.

---

## Concepts Covered

### Iterator Protocol

Understanding how Python internally uses `__iter__()` and `__next__()` to iterate through collections.

### Generators and yield

Learning how generator functions pause and resume execution, producing values one at a time instead of creating entire collections in memory.

### Generator Expressions

Using generator expressions to process large datasets efficiently while minimizing memory usage.

---

## What This Project Demonstrates

- Internal working of Python loops
- Building custom iterators
- Lazy evaluation
- Streaming data efficiently
- Memory optimization techniques

---

## Learning Outcomes

After completing this module, you will understand how Python performs iteration internally, create custom iterators, use generators for scalable applications, and write memory-efficient programs suitable for real-world backend systems.