# Introduction

Data structure iteration means visiting each value inside a collection and doing
something useful with it.

Python makes this readable:

```python
for item in collection:
    print(item)
```

The same loop shape works across many data structures, but each structure has
different rules.

- Lists are ordered and allow duplicates.
- Dictionaries store key/value pairs.
- Sets store unique values and do not provide meaningful ordering guarantees.

Good iteration code should make the data shape obvious. A reader should be able
to tell whether the loop needs values only, indexes and values, dictionary keys,
dictionary values, or full key/value pairs.

This module uses utility functions so each operation can be tested directly.
That mirrors real project practice: business logic belongs in reusable helpers,
while demos and scripts should stay thin.
