# 3. Sort numbers in an array

def sort(list):
    a = len(list)
    b = False
    for i in range (a):
        for j in range (0,a-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                b = True
        if b == False: break
    return list
print(sort([1,5,2,6,3,4,12]))