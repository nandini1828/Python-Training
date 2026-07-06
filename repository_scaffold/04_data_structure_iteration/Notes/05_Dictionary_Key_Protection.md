# Dictionary Key Protection

Use safe dictionary access methods to avoid runtime errors.

Direct access is useful when a key must exist:

```python
name = profile["name"]
```

If `"name"` is missing, Python raises `KeyError`.

Use `.get()` when missing data is expected:

```python
city = profile.get("city", "Unknown")
```

Use `.setdefault()` when you want to add a fallback value only if the key is
missing:

```python
profile.setdefault("country", "India")
```

Use `.pop(key, default)` for safe removal:

```python
profile.pop("temporary", None)
```

Choosing the right access pattern makes the code's intent visible. Missing data
can either be normal input or a bug; the lookup style should communicate which
one it is.
