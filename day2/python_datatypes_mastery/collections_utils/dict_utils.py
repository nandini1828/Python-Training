class DictUtils:

    @staticmethod
    def demonstrate() -> dict[str, object]:

        data: dict[str, object] = {}

        data.setdefault("name", "Bhavya")
        data.update({"age": 22})

        return data