def query_json(data_dict, path_str, default=None):
    """Query a nested dictionary using a dot-separated path string."""
    keys = path_str.split('.') if path_str else []
    current = data_dict
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current
