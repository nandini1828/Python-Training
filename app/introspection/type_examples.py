"""
type() Function Examples

Demonstrates using type() to get the type of objects
and understanding Python's type system.
"""

from typing import Dict, Type, List


class TypeExamples:
    """Examples of using the type() function for introspection."""

    @staticmethod
    def basic_type_checking() -> Dict[str, Type]:
        """
        Demonstrate basic type() usage.
        
        Returns:
            Dict[str, Type]: Dictionary with type results.
        """
        return {
            "string_type": type("hello"),
            "int_type": type(42),
            "float_type": type(3.14),
            "list_type": type([1, 2, 3]),
            "dict_type": type({"key": "value"}),
            "tuple_type": type((1, 2, 3)),
            "set_type": type({1, 2, 3}),
            "bool_type": type(True),
            "none_type": type(None),
        }

    @staticmethod
    def type_names() -> Dict[str, str]:
        """
        Get type names as strings.
        
        Returns:
            Dict[str, str]: Dictionary with type name strings.
        """
        return {
            "string_type": type("hello").__name__,
            "int_type": type(42).__name__,
            "float_type": type(3.14).__name__,
            "list_type": type([1, 2, 3]).__name__,
            "dict_type": type({}).__name__,
            "bool_type": type(True).__name__,
        }

    @staticmethod
    def type_comparison() -> Dict[str, bool]:
        """
        Demonstrate type comparisons.
        
        Returns:
            Dict[str, bool]: Dictionary with comparison results.
        """
        return {
            "string_equals_string": type("hello") == type("world"),
            "int_equals_int": type(42) == type(100),
            "int_equals_bool": type(42) == type(True),
            "list_equals_list": type([1, 2]) == type([3, 4]),
            "list_not_equals_tuple": type([1, 2]) != type((1, 2)),
        }

    @staticmethod
    def type_vs_isinstance() -> Dict[str, bool]:
        """
        Demonstrate differences between type() and isinstance().
        
        Returns:
            Dict[str, bool]: Dictionary showing differences.
        """
        # Note: bool is a subclass of int
        
        return {
            "type_true_is_bool": type(True) == bool,
            "type_true_is_not_int": type(True) != int,
            "isinstance_true_is_bool": isinstance(True, bool),
            "isinstance_true_is_int": isinstance(True, int),  # True!
            "type_approach_stricter": type(True) == bool,
            "isinstance_approach_flexible": isinstance(True, int),
        }

    @staticmethod
    def class_types() -> Dict[str, Type]:
        """
        Get types of class instances.
        
        Returns:
            Dict[str, Type]: Dictionary with class types.
        """
        class Person:
            pass
        
        class Student(Person):
            pass
        
        person = Person()
        student = Student()
        
        return {
            "person_type": type(person),
            "student_type": type(student),
            "person_type_name": type(person).__name__,
            "student_type_name": type(student).__name__,
        }

    @staticmethod
    def type_of_type() -> Dict[str, Type]:
        """
        Demonstrate type of types (metaclasses).
        
        Returns:
            Dict[str, Type]: Dictionary with metaclass information.
        """
        class MyClass:
            pass
        
        return {
            "type_of_int": type(42),
            "type_of_type_int": type(int),
            "type_of_myclass": type(MyClass),
            "type_of_type_myclass": type(MyClass),
            "all_types_are_type": type(int) == type(str) == type(list),
        }

    @staticmethod
    def callable_type_check() -> Dict[str, bool]:
        """
        Demonstrate callable() to check if object is callable.
        
        Returns:
            Dict[str, bool]: Dictionary with callable results.
        """
        def my_function():
            pass
        
        class MyClass:
            def method(self):
                pass
        
        obj = MyClass()
        
        return {
            "function_is_callable": callable(my_function),
            "class_is_callable": callable(MyClass),
            "instance_is_callable": callable(obj),
            "instance_method_is_callable": callable(obj.method),
            "string_not_callable": callable("hello"),
            "list_not_callable": callable([1, 2, 3]),
            "int_not_callable": callable(42),
            "lambda_is_callable": callable(lambda x: x),
        }

    @staticmethod
    def hasattr_getattr() -> Dict[str, object]:
        """
        Demonstrate hasattr() and getattr() for attribute inspection.
        
        Returns:
            Dict[str, object]: Dictionary with attribute results.
        """
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age
        
        person = Person("Alice", 30)
        
        return {
            "has_name_attr": hasattr(person, "name"),
            "has_email_attr": hasattr(person, "email"),
            "get_name": getattr(person, "name"),
            "get_with_default": getattr(person, "email", "N/A"),
            "has_method": hasattr(person, "__str__"),
        }
