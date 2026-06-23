def word_count(text):

    text = text.lower()

    for symbol in ".,!?":
        text = text.replace(symbol, "")

    frequency = {}

    for word in text.split():
        frequency[word] = frequency.get(word, 0) + 1

    return frequency