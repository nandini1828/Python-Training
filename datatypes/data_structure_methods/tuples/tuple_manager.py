"""
Tuple Manager

Management of tuple operations.
"""

from typing import Tuple, Dict, Any, List


class TupleManager:
    """Manager for tuple operations."""
    
    @staticmethod
    def basic_operations() -> Dict[str, Any]:
        """Demonstrate basic tuple operations."""
        tpl = (1, 2, 3, 4, 5)
        
        return {
            "original_tuple": tpl,
            "length": len(tpl),
            "first_element": tpl[0],
            "last_element": tpl[-1],
            "slice": tpl[1:4],
            "reversed": tpl[::-1],
            "indexing": tpl[2],
        }
    
    @staticmethod
    def tuple_methods() -> Dict[str, Any]:
        """Demonstrate tuple methods."""
        tpl = (1, 2, 3, 2, 1)
        
        return {
            "count": tpl.count(2),
            "index": tpl.index(2),
            "length": len(tpl),
        }
    
    @staticmethod
    def immutability() -> Dict[str, Any]:
        """Demonstrate tuple immutability."""
        tpl = (1, 2, 3)
        
        return {
            "original": tpl,
            "cannot_modify": "TypeError: 'tuple' object does not support item assignment",
            "concatenation": tpl + (4, 5),
            "repetition": tpl * 2,
            "original_unchanged": tpl,
        }
    
    @staticmethod
    def tuple_packing_unpacking() -> Dict[str, Any]:
        """Demonstrate tuple packing and unpacking."""
        # Packing
        packed = 1, 2, 3  # Implicit tuple creation
        
        # Unpacking
        a, b, c = (4, 5, 6)
        
        # Extended unpacking
        first, *middle, last = (1, 2, 3, 4, 5)
        
        return {
            "packed": packed,
            "unpacked": f"a={a}, b={b}, c={c}",
            "extended": f"first={first}, middle={middle}, last={last}",
        }
    
    @staticmethod
    def tuple_as_keys() -> Dict[str, Any]:
        """Demonstrate using tuples as dict keys."""
        coordinates = {
            (0, 0): "origin",
            (1, 0): "x-axis",
            (0, 1): "y-axis",
            (1, 1): "first quadrant",
        }
        
        return {
            "dictionary": coordinates,
            "lookup": coordinates[(1, 0)],
            "all_coordinates": list(coordinates.keys()),
        }
    
    @staticmethod
    def named_tuples() -> Dict[str, Any]:
        """Demonstrate named tuples."""
        from collections import namedtuple
        
        Point = namedtuple("Point", ["x", "y"])
        person = namedtuple("Person", ["name", "age"])
        
        p = Point(3, 4)
        person_obj = person("Alice", 30)
        
        return {
            "point": p,
            "point_x": p.x,
            "point_y": p.y,
            "person": person_obj,
            "person_name": person_obj.name,
            "as_dict": person_obj._asdict(),
        }
    
    @staticmethod
    def tuple_operations() -> Dict[str, Any]:
        """Demonstrate tuple operations."""
        tpl1 = (1, 2, 3)
        tpl2 = (4, 5, 6)
        
        return {
            "concatenation": tpl1 + tpl2,
            "repetition": (1, 2) * 3,
            "membership": 2 in tpl1,
            "not_membership": 7 not in tpl1,
            "unpacking": list(tpl1),
        }
