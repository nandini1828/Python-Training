# Series

---

# Learning Objectives

After completing this chapter, you will be able to:

* Understand what a Pandas Series is.
* Understand why Series was introduced.
* Know when to use a Series.
* Create Series in different ways.
* Understand indexes and labels.
* Access, modify, and manipulate Series data.
* Use common Series properties and methods.
* Apply Series in real-world scenarios.
* Build a strong foundation for learning DataFrames.

---

# Prerequisites

Before learning Series, you should know:

* Variables
* Lists
* Dictionaries
* Basic Python syntax
* How to import a Python library

If you've completed **01_Introduction.md**, you're ready to continue.

---

# Problem Statement

Imagine you are a teacher managing student marks.

You have the following data:

| Student | Marks |
| ------- | ----: |
| Rahul   |    85 |
| Amit    |    92 |
| Priya   |    78 |
| Sneha   |    90 |

A beginner might store only the marks like this:

```python
marks = [85, 92, 78, 90]
```

Now someone asks:

> **"What are Amit's marks?"**

Looking at the list:

```python
[85, 92, 78, 90]
```

you only know the values.

You don't know **who** they belong to.

You could store another list:

```python
students = ["Rahul", "Amit", "Priya", "Sneha"]
marks = [85, 92, 78, 90]
```

Now both lists must always stay in the same order.

If one list changes and the other doesn't, your data becomes incorrect.

Maintaining multiple related lists becomes difficult as the data grows.

There should be a better way.

---

# Why Do We Need a Series?

Instead of keeping two separate lists, what if every value could carry its own label?

Like this:

| Student | Marks |
| ------- | ----: |
| Rahul   |    85 |
| Amit    |    92 |
| Priya   |    78 |
| Sneha   |    90 |

Now the value **92** is naturally associated with **Amit**.

This is exactly the idea behind a **Series**.

A Series stores:

* Data
* Labels (called **indexes**)

together in one object.

Instead of remembering positions like:

```text
marks[1]
```

you can think in terms of meaningful labels.

This makes your code much easier to read and maintain.

---

# Real-World Scenario

Imagine you work in an HR department.

You have employee salaries.

| Employee | Salary |
| -------- | -----: |
| Alice    |  52000 |
| Bob      |  78000 |
| Charlie  |  85000 |
| Diana    |  56000 |

Every employee has exactly one salary.

This is a perfect example of data that can be represented using a Series.

Other examples include:

* Student → Marks
* Product → Price
* Country → Population
* Month → Sales
* Subject → Grade
* Stock → Closing Price

Whenever one label maps to one value, a Series is often a good fit.

---

# What Is a Series?

A **Series** is a **one-dimensional labeled data structure** provided by Pandas.

Let's understand this definition one part at a time.

### One-dimensional

A Series contains a **single column** of data.

Example:

| Salary |
| -----: |
|  52000 |
|  78000 |
|  85000 |
|  56000 |

Unlike a DataFrame, it does not have multiple columns.

---

### Labeled

Every value has an associated **index**.

Example:

|   Index | Salary |
| ------: | -----: |
|   Alice |  52000 |
|     Bob |  78000 |
| Charlie |  85000 |
|   Diana |  56000 |

The labels make it easier to identify data.

---

### Data Structure

A data structure is simply a way of organizing data so that it can be stored, accessed, and manipulated efficiently.

Python gives us data structures like:

* List
* Tuple
* Dictionary
* Set

Pandas provides:

* Series
* DataFrame

These are optimized specifically for working with structured data.

---

# Visual Representation

A Python list looks like this:

```text
Index

0 → 85

1 → 92

2 → 78

3 → 90
```

A Series can look like this:

```text
Rahul → 85

Amit → 92

Priya → 78

Sneha → 90
```

Notice the difference.

The labels are meaningful.

This makes the data easier to understand and easier to work with.

---

# Series vs Python List

| Python List               | Pandas Series                      |
| ------------------------- | ---------------------------------- |
| Stores values             | Stores values with labels          |
| General-purpose           | Designed for data analysis         |
| Basic operations          | Rich analytical operations         |
| Limited built-in analysis | Many built-in analytical methods   |
| Mostly position-based     | Supports both labels and positions |

Lists are excellent for general programming.

Series are designed for data analysis.

---

# Did You Know?

💡 A **Series** is one of the two fundamental data structures in Pandas.

The other one is the **DataFrame**.

In fact, every column inside a DataFrame is itself a Series.

Understanding Series first makes DataFrames much easier to learn.

---

# Chapter Summary

In this part, you learned:

