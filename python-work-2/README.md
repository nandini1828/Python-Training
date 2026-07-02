# Python Control Flow & Iteration

A well-structured Python project demonstrating the fundamentals of **Control Flow**, **Loops**, **Iteration Helpers**, **Data Structures**, **Comprehensions**, and **Iterators & Generators**.

The project is organized into modular packages, with each concept implemented in its own file for better readability, maintainability, and scalability.

---

## Project Structure

```text
python-control-flow/
│
├── main.py
├── README.md
├── requirements.txt
│
├── control_flow/
│   ├── if_else.py
│   ├── truthy_falsy.py
│   ├── logical_operators.py
│   ├── short_circuit.py
│   ├── ternary.py
│   └── match_case.py
│
├── loops/
│   ├── for_loop.py
│   ├── while_loop.py
│   ├── break_continue_pass.py
│   └── loop_else.py
│
├── iteration_helpers/
│   ├── range_examples.py
│   ├── enumerate_examples.py
│   ├── zip_examples.py
│   ├── reversed_sorted.py
│   └── any_all.py
│
├── data_structures/
│   ├── lists.py
│   ├── list_modification.py
│   ├── dictionaries.py
│   ├── dictionary_safety.py
│   └── sets.py
│
├── comprehensions/
│   ├── list_comprehension.py
│   ├── dictionary_comprehension.py
│   ├── set_comprehension.py
│   └── nested_comprehension.py
│
├── iterators_generators/
│   ├── iterator_protocol.py
│   ├── generators.py
│   └── generator_expression.py
│
└── utils/
    └── printer.py
```

---

# Topics Covered

## Part 1: Conditional Control Flow & Decision Making

* if-elif-else
* Truthy and Falsy values
* Logical Operators (`and`, `or`, `not`)
* Short-Circuit Evaluation
* Ternary Operator
* `match-case` (Python 3.10+)

---

## Part 2: Loop Foundations & Basic Iteration

* `for` Loop
* `while` Loop
* `break`
* `continue`
* `pass`
* `for-else`
* `while-else`

---

## Part 3: Python's Iteration Helpers

* `range()`
* `enumerate()`
* `zip()`
* `zip_longest()`
* `reversed()`
* `sorted()`
* `any()`
* `all()`

---

## Part 4: Data Structure Iteration & Safety

### Lists

* Indexing
* Slicing
* Iteration

### List Modification Trap

* Incorrect way of modifying a list while iterating
* Safe approaches using copy and list comprehension

### Dictionaries

* `.keys()`
* `.values()`
* `.items()`

### Dictionary Safety

* `.get()`
* `collections.defaultdict`

### Sets

* Iteration
* Fast membership testing

---

## Part 5: Comprehensions

* List Comprehensions
* Dictionary Comprehensions
* Set Comprehensions
* Nested Comprehensions

---

## Part 6: Iterators & Generators

* Iterator Protocol
* `iter()`
* `next()`
* `yield`
* Generators
* Generator Expressions

---

# Features

* Modular project structure
* Well-documented source code
* Reusable demo functions
* Easy to extend with new Python concepts
* Beginner-friendly examples
* Production-style package organization

---

# Requirements

* Python 3.10 or later

---

# Run the Project

Clone the repository and run:

```bash
python main.py
```

---

# Learning Outcomes

After completing this project, you will understand:

* Conditional statements
* Looping techniques
* Iteration helpers
* Safe iteration over Python data structures
* Python comprehensions
* The Iterator Protocol
* Lazy evaluation using generators
* Writing clean, modular Python code

---

# Future Enhancements

Additional Python topics that can be added later:

* Functions
* Exception Handling
* Object-Oriented Programming (OOP)
* File Handling
* Modules & Packages
* Decorators
* Context Managers
* Itertools
* Functional Programming
* Multithreading & Multiprocessing
* Async Programming
* Type Hinting
* Unit Testing
