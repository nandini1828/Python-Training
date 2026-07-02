"""Test suite for comparison and arithmetic examples."""
import pytest
from datatypes.dunder_methods import ComparisonExamples, ArithmeticExamples


class TestComparisonExamples:
    def test_comparison_operators(self):
        result = ComparisonExamples.comparison_operators()
        assert result["less_than"] is True
        assert result["greater_than"] is False
        assert result["equal"] is False
    
    def test_string_comparison(self):
        result = ComparisonExamples.string_comparison()
        assert result["apple_less_than_banana"] is True
    
    def test_comparison_chaining(self):
        result = ComparisonExamples.comparison_chaining()
        assert result["chain_less_than"] is True
        assert result["chain_false"] is False


class TestArithmeticExamples:
    def test_basic_arithmetic(self):
        result = ArithmeticExamples.basic_arithmetic()
        assert result["addition"] == 19
        assert result["subtraction"] == 11
        assert result["multiplication"] == 60
    
    def test_unary_operators(self):
        result = ArithmeticExamples.unary_operators()
        assert result["positive"] == 42
        assert result["negative"] == -42
    
    def test_bitwise_operations(self):
        result = ArithmeticExamples.bitwise_operations()
        assert result["bitwise_and"] == 4
        assert result["bitwise_or"] == 13
