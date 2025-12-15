def unique_words_frequency(words):
    unique = set(words)
    freq = {word: words.count(word) for word in unique}
    return unique, freq


words = ["apple", "banana", "apple", "orange", "banana", "kiwi"]
print(unique_words_frequency(words))
