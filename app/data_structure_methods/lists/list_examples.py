"""
List Examples

Practical examples of list usage.
"""

from typing import List


class ListExamples:
    """Practical list usage examples."""
    
    @staticmethod
    def real_world_scenarios() -> dict:
        """Real-world list usage examples."""
        # Student grades
        grades = [85, 90, 78, 95, 88]
        
        # Processing data
        users = [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25},
            {"name": "Carol", "age": 35},
        ]
        
        return {
            "average_grade": sum(grades) / len(grades),
            "highest_grade": max(grades),
            "passing_grades": [g for g in grades if g >= 80],
            "user_names": [u["name"] for u in users],
            "adults": [u for u in users if u["age"] >= 30],
        }
    
    @staticmethod
    def nested_lists() -> dict:
        """Working with nested lists."""
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        
        return {
            "matrix": matrix,
            "first_row": matrix[0],
            "element_at_1_1": matrix[1][1],
            "flattened": [item for row in matrix for item in row],
            "transpose": [[matrix[i][j] for i in range(3)] for j in range(3)],
        }
    
    @staticmethod
    def list_mutations() -> dict:
        """Demonstrating list mutations."""
        original = [1, 2, 3]
        
        modified = original.copy()
        modified.append(4)
        
        extended = original.copy()
        extended.extend([5, 6])
        
        return {
            "original": original,
            "after_append": modified,
            "after_extend": extended,
            "original_unchanged": original,
        }
