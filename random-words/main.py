# lista = ["asd", "basd", "casd", "dasd"]
# print(random.choice(lista))

import random
lista = []
for i in range(25):
    lista.append(random.choice(list(open('words.txt'))))