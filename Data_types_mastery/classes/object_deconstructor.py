def deconstruct_object(obj):
    """Recursively convert custom objects into nested dictionaries."""

    if isinstance(obj, dict):
        return {key: deconstruct_object(value) for key, value in obj.items()}

    if isinstance(obj, (list, tuple, set)):
        container = [deconstruct_object(item) for item in obj]
        return tuple(container) if isinstance(obj, tuple) else container

    if hasattr(obj, "__dict__"):
        return {key: deconstruct_object(value) for key, value in obj.__dict__.items()}

    return obj
