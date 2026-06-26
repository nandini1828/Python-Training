# Python Training Project

A comprehensive Python training program covering fundamental concepts and intermediate programming techniques with full industrial-grade code examples.

## Overview

This project provides structured learning materials for Python developers at all levels, featuring:

- **Primitive Data Types**: Comprehensive coverage of int, float, str, bool types
- **Type Casting**: Safe conversion between types with error handling
- **Introspection**: Object inspection, type checking, and documentation
- **Object-Oriented Programming**: Classes, inheritance, and composition patterns
- **Dunder Methods**: Operator overloading and special methods
- **Data Structures**: Lists, tuples, sets, and dictionaries with all operations

## Project Structure

```
Python-Training/
├── app/
│   ├── primitive_datatypes/     # Int, Float, String, Boolean modules
│   ├── type_casting/            # Safe and unsafe casting examples
│   ├── introspection/           # Reflection and object inspection
│   ├── classes/                 # OOP with Student, Employee examples
│   ├── dunder_methods/          # Operator overloading examples
│   └── data_structure_methods/  # Lists, Tuples, Sets, Dicts
├── tests/                       # Comprehensive test suites
├── main.py                      # Entry point with demonstrations
├── requirements.txt             # Python dependencies
├── pytest.ini                   # Pytest configuration
└── README.md                    # This file
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Python-Training.git
cd Python-Training
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Run the Main Demonstration

```bash
python main.py
```

This will display demonstrations of all modules and their features.

### Run All Tests

```bash
pytest
```

Run tests with coverage report:
```bash
pytest --cov=app --cov-report=html
```

### Run Specific Test Module

```bash
pytest tests/primitive_datatypes/
pytest tests/type_casting/
pytest tests/classes/
```

### Run Tests by Category

```bash
pytest -m primitives          # Primitive data types tests
pytest -m type_casting        # Type casting tests
pytest -m introspection       # Introspection tests
pytest -m classes             # Class tests
pytest -m dunder              # Dunder method tests
pytest -m data_structures     # Data structure tests
```

## Module Documentation

### 1. Primitive Data Types (`app/primitive_datatypes/`)

Learn about Python's fundamental data types:

- **IntegerDemo**: Arithmetic, bitwise operations, representations
- **FloatDemo**: Floating-point operations, precision, special values
- **StringDemo**: Manipulation, formatting, regex operations
- **BooleanDemo**: Logical operations, truthiness, filtering
- **PrimitiveManager**: Unified interface for all primitive types

### 2. Type Casting (`app/type_casting/`)

Safe type conversions with error handling:

- **SafeCast**: Safe conversion with defaults and validation
- **NumericCasting**: Integer, float, complex number conversions
- **StringCasting**: String parsing and formatting
- **BooleanCasting**: Truthiness and boolean conversions

### 3. Introspection (`app/introspection/`)

Explore Python's runtime capabilities:

- **DirectoryExamples**: Using `dir()` for object inspection
- **TypeExamples**: Type checking with `type()` and `callable()`
- **InstanceOfExamples**: Inheritance checking with `isinstance()`
- **ObjectInspector**: Advanced object analysis
- **DocInspector**: Documentation and signature inspection

### 4. Object-Oriented Programming (`app/classes/`)

Build robust OOP systems:

- **Student**: Basic class with attributes and methods
- **Employee**: Class with validation and computed properties
- **Department**: Managing collections of objects
- **Company/Address/Office**: Composition pattern demonstration
- **ClassManager**: Factory and orchestration pattern

### 5. Dunder Methods (`app/dunder_methods/`)

Operator overloading and special behavior:

- **CustomNumber**: Arithmetic operator overloading (+, -, *, /)
- **CustomString**: String-like operations and indexing
- **ArithmeticExamples**: Comprehensive arithmetic demonstrations
- **ComparisonExamples**: Comparison operator usage

### 6. Data Structures (`app/data_structure_methods/`)

Master Python's built-in collections:

- **Lists**: Append, extend, sort, comprehensions
- **Tuples**: Immutability, unpacking, named tuples
- **Sets**: Union, intersection, difference operations
- **Dictionaries**: Merging, nesting, iteration patterns

## Key Features

### Industrial-Grade Code Quality

- **Comprehensive Docstrings**: Every function documented with purpose and examples
- **Type Hints**: Full typing annotations for better IDE support
- **Error Handling**: Proper exception handling and validation
- **Best Practices**: Following PEP 8 and Python conventions

### Extensive Examples

- **Theory + Practice**: Concept explanation with runnable examples
- **Real-World Scenarios**: Practical use cases for each concept
- **Performance Considerations**: Notes on efficiency and trade-offs

### Complete Test Coverage

- **Unit Tests**: Testing individual functions and methods
- **Integration Tests**: Testing module interactions
- **Edge Cases**: Handling boundary conditions
- **Coverage Reporting**: Automated test coverage analysis

## Code Examples

### Working with Primitive Types

```python
from app.primitive_datatypes import IntegerDemo, StringDemo

