def tuple_count(tpl, value):
    return tpl.count(value)


def tuple_index(tpl, value, default=None):
    try:
        return tpl.index(value)
    except ValueError:
        return default