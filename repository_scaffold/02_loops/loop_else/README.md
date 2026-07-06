# Loop with Else in Python

## 📌 What is Loop-Else?

In Python, both `for` and `while` loops can have an `else` block.

👉 The `else` block executes **only if the loop completes normally**  
👉 It does **NOT execute if the loop is terminated by `break`**

---

## 🧠 Key Rule (VERY IMPORTANT)

| Situation              | else runs? |
|----------------------|-----------|
| Loop completes fully | ✅ YES     |
| Loop breaks early    | ❌ NO      |

---

## 🔹 Syntax

### For Loop

```python
for item in iterable:
    if condition:
        break
else:
    # runs only if no break occurred