def list_public_attributes(obj):
    """Return public attribute and method names for any object."""
    return [name for name in dir(obj) if not name.startswith("_")]
