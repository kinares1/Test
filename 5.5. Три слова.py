text = "start 5 one two three 7 end"
words = text.split()
for triple in zip(words, words[1:], words[2:]):
    if all(s.isalpha() for s in triple):
        print("True")
        print(*triple)
        break
else:
    print("not found")
#Решенная


