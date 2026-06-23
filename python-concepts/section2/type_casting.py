def safe_cast(value, target_type, default=None):
    try:
        return target_type(value)
    except (ValueError, TypeError):
        return default