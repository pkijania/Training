# 7. Create a list with random numbers and delete duplicates

import random

def duplicates():
    old_list = []
    list_length = int(input("How many digits? "))
    for i in range(list_length):
        old_list.append(random.randint(0, list_length))
    temp_set = set()

    for item in old_list:
        temp_set.add(item)
    new_list = list(temp_set)

    if len(old_list) == len(new_list):
        print("List without duplicates:", new_list)
    else:
        print("List:", old_list, "List without duplicates:", new_list)

duplicates()