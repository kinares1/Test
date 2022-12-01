#1. Анализ текста. Популярность.
#Дано: текст (str).
#Задание: необходимо получить 2 словаря (популярности слов и популярности букв).
import string
text = 'hello hello, how are you?'
text = text.translate(str.maketrans('', '', string.punctuation))
words = text.split(" ") # получение списка из слов
letters = text.replace(" ","") # получение строки букв

words_popularity = {}
letters_popularity = {}

for word in set(words):
    words_popularity[word] = text.count(word)

for letter in set(letters):
    letters_popularity[letter] = text.count(letter)
print("Популярность букв:", letters_popularity)
print("Популярность слов:",words_popularity)

