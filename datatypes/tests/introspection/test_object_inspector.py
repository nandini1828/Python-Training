"""Test suite for object inspector."""
import pytest
from datatypes.introspection import ObjectInspector


class TestObjectInspector:
    def test_inspect_object(self):
        result = ObjectInspector.inspect_object([1, 2, 3])
        assert result["type"] == "list"
        assert result["is_callable"] is False
    
    def test_get_attributes(self):
        result = ObjectInspector.get_attributes("hello")
        assert len(result["public_attributes"]) > 0
        assert len(result["methods"]) > 0
