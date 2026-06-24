class TupleUtils:

    @staticmethod
    def demonstrate() -> dict[str, int]:

        data: tuple[int, ...] = (1, 2, 2, 3)

        return {
            "count": data.count(2),
            "index": data.index(3)
        }