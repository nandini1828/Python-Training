"""
isinstance() and issubclass() Examples

Demonstrates checking object types and class inheritance relationships.
"""

from typing import List, Dict, Union


class InstanceOfExamples:
    """Examples of using isinstance() and issubclass() functions."""

    @staticmethod
    def basic_isinstance() -> Dict[str, bool]:
        """
        Demonstrate basic isinstance() checks.
        
        Returns:
            Dict[str, bool]: Dictionary with isinstance results.
        """
        return {
            "string_is_str": isinstance("hello", str),
            "number_is_int": isinstance(42, int),
            "number_is_float": isinstance(3.14, float),
            "list_is_list": isinstance([1, 2, 3], list),
            "dict_is_dict": isinstance({"key": "value"}, dict),
            "true_is_bool": isinstance(True, bool),
            "true_is_int": isinstance(True, int),  # bool is subclass of int!
        }

    @staticmethod
    def isinstance_with_tuple() -> Dict[str, bool]:
        """
        Demonstrate isinstance() with multiple types.
        
        Returns:
            Dict[str, bool]: Dictionary with results.
        """
        value = "hello"
        
        return {
            "str_matches_tuple": isinstance(value, (str, int, float)),
            "str_in_tuple": isinstance(value, (int, float, complex)),
            "check_numeric": isinstance(42, (int, float, complex)),
        }

    @staticmethod
    def isinstance_inheritance() -> Dict[str, bool]:
        """
        Demonstrate isinstance() with class inheritance.
        
        Returns:
            Dict[str, bool]: Dictionary with inheritance checks.
        """
        class Animal:
            pass
        
        class Dog(Animal):
            pass
        
        class Cat(Animal):
            pass
        
        dog = Dog()
        cat = Cat()
        
        return {
            "dog_is_dog": isinstance(dog, Dog),
            "dog_is_animal": isinstance(dog, Animal),
            "cat_is_cat": isinstance(cat, Cat),
            "cat_is_animal": isinstance(cat, Animal),
            "dog_is_cat": isinstance(dog, Cat),
        }

    @staticmethod
    def builtin_type_hierarchy() -> Dict[str, bool]:
        """
        Demonstrate built-in type hierarchy with isinstance().
        
        Returns:
            Dict[str, bool]: Dictionary with hierarchy results.
        """
        return {
            "bool_is_int": isinstance(True, int),
            "int_is_int": isinstance(42, int),
            "int_is_not_bool": not isinstance(42, bool),
            "list_is_sequence": isinstance([1, 2], (list, tuple)),
            "tuple_is_sequence": isinstance((1, 2), (list, tuple)),
        }

    @staticmethod
    def issubclass_examples() -> Dict[str, bool]:
        """
        Demonstrate issubclass() function.
        
        Returns:
            Dict[str, bool]: Dictionary with issubclass results.
        """
        class Vehicle:
            pass
        
        class Car(Vehicle):
            pass
        
        class Truck(Vehicle):
            pass
        
        return {
            "car_is_subclass_of_vehicle": issubclass(Car, Vehicle),
            "truck_is_subclass_of_vehicle": issubclass(Truck, Vehicle),
            "car_is_subclass_of_car": issubclass(Car, Car),
            "car_is_not_subclass_of_truck": not issubclass(Car, Truck),
            "bool_is_subclass_of_int": issubclass(bool, int),
        }

    @staticmethod
    def checking_abstract_base_classes() -> Dict[str, bool]:
        """
        Demonstrate isinstance() with collections abstract base classes.
        
        Returns:
            Dict[str, bool]: Dictionary with ABC results.
        """
        from collections.abc import Sequence, Mapping, Iterable
        
        return {
            "list_is_sequence": isinstance([1, 2, 3], Sequence),
            "tuple_is_sequence": isinstance((1, 2, 3), Sequence),
            "string_is_sequence": isinstance("hello", Sequence),
            "dict_is_mapping": isinstance({"a": 1}, Mapping),
            "list_is_iterable": isinstance([1, 2], Iterable),
            "string_is_iterable": isinstance("abc", Iterable),
        }

    @staticmethod
    def type_checking_patterns() -> Dict[str, Union[str, bool]]:
        """
        Demonstrate common type checking patterns.
        
        Returns:
            Dict[str, Union[str, bool]]: Dictionary with pattern examples.
        """
        def process_data(data):
            if isinstance(data, str):
                return f"Processing string: {data}"
            elif isinstance(data, (int, float)):
                return f"Processing number: {data}"
            elif isinstance(data, (list, tuple)):
                return f"Processing sequence of {len(data)} items"
            else:
                return "Unknown type"
        
        return {
            "process_string": process_data("hello"),
            "process_int": process_data(42),
            "process_list": process_data([1, 2, 3]),
            "process_dict": process_data({"key": "value"}),
        }
