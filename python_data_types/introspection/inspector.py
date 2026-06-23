import inspect


def get_type(obj):
    """Return type of object."""
    return type(obj)


def get_id(obj):
    """Return memory id of object."""
    return id(obj)


def get_all_attributes(obj):
    """Return all attributes and methods of object."""
    return dir(obj)


def get_public_attributes(obj):
    """Return only public attributes (ignore _ and __)."""
    return [attr for attr in dir(obj) if not attr.startswith("_")]


def get_doc(obj):
    """Return documentation string of object."""
    return inspect.getdoc(obj)


def get_methods(obj):
    """Return all callable methods of object."""
    return [
        attr
        for attr in dir(obj)
        if callable(getattr(obj, attr))
    ]


def get_methods_with_docs(obj):
    """Return methods with their documentation."""
    result = []

    for attr in dir(obj):
        value = getattr(obj, attr)

        if callable(value):
            result.append({
                "method": attr,
                "doc": inspect.getdoc(value)
            })

    return result