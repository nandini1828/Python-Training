"""
Comparison Examples

Demonstrates comparison dunder methods.
"""

from typing import Dict, Tuple


class ComparisonExamples:
    """Examples of comparison dunder methods."""
    
    @staticmethod
    def comparison_operators() -> Dict[str, bool]:
        """
        Demonstrate basic comparison operators.
        
        Returns:
            Dict[str, bool]: Comparison results.
        """
        a, b = 10, 20
        
        return {
            "less_than": a < b,
            "greater_than": a > b,
            "less_equal": a <= b,
            "greater_equal": a >= b,
            "equal": a == b,
            "not_equal": a != b,
        }
    
    @staticmethod
    def string_comparison() -> Dict[str, bool]:
        """
        Demonstrate string comparison.
        
        Returns:
            Dict[str, bool]: String comparison results.
        """
        str1, str2 = "apple", "banana"
        
        return {
            "apple_less_than_banana": str1 < str2,
            "banana_greater_than_apple": str2 > str1,
            "same_strings_equal": "hello" == "hello",
            "different_strings_not_equal": str1 != str2,
            "lexicographic_ordering": ["zebra", "apple", "banana"].sort() or True,
        }
    
    @staticmethod
    def list_comparison() -> Dict[str, bool]:
        """
        Demonstrate list comparison.
        
        Returns:
            Dict[str, bool]: List comparison results.
        """
        list1 = [1, 2, 3]
        list2 = [1, 2, 4]
        list3 = [1, 2, 3]
        
        return {
            "equal_lists": list1 == list3,
            "different_lists": list1 != list2,
            "compare_by_length": len(list1) < len(list2),
            "first_element_comparison": list1[0] < list2[0],
        }
    
    @staticmethod
    def tuple_comparison() -> Dict[str, bool]:
        """
        Demonstrate tuple comparison.
        
        Returns:
            Dict[str, bool]: Tuple comparison results.
        """
        tuple1 = (1, 2, 3)
        tuple2 = (1, 2, 4)
        
        return {
            "tuples_equal": (1, 2, 3) == (1, 2, 3),
            "first_diff_at_position": tuple1 < tuple2,
            "empty_tuple_less": () < (1,),
        }
    
    @staticmethod
    def custom_class_comparison() -> Dict[str, object]:
        """
        Demonstrate comparison with custom classes.
        
        Returns:
            Dict[str, object]: Custom comparison examples.
        """
        class Person:
            def __init__(self, name: str, age: int):
                self.name = name
                self.age = age
            
            def __lt__(self, other):
                return self.age < other.age
            
            def __eq__(self, other):
                return self.name == other.name and self.age == other.age
        
        person1 = Person("Alice", 30)
        person2 = Person("Bob", 25)
        person3 = Person("Alice", 30)
        
        return {
            "person1_older_than_person2": not (person1 < person2),
            "person1_equals_person3": person1 == person3,
            "person1_not_equals_person2": person1 != person2,
            "sorting_by_age": [person1.age, person2.age],
        }
    
    @staticmethod
    def comparison_chaining() -> Dict[str, bool]:
        """
        Demonstrate comparison chaining.
        
        Returns:
            Dict[str, bool]: Chaining results.
        """
        a, b, c = 10, 20, 30
        
        return {
            "chain_less_than": a < b < c,
            "chain_with_equality": a < b <= c,
            "chain_false": a < c < b,
            "multiple_chains": 10 < 20 < 30 < 40,
        }
    
    @staticmethod
    def three_way_comparison() -> Dict[str, int]:
        """
        Demonstrate three-way comparison (returns -1, 0, 1).
        
        Returns:
            Dict[str, int]: Three-way comparison results.
        """
        def compare(a, b) -> int:
            if a < b:
                return -1
            elif a > b:
                return 1
            else:
                return 0
        
        return {
            "5_vs_10": compare(5, 10),
            "10_vs_10": compare(10, 10),
            "15_vs_10": compare(15, 10),
        }
