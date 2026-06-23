def get_method_names(obj):
    """Return callable method names on an object excluding dunder methods."""
    return [name for name in dir(obj) if callable(getattr(obj, name)) and not name.startswith("__")]
