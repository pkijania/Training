# 8. Reverse values in an array

def reverse(list):
    new_list = []
    for i in range(1, len(list) + 1):
        new_list.append(list[-i])
    return new_list

print("Reversed list: ", reverse([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))