# 8. Create a list with random numbers and delete duplicates

import random

def random_values():
    old_list = []
    list_length = int(input("How many digits? "))
    for i in range(list_length):
        old_list.append(random.randint(0, list_length))
    print(old_list)

    temp_set = set()
    for item in old_list:
        temp_set.add(item)
    print(temp_set)
    new_list = list(temp_set)
    return new_list

print(random_values())