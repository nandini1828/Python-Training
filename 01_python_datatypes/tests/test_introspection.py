from introspection import inspect_object, get_methods, get_documentation


def test_inspect_basic_types():
    info = inspect_object([1, 2, 3])
    assert info["class_name"] == "list"
    assert "append" in info["methods"]


def test_get_methods():
    methods = get_methods({})
    assert "get" in methods


def test_get_documentation():
    doc = get_documentation(dict)
    assert "mapping" in doc.lower() or isinstance(doc, str)
