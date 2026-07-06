# Iterator Protocol

The iterator protocol is the contract behind `for` loops.

An iterator provides:

- `__iter__`, which returns the iterator object.
- `__next__`, which returns the next value or raises `StopIteration`.

This package includes:

- `CountDown`, a small custom iterator.
- `is_iterable`, a safe iterable check using `iter`.
- `get_first`, which reads the first item from an iterable.
- `collect_iterator`, which collects remaining values.
- `manual_next`, which wraps `next` with a default value.

Iterator objects are stateful. Once a value is consumed, it is gone from that
iterator.
