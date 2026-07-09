# Working with Date and Time

## Introduction

Many real-world datasets contain date and time information.

Examples

- Sales
- Banking
- Stock Market
- IoT
- Healthcare

---

# Convert to Datetime

```python
df["order_date"] = pd.to_datetime(df["order_date"])
```

---

# Datetime Components

Year

```python
df["order_date"].dt.year
```

Month

```python
df["order_date"].dt.month
```

Day

```python
df["order_date"].dt.day
```

Weekday

```python
df["order_date"].dt.day_name()
```

Hour

```python
df["order_date"].dt.hour
```

Quarter

```python
df["order_date"].dt.quarter
```

---

# Date Filtering

```python
df[
    df["order_date"] >= "2024-03-01"
]
```

---

# Sort Dates

```python
df.sort_values("order_date")
```

---

# Difference Between Dates

```python
df["delivery_days"] = (
    df["delivery_date"]
    - df["order_date"]
).dt.days
```

---

# Current Date

```python
pd.Timestamp.now()
```

---

# Date Range

```python
pd.date_range(
    start="2024-01-01",
    end="2024-01-10"
)
```

---

# Resampling

Monthly sales

```python
df.resample(
    "M",
    on="order_date"
)["price"].sum()
```

---

# Common Date Formats

```
YYYY-MM-DD

DD-MM-YYYY

MM/DD/YYYY
```

---

# Best Practices

- Always convert strings to datetime.
- Store dates in ISO format.
- Sort dates before time-series analysis.
- Avoid comparing strings as dates.

---

# Interview Questions

1. Why use `to_datetime()`?
2. Difference between string and datetime.
3. What does `.dt` do?
4. Explain resampling.
5. How do you filter a date range?