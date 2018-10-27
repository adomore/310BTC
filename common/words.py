def get_word(index):
    with open('../common/english.txt') as words:
        word = words.readlines()[index - 1]
        word = word[:(len(word) - 1)]
        return word
