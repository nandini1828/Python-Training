# Generators

Generator functions use `yield` to produce values one at a time.

This package includes generators for:

- Natural numbers.
- Fibonacci numbers.
- Filtering numbers above a threshold.
- Reading line-like strings.
- Batching values into fixed-size groups.

Generators are useful when:

- The full result may be large.
- Values can be processed one at a time.
- You want pipeline-style code.

Once a generator is exhausted, it does not restart. Create a new generator when
you need to iterate again.
