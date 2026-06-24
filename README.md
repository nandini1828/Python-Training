Python Data Types Mastery Project

Overview

This project was developed to explore and implement core Python concepts, including:

* Data Types
* Type Casting
* Introspection
* Dunder Methods
* Collections
* Object-Oriented Programming
* Type Hints
* Argparse
* Pytest
* Nested JSON Querying
* Runtime Object Inspection

The project is organized into modular packages following separation of concerns and reusable design principles.

⸻

Project Structure

python_datatypes_mastery/
│
├── main.py
│
├── primitives/
├── collection_utils/
├── classes/
├── inspectors/
├── exercises/
├── tests/
│
└── README.md

⸻

Folder Details

1. primitives/

Contains Python fundamental concepts and language features.

Files

introspection.py

Implements runtime object inspection using:

* type()
* dir()
* id()

Purpose:

* Inspect objects during execution
* Understand object metadata

⸻

casting.py

Implements type conversion utilities.

Examples:

* String → Integer
* String → Float
* Float → Integer

Includes:

* Safe type conversion
* Error handling

⸻

dunder_examples.py

Demonstrates Python magic methods.

Examples:

* add()
* eq()
* contains()
* len()

Purpose:

Understand how Python operators work internally.

⸻

type_annotations.py

Demonstrates Type Hints.

Examples:

def add(a: int, b: int) -> int:

Purpose:

* Improve readability
* Improve IDE support
* Enable static analysis

⸻

callable_examples.py

Demonstrates usage of:

callable()

Purpose:

* Determine whether an object can be invoked
* Understand how callable methods are identified

⸻

2. collection_utils/

Contains reusable operations for Python collections.

Files

list_utils.py

Operations related to lists.

Examples:

* append()
* insert()
* remove()
* pop()
* sort()

⸻

tuple_utils.py

Tuple-related functionality.

Examples:

* count()
* index()

Purpose:

Understand immutable collections.

⸻

set_utils.py

Set operations.

Examples:

* union
* intersection
* difference
* symmetric difference

Purpose:

Handle unique data efficiently.

⸻

dict_utils.py

Dictionary operations.

Examples:

* get()
* setdefault()
* keys()
* values()
* items()
* update()

Purpose:

Efficient key-value data manipulation.

⸻

3. classes/

Contains Object-Oriented Programming examples and implementations.

Files

student.py

Represents a Student object.

Concepts:

* Classes
* Objects
* Constructors
* Instance Variables
* Methods

⸻

computer.py

Demonstrates Composition.

Example:

Computer
    HAS-A
CPU

Purpose:

Understand object composition.

⸻

object_deconstructor.py

Recursively converts objects into dictionaries.

Uses:

__dict__

Purpose:

Understand how Python objects store state internally.

⸻

4. inspectors/

Contains runtime inspection utilities.

Files

object_inspector.py

Accepts any Python object and returns:

* Object Type
* Object ID
* Public Methods
* Method Documentation

Uses:

* dir()
* getattr()
* callable()
* doc
* type()
* id()

Example:

inspect_object(student)

Purpose:

Demonstrate advanced introspection techniques.

⸻

5. exercises/

Contains implementations of assignment exercises.

Files

queue.py

Implements a custom Queue.

Operations:

* enqueue()
* dequeue()
* size()

Concept:

FIFO (First In First Out)

⸻

tag_merger.py

Merges tags using Sets.

Features:

* Remove duplicates
* Find common tags
* Find unique tags

⸻

word_counter.py

Counts word occurrences in text.

Features:

* Case-insensitive counting
* Frequency analysis

⸻

nested_json_query_engine.py

Implements a Nested JSON Query Engine.

Example:

engine.query(
    data,
    "user.profile.name"
)

Features:

* Dot-separated path traversal
* Safe lookup
* Default values
* Nested dictionary navigation

Purpose:

Understand JSON traversal and API-style data structures.

⸻

6. tests/

Contains automated test cases using pytest.

Files

test_casting.py

Tests:

* Safe casting
* Type conversions

⸻

test_queue.py

Tests:

* Queue insertion
* Queue removal
* Empty queue handling

⸻

test_json_query.py

Tests:

* Valid path lookup
* Invalid path lookup
* Default value handling

⸻

test_word_counter.py

Tests:

* Word frequency calculations

⸻

test_deconstructor.py

Tests:

* Object to dictionary conversion

⸻

Additional Concepts Implemented

Argparse

Implemented command-line argument parsing.

Purpose:

Allow users to execute project functionality through terminal arguments.

Example:

python main.py --module queue

Concepts:

* Command-line interfaces
* User input handling
* Program configuration

⸻

Type Hints

Implemented throughout the project.

Examples:

def query(
    data: dict,
    path: str
) -> Any:

Benefits:

* Better readability
* Improved maintainability
* IDE support
* Static analysis

⸻

Pytest

Implemented automated testing.

Examples:

assert result == expected

Benefits:

* Automated validation
* Regression prevention
* Easier debugging

⸻

Key Python Concepts Covered

Python Fundamentals

* Data Types
* Type Casting
* Truthy and Falsy Values
* Type Hints

Introspection

* type()
* dir()
* id()
* getattr()
* callable()
* doc

Collections

* List
* Tuple
* Set
* Dictionary

OOP

* Classes
* Objects
* Constructors
* Composition

Advanced Concepts

* Dunder Methods
* Nested JSON Querying
* Object Deconstruction
* Runtime Inspection

Testing

* Pytest
* Assertions
* Automated Validation

⸻

Design Principles Followed

* Separation of Concerns
* Modular Design
* Reusable Components
* Single Responsibility Principle
* Readable Naming Conventions
* Test-Driven Validation

⸻

Outcome

This project demonstrates a strong understanding of Python fundamentals, object-oriented programming, collection handling, introspection, testing practices, command-line interfaces, and nested data processing while maintaining a clean and scalable project structure.