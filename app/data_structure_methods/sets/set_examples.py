"""
Set Examples

Practical set usage examples.
"""


class SetExamples:
    """Practical set usage examples."""
    
    @staticmethod
    def removing_duplicates() -> dict:
        """Using sets to remove duplicates."""
        data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        
        return {
            "original": data,
            "unique": list(set(data)),
            "count_unique": len(set(data)),
        }
    
    @staticmethod
    def set_theory_operations() -> dict:
        """Set theory operations."""
        students_a = {"Alice", "Bob", "Carol"}
        students_b = {"Bob", "David", "Eve"}
        
        return {
            "class_a": students_a,
            "class_b": students_b,
            "both_classes": students_a & students_b,
            "either_class": students_a | students_b,
            "only_a": students_a - students_b,
            "only_b": students_b - students_a,
            "either_but_not_both": students_a ^ students_b,
        }
    
    @staticmethod
    def membership_testing() -> dict:
        """Using sets for efficient membership testing."""
        numbers = set(range(1000))
        
        return {
            "size": len(numbers),
            "500_in_set": 500 in numbers,
            "5000_in_set": 5000 in numbers,
            "efficient_lookup": "O(1) average case",
        }
