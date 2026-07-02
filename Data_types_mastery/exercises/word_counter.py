def word_count(text):
    text = text.lower()
    for ch in ".,!?":
        text = text.replace(ch, "")

    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
