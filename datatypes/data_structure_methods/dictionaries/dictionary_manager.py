"""
Dictionary Manager

Management of dictionary operations.
"""

from typing import Dict, Any


class DictionaryManager:
    """Manager for dictionary operations."""
    
    @staticmethod
    def basic_operations() -> Dict[str, Any]:
        """Demonstrate basic dictionary operations."""
        d = {"a": 1, "b": 2, "c": 3}
        
        return {
            "dictionary": d,
            "length": len(d),
            "get_a": d["a"],
            "get_with_default": d.get("d", "default"),
            "keys": list(d.keys()),
            "values": list(d.values()),
            "items": list(d.items()),
        }
    
    @staticmethod
    def dictionary_methods() -> Dict[str, Any]:
        """Demonstrate dictionary methods."""
        d = {"a": 1, "b": 2, "c": 3}
        d_copy = d.copy()
        
        return {
            "update": (lambda: d_copy.update({"d": 4}) or d_copy)(),
            "pop": (lambda: d_copy.pop("a") or d_copy)(),
            "popitem": d.copy().popitem() if d else None,
            "setdefault": (lambda: d_copy.setdefault("e", 5) or d_copy)(),
            "clear_result": "Clears all items",
        }
    
    @staticmethod
    def dictionary_comprehension() -> Dict[str, Dict]:
        """Demonstrate dictionary comprehensions."""
        return {
            "squares": {x: x**2 for x in range(5)},
            "from_list": {x: x for x in ["a", "b", "c"]},
            "filtered": {x: x**2 for x in range(10) if x % 2 == 0},
            "nested": {i: {j: i*j for j in range(3)} for i in range(3)},
        }
    
    @staticmethod
    def merging_dicts() -> Dict[str, Any]:
        """Demonstrate merging dictionaries."""
        d1 = {"a": 1, "b": 2}
        d2 = {"c": 3, "d": 4}
        d3 = {**d1, **d2}  # Python 3.5+
        
        d1_copy = d1.copy()
        d1_copy.update(d2)  # In-place merge
        
        return {
            "dict1": d1,
            "dict2": d2,
            "merged_unpacking": d3,
            "merged_update": d1_copy,
        }
    
    @staticmethod
    def nested_dictionaries() -> Dict[str, Any]:
        """Demonstrate nested dictionaries."""
        person = {
            "name": "Alice",
            "age": 30,
            "address": {
                "street": "123 Main St",
                "city": "Springfield",
            },
            "hobbies": ["reading", "hiking"],
        }
        
        return {
            "person": person,
            "name": person["name"],
            "city": person["address"]["city"],
            "hobbies": person["hobbies"],
        }
    
    @staticmethod
    def iteration_examples() -> Dict[str, Any]:
        """Demonstrate dictionary iteration."""
        d = {"a": 1, "b": 2, "c": 3}
        
        return {
            "keys_iteration": list(d.keys()),
            "values_iteration": list(d.values()),
            "items_iteration": list(d.items()),
            "key_value_pairs": [(k, v) for k, v in d.items()],
            "only_values": [v for v in d.values()],
        }
    
    @staticmethod
    def defaultdict_usage() -> Dict[str, Any]:
        """Demonstrate defaultdict."""
        from collections import defaultdict
        
        dd = defaultdict(list)
        dd["fruits"].append("apple")
        dd["fruits"].append("banana")
        dd["vegetables"].append("carrot")
        
        return {
            "defaultdict": dict(dd),
            "automatic_list_creation": True,
            "no_keyerror": "Missing keys auto-create default value",
        }
    
    @staticmethod
    def counter_usage() -> Dict[str, Any]:
        """Demonstrate Counter."""
        from collections import Counter
        
        words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
        word_count = Counter(words)
        
        return {
            "counter": dict(word_count),
            "most_common": word_count.most_common(2),
            "apple_count": word_count["apple"],
        }
