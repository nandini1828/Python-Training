# Best Practices for Control Flow

---

# Write Readable Code

Readable code is more valuable than clever code.

Good

```python
if is_authenticated:
    ...
```

Poor

```python
if auth == True:
    ...
```

---

# Keep Conditions Small

Bad

```python
if (
    age >= 18
    and verified
    and salary > 50000
    and score > 750
    and not blocked
):
```

Better

```python
eligible = (
    age >= 18
    and verified
    and salary > 50000
)

if eligible and not blocked:
```

---

# Use Guard Clauses

Instead of

```python
if user:

    if user.active:

        process()
```

Prefer

```python
if not user:
    return

if not user.active:
    return

process()
```

---

# Avoid Deep Nesting

Avoid

```
if

↓

if

↓

if

↓

if
```

Deep nesting becomes difficult to maintain.

---

# Prefer Truthiness

Instead of

```python
if len(items) > 0:
```

Use

```python
if items:
```

---

# Avoid Comparing with True

Poor

```python
if flag == True:
```

Better

```python
if flag:
```

---

# Use Parentheses

Good

```python
if (
    authenticated
    and verified
    and not blocked
):
```

Much easier to read.

---

# Use Short-Circuit Evaluation

Instead of

```python
if cache:

    data = cache

else:

    data = database()
```

Use

```python
data = cache or database()
```

---

# Keep Ternary Operators Simple

Good

```python
status = "Adult" if age >= 18 else "Minor"
```

Avoid

```python
result = (
    ...
    if ...
    else ...
    if ...
    else ...
)
```

---

# Choose match-case Carefully

Use

```
API parsing

Commands

Tokens

Enums

Protocols
```

Don't use it for every simple condition.

---

# Name Boolean Variables Clearly

Good

```
is_logged_in

has_permission

is_admin

can_edit
```

Poor

```
flag

x

status
```

---

# Avoid Magic Numbers

Instead of

```python
if age >= 18:
```

Use

```python
LEGAL_AGE = 18

if age >= LEGAL_AGE:
```

---

# Return Early

Good

```python
if not authenticated:
    return

process()
```

---

# Write Testable Functions

Instead of

```python
print("Approved")
```

Return

```python
return "Approved"
```

---

# Follow PEP 8

- Four-space indentation
- Meaningful names
- Maximum readability
- Blank lines between functions
- Type hints

---

# Enterprise Checklist

Before writing an if statement ask yourself

- Is it readable?
- Can it be simplified?
- Should it become a separate function?
- Is nesting necessary?
- Can I use a guard clause?

---

# Common Mistakes

❌ Deep nesting

❌ Huge conditions

❌ Comparing with True

❌ Ignoring operator precedence

❌ Long nested ternary operators

❌ Repeating conditions

---

# Summary

Professional Python developers optimize for readability first.

The best code is the one another developer can understand immediately.