"""
Utility functions demonstrating range() usage
"""

def generate_numbers(n):
    """Generate numbers from 0 to n-1"""
    return list(range(n))


def generate_custom_range(start, stop, step):
    """Generate custom range"""
    return list(range(start, stop, step))


def even_numbers(n):
    """Return even numbers up to n"""
    return [i for i in range(n) if i % 2 == 0]


def odd_numbers(n):
    """Return odd numbers up to n"""
    return [i for i in range(n) if i % 2 != 0]


def sum_of_range(n):
    """Return sum of numbers from 0 to n-1"""
    return sum(range(n))