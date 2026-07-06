# Set Iteration

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand how sets store unique values.
- Iterate over sets safely.
- Use union, intersection, difference, and subset operations.
- Know why set iteration order should not be trusted.
- Convert lists to sets for uniqueness.
- Use sorted output when order matters.

---

# Introduction

A set is an unordered collection of unique values.

Example

```python
skills = {"python", "sql", "python", "git"}
print(skills)
```

The duplicate `"python"` appears only once.

Sets are useful when uniqueness and membership checks matter.

---

# Creating a Set

```python
numbers = {1, 2, 3}
```

From a list:

```python
values = [1, 1, 2, 3, 3]
unique_values = set(values)

print(unique_values)
```

Output

```text
{1, 2, 3}
```

---

# Iterating Over a Set

```python
skills = {"python", "sql", "git"}

for skill in skills:
    print(skill)
```

The values are all visited, but the order should not be treated as meaningful.

For display:

```python
for skill in sorted(skills):
    print(skill)
```

---

# Membership Checks

Sets are fast for membership testing.

```python
allowed_roles = {"admin", "manager", "editor"}

if "admin" in allowed_roles:
    print("Access allowed")
```

This is one of the most common real-world uses of sets.

---

# Union

Union combines values from both sets.

```python
frontend = {"html", "css", "javascript"}
backend = {"python", "sql", "javascript"}

all_skills = frontend | backend
print(all_skills)
```

Result

```python
{"html", "css", "javascript", "python", "sql"}
```

---

# Intersection

Intersection returns values common to both sets.

```python
common = frontend & backend
print(common)
```

Output

```text
{'javascript'}
```

---

# Difference

Difference returns values present in the first set but not in the second.

```python
frontend_only = frontend - backend
print(frontend_only)
```

Result

```python
{"html", "css"}
```

---

# Subset

Subset checks whether all values from one set exist in another.

```python
required = {"python", "sql"}
candidate = {"python", "sql", "git"}

print(required <= candidate)
```

Output

```text
True
```

---

# Real-World Example: Permission Checking

```python
required_permissions = {"read", "write"}
user_permissions = {"read", "write", "delete"}

if required_permissions <= user_permissions:
    print("User has enough permissions")
else:
    print("Permission denied")
```

This pattern is common in authentication and authorization systems.

---

# Real-World Example: Duplicate Removal

```python
emails = [
    "a@example.com",
    "b@example.com",
    "a@example.com",
]

unique_emails = set(emails)
```

Use a set when order is not important.

If order must be preserved, use a dictionary-based approach:

```python
unique_emails = list(dict.fromkeys(emails))
```

---

# Common Mistakes

## Mistake 1: Expecting set order

```python
list({"b", "a", "c"})
```

Do not depend on the resulting order.

## Mistake 2: Putting unhashable values in a set

```python
values = {[1, 2], [3, 4]}
```

Lists cannot be set elements because they are mutable and unhashable.

Use tuples:

```python
values = {(1, 2), (3, 4)}
```

## Mistake 3: Confusing `{}` with an empty set

```python
empty = {}
```

This creates an empty dictionary.

Use:

```python
empty = set()
```

---

# Best Practices

- Use sets for uniqueness.
- Use sets for fast membership checks.
- Sort sets before displaying them when order matters.
- Use set operations instead of manual nested loops.
- Do not store mutable values like lists inside sets.

---

# Summary

Sets are ideal for uniqueness, membership, and relationship checks.

Iteration over a set visits every value, but the order should not be part of the
program's logic.
