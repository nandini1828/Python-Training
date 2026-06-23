"""
Tuple Examples

Practical tuple usage examples.
"""


class TupleExamples:
    """Practical tuple usage examples."""
    
    @staticmethod
    def function_multiple_returns() -> dict:
        """Using tuples for multiple return values."""
        def get_min_max(numbers):
            return min(numbers), max(numbers)
        
        min_val, max_val = get_min_max([3, 1, 4, 1, 5, 9])
        
        return {
            "result": (min_val, max_val),
            "min": min_val,
            "max": max_val,
        }
    
    @staticmethod
    def coordinate_system() -> dict:
        """Using tuples for coordinates."""
        points = [(0, 0), (1, 0), (0, 1), (1, 1)]
        
        return {
            "points": points,
            "origin": points[0],
            "distances": [
                ((x**2 + y**2) ** 0.5)
                for x, y in points
            ],
        }
    
    @staticmethod
    def rgb_colors() -> dict:
        """Using tuples for RGB colors."""
        colors = {
            "red": (255, 0, 0),
            "green": (0, 255, 0),
            "blue": (0, 0, 255),
        }
        
        return {
            "red": colors["red"],
            "green_value": colors["green"][1],
        }