# Integer operations
int_demo = IntegerDemo()
operations = int_demo.basic_operations()
print(f"10 + 3 = {operations['addition']}")

# String manipulation
string_demo = StringDemo()
concat = string_demo.string_concatenation()
print(concat['f_string'])
```

### Safe Type Casting

```python
from app.type_casting import SafeCast

# Safe conversions with defaults
value = SafeCast.to_int("42", default=0)
age = SafeCast.to_int("invalid", default=18)
```

### Class Usage

```python
from app.classes import Student, Employee, Department

# Create domain objects
student = Student("S001", "Alice", "Computer Science", 3.8)
student.enroll_course("Python")

# Create employees and department
emp1 = Employee("E001", "Bob", "Developer", 100000)
dept = Department("Engineering", "E001")
dept.add_employee(emp1)
```

### Operator Overloading

```python
from app.dunder_methods import CustomNumber, CustomString

# Custom arithmetic
num1 = CustomNumber(10)
num2 = CustomNumber(5)
result = num1 + num2  # Uses __add__

# Custom string operations
str1 = CustomString("Hello")
str2 = CustomString(" World")
message = str1 + str2
```

## Learning Path

1. **Start**: `app/primitive_datatypes/` - Understand basic types
2. **Next**: `app/type_casting/` - Learn conversions
3. **Progress**: `app/introspection/` - Explore objects
4. **Intermediate**: `app/classes/` - OOP fundamentals
5. **Advanced**: `app/dunder_methods/` - Operator overloading
6. **Master**: `app/data_structure_methods/` - Data manipulation

## Testing Strategy

Run tests in this order to verify all functionality:

```bash
# Test primitives
pytest tests/primitive_datatypes/ -v

# Test type casting
pytest tests/type_casting/ -v

# Test introspection
pytest tests/introspection/ -v

# Test OOP
pytest tests/classes/ -v

# Test dunder methods
pytest tests/dunder_methods/ -v

# Test data structures
pytest tests/data_structure_methods/ -v

# All tests with coverage
pytest --cov=app --cov-report=term-missing
```

## Performance Tips

- **Lists vs Tuples**: Use tuples for immutable sequences
- **Sets for Membership**: Check `x in set()` is O(1) vs O(n) for lists
- **Dict vs Lists**: Use dicts for key-value lookups
- **Generators**: Use for memory-efficient iteration
- **List Comprehensions**: Faster than loops for list creation

## Common Pitfalls to Avoid

1. **Floating Point Precision**: Always use `math.isclose()` for float comparisons
2. **Mutable Default Arguments**: Don't use `[]` or `{}` as defaults
3. **String Immutability**: Remember strings are immutable in Python
4. **List Aliasing**: Understand copy vs reference behavior
5. **None vs False**: They're different; always check with `is None`

## Contributing

To improve this training material:

1. Fork the repository
2. Create a feature branch
3. Add or improve modules
4. Ensure all tests pass
5. Submit a pull request

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Real Python Tutorials](https://realpython.com/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

## FAQ

**Q: What Python version is required?**
A: Python 3.8+ for full compatibility with all features.

**Q: Can I use this for commercial projects?**
A: Yes, it's MIT licensed for any use.

**Q: How comprehensive are the tests?**
A: Over 50+ test cases covering all major functionality.

**Q: Is this suitable for beginners?**
A: Yes! Start with primitive_datatypes and progress through the modules.

## Support

For questions or issues:
- Open an issue on GitHub
- Check the README for common pitfalls
- Review existing tests for usage examples

---

**Last Updated**: June 2024
**Version**: 1.0.0
**Python**: 3.8+