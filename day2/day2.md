Day 2 - Advanced Python Collections, Introspection and JSON Processing

Overview

This module focuses on Python collections, dunder methods, type casting, JSON processing, introspection, and unit testing.

⸻

Folder Structure

core/

Contains reusable implementations.

queue.py

Implemented a custom queue using collections.deque.

Features:

* enqueue()
* dequeue()
* size()
* is_empty()

type_casting.py

Implemented:

* String to float conversion
* Integer to string conversion
* Float to integer conversion
* Safe casting utility

dunder_demo.py

Demonstrates Python magic methods:

* add()
* eq()
* contains()
* abs()

json_query_engine.py

Implemented nested JSON querying using dot-separated paths.

Example:

user.profile.name

Features:

* Nested dictionary traversal
* Safe lookup
* Default values

⸻

examples/

Contains practical demonstrations.

collections_examples.py

Demonstrates:

* Queue operations
* Set operations
* Tag merging

introspection_examples.py

Demonstrates:

* type()
* id()
* dir()
* Runtime object inspection

json_examples.py

Demonstrates:

* Nested JSON queries
* Dictionary traversal
* Safe data retrieval

⸻

tests/

Contains unit tests.

test_queue.py

Tests:

* Queue insertion
* Queue removal
* Empty queue handling

test_json_query_engine.py

Tests:

* Valid path lookup
* Invalid path lookup
* Default value handling

⸻

Concepts Covered

* Lists
* Tuples
* Sets
* Queue Implementation
* Dunder Methods
* Introspection
* Type Casting
* JSON Processing
* Nested Data Structures
* Unit Testing

⸻

Design Improvements

* Reusable core components
* Modular architecture
* Utility-based design
* Separation of concerns
* Unit test coverage
* Improved code readability
* Followed Python best practices