"""Test suite for SafeCast class."""
import pytest
from datatypes.type_casting import SafeCast


class TestSafeCast:
    def test_to_int(self):
        assert SafeCast.to_int("42") == 42
        assert SafeCast.to_int("invalid") == 0
        assert SafeCast.to_int(42.5) == 42
    
    def test_to_float(self):
        assert SafeCast.to_float("3.14") == 3.14
        assert SafeCast.to_float("invalid") == 0.0
        assert SafeCast.to_float(42) == 42.0
    
    def test_to_str(self):
        assert SafeCast.to_str(42) == "42"
        assert SafeCast.to_str(3.14) == "3.14"
        assert SafeCast.to_str(True) == "True"
    
    def test_to_bool(self):
        assert SafeCast.to_bool(1) is True
        assert SafeCast.to_bool(0) is False
        assert SafeCast.to_bool("") is False
        assert SafeCast.to_bool("hello") is True
    
    def test_attempt_cast(self):
        result = SafeCast.attempt_cast("42", int, float, str)
        assert result == 42
        assert isinstance(result, int)
