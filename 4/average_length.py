
def average_length(strings):
    word_lengths = [len(string) for string in strings]
    average_length = round(sum(word_lengths) / len(word_lengths), 1)
    return average_length

