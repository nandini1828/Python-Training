# Introspection

Concept Overview

Utilities for inspecting Python objects at runtime using the `inspect` module.

Why It Exists

To demonstrate dynamic analysis and build tools that can be used in debugging,
APIs and developer tooling.

Example Code

```py
from introspection import inspect_object
print(inspect_object([1,2,3]))
```

Expected Output

JSON-like metadata describing the list: methods, attributes, mro, etc.
