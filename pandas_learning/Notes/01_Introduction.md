# Introduction to Pandas

## What is Pandas?

Pandas is an open-source Python library used for data manipulation and analysis.

It provides fast, flexible, and expressive data structures that make working with structured data easy.

---

## Why Pandas?

Without Pandas

- Reading CSV files is difficult
- Filtering data requires loops
- Aggregation is manual
- Missing values are hard to handle

With Pandas

- Read CSV in one line
- Filter using conditions
- Aggregate using groupby()
- Handle missing values easily
- Join multiple datasets

---

## Features

- Fast
- Easy to learn
- Built on NumPy
- Excellent CSV/Excel support
- Powerful indexing
- Handles missing data
- Time series support

---

## Installation

```bash
pip install pandas
```

Check version

```python
import pandas as pd

print(pd.__version__)
```

---

## Import

```python
import pandas as pd
```

`pd` is the standard alias.

---

## Real World Usage

Pandas is widely used in:

- Data Analysis
- Data Engineering
- Machine Learning
- Business Intelligence
- Finance
- Banking
- Healthcare
- Research

---

## Advantages

- Less code
- Faster development
- Easy visualization integration
- Rich API
- Large community

---

## Limitations

- Works in memory
- Not suitable for extremely large datasets
- Slower than distributed frameworks like Spark for big data

---

## Interview Questions

### What is Pandas?

A Python library for data manipulation and analysis.

---

### Why is Pandas built on NumPy?

NumPy provides fast numerical arrays, while Pandas adds labels, indexing, and tabular data structures.

---

### What are the two main data structures?

- Series
- DataFrame