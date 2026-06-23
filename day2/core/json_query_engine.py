class NestedJSONQueryEngine:

    def query(
        self,
        data_dict,
        path,
        default=None
    ):
        current = data_dict

        for key in path.split("."):

            if (
                isinstance(current, dict)
                and key in current
            ):
                current = current[key]

            else:
                return default

        return current