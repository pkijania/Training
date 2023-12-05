# 8. Create a list with random numbers and delete duplicates

import random

def random_values():
    lista = []
    list_length = int(input("How many digits? "))
    for i in range(list_length):
        lista.append(random.randint(0, list_length))
    print(lista)

    temp_set = set()

    for item in lista:
        temp_set.add(item)

    output = list(temp_set)
    return output

print(random_values())