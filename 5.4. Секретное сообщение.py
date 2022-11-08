text = "How are you? Eh, ok. Low or Lower.Ohh"
secret_text = ''
for i in text:
    if i.isupper() == True:
        secret_text += str(i)
print(secret_text)
#Решенная