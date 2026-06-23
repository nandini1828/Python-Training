"""
Set Manager

Management of set operations.
"""

from typing import Set, Dict, Any


class SetManager:
    """Manager for set operations."""
    
    @staticmethod
    def basic_operations() -> Dict[str, Any]:
        """Demonstrate basic set operations."""
        s = {1, 2, 3, 4, 5}
        
        return {
            "set": s,
            "length": len(s),
            "membership": 3 in s,
            "not_membership": 6 not in s,
            "add": (lambda s: s.add(6) or s)(s.copy()),
            "remove": (lambda s: s.discard(3) or s)(s.copy()),
            "copy": s.copy(),
        }
    
    @staticmethod
    def set_methods() -> Dict[str, Any]:
        """Demonstrate set methods."""
        s = {1, 2, 3, 4, 5}
        s_copy = s.copy()
        
        return {
            "add": (lambda: s_copy.add(6) or s_copy)(),
            "discard": (lambda: s_copy.discard(1) or s_copy)(),
            "remove": (lambda: (s.copy(), s.copy().remove(1))[0] if 1 in s else None),
            "pop": (lambda: s_copy.pop() or s_copy)() if s_copy else None,
            "clear_result": "set()" if (lambda: s.copy().clear() or True)() else None,
        }
    
    @staticmethod
    def set_operations() -> Dict[str, Any]:
        """Demonstrate set operations (union, intersection, etc)."""
        s1 = {1, 2, 3, 4}
        s2 = {3, 4, 5, 6}
        
        return {
            "union": s1 | s2,
            "union_method": s1.union(s2),
            "intersection": s1 & s2,
            "intersection_method": s1.intersection(s2),
            "difference": s1 - s2,
            "difference_method": s1.difference(s2),
            "symmetric_difference": s1 ^ s2,
            "symmetric_difference_method": s1.symmetric_difference(s2),
        }
    
    @staticmethod
    def set_comparisons() -> Dict[str, bool]:
        """Demonstrate set comparisons."""
        s1 = {1, 2, 3}
        s2 = {1, 2, 3, 4}
        s3 = {1, 2, 3}
        
        return {
            "equal": s1 == s3,
            "not_equal": s1 != s2,
            "subset": s1 <= s2,
            "proper_subset": s1 < s2,
            "superset": s2 >= s1,
            "proper_superset": s2 > s1,
            "disjoint": s1.isdisjoint({5, 6}),
        }
    
    @staticmethod
    def set_from_list() -> Dict[str, Any]:
        """Demonstrate creating sets from lists."""
        lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        
        return {
            "original_list": lst,
            "unique_elements": set(lst),
            "list_length": len(lst),
            "set_length": len(set(lst)),
            "duplicates_removed": True,
        }
    
    @staticmethod
    def frozenset_operations() -> Dict[str, Any]:
        """Demonstrate frozenset (immutable set)."""
        fs1 = frozenset({1, 2, 3})
        fs2 = frozenset({2, 3, 4})
        
        return {
            "frozenset": fs1,
            "union": fs1 | fs2,
            "intersection": fs1 & fs2,
            "as_dict_key": {fs1: "value"},
            "immutable": "Cannot add/remove elements",
        }
