# Dictionary Key Protection

Dictionary lookup with square brackets is direct, but it raises `KeyError` when
the key is missing.

This package focuses on defensive dictionary operations:

- Reading optional values with a default.
- Adding defaults without overwriting existing values.
- Updating a copied dictionary.
- Merging with override rules.
- Removing keys safely.
- Checking whether a key exists.
- Filtering a dictionary by selected keys.
- Returning an empty dictionary.

Example:

```python
from dictionary_key_protection import get_value_safe

profile = {"name": "Anika"}
print(get_value_safe(profile, "city", "Unknown"))
```

Expected output:

```python
"Unknown"
```

Prefer safe access when missing data is normal. Use direct indexing when a
missing key should be treated as a programming error.
