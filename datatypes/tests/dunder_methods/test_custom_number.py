"""Test suite for dunder methods."""
import pytest
from datatypes.dunder_methods import CustomNumber, CustomString


class TestCustomNumber:
    def test_addition(self):
        a = CustomNumber(10)
        b = CustomNumber(5)
        c = a + b
        assert c.value == 15
    
    def test_subtraction(self):
        a = CustomNumber(10)
        b = CustomNumber(3)
        c = a - b
        assert c.value == 7
    
    def test_multiplication(self):
        a = CustomNumber(4)
        b = CustomNumber(5)
        c = a * b
        assert c.value == 20
    
    def test_comparison(self):
        a = CustomNumber(10)
        b = CustomNumber(20)
        assert a < b
        assert b > a
        assert a == CustomNumber(10)


class TestCustomString:
    def test_concatenation(self):
        s1 = CustomString("Hello")
        s2 = CustomString(" World")
        result = s1 + s2
        assert result.value == "Hello World"
    
    def test_repetition(self):
        s = CustomString("ab")
        result = s * 3
        assert result.value == "ababab"
    
    def test_length(self):
        s = CustomString("hello")
        assert len(s) == 5
    
    def test_contains(self):
        s = CustomString("hello world")
        assert "world" in s
        assert "xyz" not in s
