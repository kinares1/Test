def get_word(word):
    reversed_word = word[::-1]
    return word == reversed_word


print(get_word('Hi'))
