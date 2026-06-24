class WordCounter:

    @staticmethod
    def count(text: str) -> dict[str, int]:

        result: dict[str, int] = {}

        for symbol in ".,!?":
            text = text.replace(symbol, "")

        for word in text.lower().split():
            result[word] = result.get(word, 0) + 1

        return result