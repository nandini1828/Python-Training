class ListUtils:

    @staticmethod
    def demonstrate() -> list[int]:

        numbers: list[int] = [1, 2]

        numbers.append(3)
        numbers.extend([4, 5])

        return numbers