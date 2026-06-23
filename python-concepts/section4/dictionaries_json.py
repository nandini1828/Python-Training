def query_json(data_dict, path_str, default=None):

    current = data_dict

    for key in path_str.split("."):

        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default

    return current