* The problem that Series solves.
* Why labels are important.
* What a Series is.
* Why it is different from a Python list.
* Where Series is used in real-world applications.

In the next section, we'll learn how to create a Series in different ways and understand its syntax.

---

# Importing Pandas

Before using any feature from Pandas, we need to import the library.

```python
import pandas as pd
```

Let's understand this statement.

## import

`import` is a Python keyword used to bring a library into your program.

Without importing Pandas, Python does not know what Pandas is.

---

## pandas

This is the actual library name.

It contains hundreds of classes, functions, and utilities for working with data.

---

## as

`as` creates an alias (a shorter name).

Instead of writing:

```python
pandas.Series(...)
```

we can write:

```python
pd.Series(...)
```

Almost every Python developer uses `pd` as the alias for Pandas.

This is the standard convention.

---

# Creating Your First Series

The simplest way to create a Series is from a Python list.

Example:

```python
import pandas as pd

marks = pd.Series([85, 92, 78, 90])

print(marks)
```

### Output

```text
0    85
1    92
2    78
3    90
dtype: int64
```

---

# Understanding the Output

Let's examine the output carefully.

```text
0    85
1    92
2    78
3    90
dtype: int64
```

### Left Side

```text
0
1
2
3
```

These are the **indexes**.

Since we didn't provide custom labels, Pandas automatically generated indexes starting from **0**.

These are called **default indexes**.

---

### Right Side

```text
85
92
78
90
```

These are the actual values stored in the Series.

---

### Last Line

```text
dtype: int64
```

This tells us the data type of the values.

Here:

* `int` means integer.
* `64` refers to the storage size (64-bit integer).

For now, simply remember:

> `dtype` tells us what type of data the Series stores.

We'll learn more about data types later.

---

# How Pandas Creates a Series Internally

When you write:

```python
marks = pd.Series([85, 92, 78, 90])
```

Pandas internally creates something similar to:

| Index | Value |
| ----: | ----: |
|     0 |    85 |
|     1 |    92 |
|     2 |    78 |
|     3 |    90 |

Notice that both the **values** and their **indexes** are stored together.

This is one of the biggest advantages of a Series.

---

# Creating a Series with Custom Index

Instead of using numbers, we can provide meaningful labels.

Example:

```python
import pandas as pd

marks = pd.Series(
    [85, 92, 78, 90],
    index=["Rahul", "Amit", "Priya", "Sneha"]
)

print(marks)
```

### Output

```text
Rahul    85
Amit     92
Priya    78
Sneha    90
dtype: int64
```

Now the Series is much easier to understand.

Instead of asking:

> What is the value at index 1?

we can ask:

> What are Amit's marks?

Meaningful indexes make the data self-explanatory.

---

# Why Use Custom Indexes?

Consider these two outputs.

### Default Index

```text
0    52000
1    78000
2    85000
3    56000
```

Can you immediately identify whose salary is whose?

No.

---

### Custom Index

```text
Alice      52000
Bob        78000
Charlie    85000
Diana      56000
```

Now the information is much clearer.

Whenever possible, use labels that describe the data.

---

# Creating a Series from a Dictionary

A dictionary already stores data as **key → value** pairs.

Pandas uses:

* Dictionary keys as indexes.
* Dictionary values as Series values.

Example:

```python
import pandas as pd

employee_salary = {
    "Alice": 52000,
    "Bob": 78000,
    "Charlie": 85000,
    "Diana": 56000
}

salary = pd.Series(employee_salary)

print(salary)
```

### Output

```text
Alice      52000
Bob        78000
Charlie    85000
Diana      56000
dtype: int64
```

Notice that we didn't have to specify the `index` parameter.

Pandas automatically used the dictionary keys as labels.

---

# When Should You Use a List or a Dictionary?

### Use a List when:

* You only have values.
* Labels are not important.
* You are creating quick examples.

### Use a Dictionary when:

* Every value has a meaningful name.
* Labels already exist.
* You want more readable data.

In real-world projects, both approaches are common depending on how the data is available.

---

# Quick Revision

✔ Import Pandas using:

```python
import pandas as pd
```

✔ A Series can be created from a Python list.

✔ If no index is provided, Pandas creates a default numeric index.

✔ You can provide your own custom indexes.

✔ A dictionary naturally maps to a Series because keys become indexes and values become the data.

---

# Did You Know?

💡 A Series does **not** require the index to be numeric.

Indexes can be:

* Names
* Product IDs
* Dates
* Employee IDs
* Email addresses

As long as the labels uniquely identify the data, they can be used as indexes.
