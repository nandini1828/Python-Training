def get_docstrings(obj):
    """Return a mapping of public attribute names to their docstrings."""
    return {name: getattr(getattr(obj, name), "__doc__", None) for name in dir(obj) if not name.startswith("__")}
