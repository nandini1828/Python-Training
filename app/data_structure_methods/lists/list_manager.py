"""
List Manager

Comprehensive management of list operations.
"""

from typing import List, Dict, Any, Callable


class ListManager:
    """Manager for list operations and demonstrations."""
    
    @staticmethod
    def basic_operations() -> Dict[str, Any]:
        """Demonstrate basic list operations."""
        lst = [1, 2, 3, 4, 5]
        
        return {
            "original_list": lst,
            "length": len(lst),
            "first_element": lst[0],
            "last_element": lst[-1],
            "slice_middle": lst[1:4],
            "every_second": lst[::2],
            "reversed": lst[::-1],
        }
    
    @staticmethod
    def list_methods() -> Dict[str, Any]:
        """Demonstrate list methods."""
        lst = [1, 2, 3, 2, 1]
        
        return {
            "append": (lst.copy(), lst.copy() + [6])[1] or True,
            "extend": (lambda l: l.extend([4, 5]) or l)(lst.copy()),
            "insert": (lambda l: l.insert(0, 0) or l)(lst.copy()),
            "remove": (lambda l: l.remove(2) or l)(lst.copy()),
            "pop": (lambda l: l.pop() or l)(lst.copy()),
            "pop_index": (lambda l: l.pop(0) or l)(lst.copy()),
            "count": lst.count(2),
            "index": lst.index(2),
            "copy": lst.copy(),
        }
    
    @staticmethod
    def sorting_operations() -> Dict[str, List]:
        """Demonstrate sorting operations."""
        lst = [3, 1, 4, 1, 5, 9, 2, 6]
        
        return {
            "original": lst,
            "sorted_ascending": sorted(lst),
            "sorted_descending": sorted(lst, reverse=True),
            "sort_in_place": (lambda l: l.sort() or l)(lst.copy()),
            "sorted_by_magnitude": sorted([-3, 1, -2, 4], key=abs),
        }
    
    @staticmethod
    def list_comprehension() -> Dict[str, List]:
        """Demonstrate list comprehensions."""
        return {
            "squares": [x**2 for x in range(5)],
            "evens": [x for x in range(10) if x % 2 == 0],
            "nested_pairs": [(x, y) for x in range(3) for y in range(3)],
            "uppercase": [s.upper() for s in ["apple", "banana", "cherry"]],
            "filtered_squares": [x**2 for x in range(10) if x % 2 == 0],
        }
    
    @staticmethod
    def list_unpacking() -> Dict[str, Any]:
        """Demonstrate list unpacking."""
        a, b, c = [1, 2, 3]
        first, *middle, last = [1, 2, 3, 4, 5]
        
        return {
            "simple_unpack": f"a={a}, b={b}, c={c}",
            "with_star": f"first={first}, middle={middle}, last={last}",
            "ignore_middle": (lambda f, *_, l: (f, l))(*[1, 2, 3, 4, 5]),
        }
    
    @staticmethod
    def list_operations() -> Dict[str, Any]:
        """Demonstrate list operations."""
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        
        return {
            "concatenation": list1 + list2,
            "repetition": [1, 2] * 3,
            "membership": 2 in list1,
            "not_membership": 7 not in list1,
            "clear": (lambda l: l.clear() or l)(list1.copy()),
            "reverse": (lambda l: l.reverse() or l)(list1.copy()),
        }
    
    @staticmethod
    def advanced_operations() -> Dict[str, Any]:
        """Demonstrate advanced list operations."""
        numbers = [1, 2, 3, 4, 5]
        
        return {
            "map": list(map(lambda x: x**2, numbers)),
            "filter": list(filter(lambda x: x > 2, numbers)),
            "any": any([False, False, True, False]),
            "all": all([True, True, True, True]),
            "sum": sum(numbers),
            "max": max(numbers),
            "min": min(numbers),
            "zip": list(zip([1, 2, 3], ["a", "b", "c"])),
        }
