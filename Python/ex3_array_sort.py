# 3. Sort numbers in an array

def sort(list):
    end = False
    for i in range (len(list)):
        for j in range (0, len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                end = True
        if end == False: break
    return list

print(sort([1, 5, 2, 6, 3, 4, 12]))