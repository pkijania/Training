# 8. Create a list with random numbers and count every number

import random
import operator

def count_numbers():
    dictonary = {}
    list = []
    list_length = int(input("How many digits? "))
    for i in range(list_length):
        list.append(random.randint(0, list_length))

    for i in list:
        dictonary[i] = 0

    for i in list:
        if dictonary[i] == 0:
            dictonary[i] = 1
        else:
            dictonary[i] = dictonary[i] + 1

    sorted_dictionary = sorted(dictonary.items(), key = operator.itemgetter(0))
    return sorted_dictionary

print(count_numbers())