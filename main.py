"""
Main entry point for the Python Training application.

This script demonstrates all training modules and their features.
"""

import sys
from app.primitive_datatypes import PrimitiveManager
from app.type_casting import SafeCast, StringCasting, NumericCasting, BooleanCasting
from app.introspection import ObjectInspector, DocInspector
from app.classes import ClassManager
from app.dunder_methods import CustomNumber, CustomString
from app.data_structure_methods.lists import ListManager
from app.data_structure_methods.tuples import TupleManager
from app.data_structure_methods.sets import SetManager
from app.data_structure_methods.dictionaries import DictionaryManager


def main():
    """Main entry point for demonstrations."""
    
    print("=" * 70)
    print("PYTHON TRAINING - COMPREHENSIVE DEMONSTRATIONS")
    print("=" * 70)
    
    # Primitive Data Types
    print("\n1. PRIMITIVE DATA TYPES")
    print("-" * 70)
    manager = PrimitiveManager()
    int_demo = manager.get_integer_demonstrations()
    print(f"Integer operations: {int_demo['basic_operations']}")
    
    # Type Casting
    print("\n2. TYPE CASTING")
    print("-" * 70)
    print(f"Safe int casting: {SafeCast.to_int('42')} (from '42')")
    print(f"Numeric casting: {NumericCasting.int_to_float()}")
    
    # Classes and Objects
    print("\n3. OBJECT-ORIENTED PROGRAMMING")
    print("-" * 70)
    class_mgr = ClassManager()
    demo_data = class_mgr.get_demo_data()
    print(f"Total students: {len(demo_data['students'])}")
    print(f"Total employees: {len(demo_data['employees'])}")
    
    # Dunder Methods
    print("\n4. OPERATOR OVERLOADING (DUNDER METHODS)")
    print("-" * 70)
    num1 = CustomNumber(10)
    num2 = CustomNumber(5)
    print(f"CustomNumber(10) + CustomNumber(5) = {(num1 + num2).value}")
    
    str1 = CustomString("Hello")
    str2 = CustomString(" World")
    print(f"CustomString('Hello') + CustomString(' World') = '{(str1 + str2).value}'")
    
    # Data Structures
    print("\n5. DATA STRUCTURE OPERATIONS")
    print("-" * 70)
    list_ops = ListManager.basic_operations()
    print(f"List operations: {list_ops['length']} elements")
    
    set_ops = SetManager.set_operations()
    print(f"Set union: {set_ops['union']}")
    
    dict_ops = DictionaryManager.basic_operations()
    print(f"Dictionary operations: {dict_ops['length']} keys")
    
    # Introspection
    print("\n6. INTROSPECTION & REFLECTION")
    print("-" * 70)
    obj_info = ObjectInspector.inspect_object([1, 2, 3])
    print(f"Object type: {obj_info['type']}")
    print(f"Object ID: {obj_info['id']}")
    
    print("\n" + "=" * 70)
    print("TRAINING MODULES OVERVIEW")
    print("=" * 70)
    print("""
    This comprehensive Python training includes:
    
    1. Primitive Data Types:
       - Integers, Floats, Strings, Booleans
       - Operations, methods, and best practices
    
    2. Type Casting:
       - Safe casting with error handling
       - Numeric, string, and boolean conversions
    
    3. Introspection:
       - Object inspection (dir, isinstance, type)
       - Documentation access and analysis
    
    4. Object-Oriented Programming:
       - Classes, inheritance, and composition
       - Instance and class methods
    
    5. Dunder Methods:
       - Operator overloading
       - Custom string and number implementations
    
    6. Data Structures:
       - Lists, tuples, sets, dictionaries
       - Comprehensive methods and operations
    
    Run tests with: pytest tests/
    """)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
