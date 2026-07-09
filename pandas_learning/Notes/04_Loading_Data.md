# Loading Data

## Read CSV

```python
import pandas as pd

df = pd.read_csv("employees.csv")
```

---

## Read Excel

```python
df = pd.read_excel("employees.xlsx")
```

Requires

```bash
pip install openpyxl
```

---

## Read JSON

```python
df = pd.read_json("employees.json")
```

---

## Save CSV

```python
df.to_csv("output.csv", index=False)
```

---

## Save Excel

```python
df.to_excel("output.xlsx", index=False)
```

---

## Common Parameters

```python
pd.read_csv(
    "employees.csv",
    sep=",",
    header=0,
    index_col=None
)
```

---

## Handling Encoding

```python
pd.read_csv(
    "employees.csv",
    encoding="utf-8"
)
```

---

## Reading Large Files

```python
pd.read_csv(
    "large.csv",
    chunksize=5000
)
```

---

## Interview Questions

Difference between read_csv and read_excel.

Why use index=False while saving CSV?

Explain chunksize.