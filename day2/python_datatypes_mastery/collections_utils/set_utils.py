class SetUtils:

    @staticmethod
    def demonstrate() -> dict[str, set[int]]:

        a: set[int] = {1, 2, 3}
        b: set[int] = {3, 4, 5}

        return {
            "union": a | b,
            "intersection": a & b,
            "difference": a - b
        }