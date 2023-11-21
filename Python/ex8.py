# 8. Reverse values in an array

def reverse(list):
    length = len(list)
    new_list = []
    for i in range(1, length + 1):
        new_list.append(list[-i])
    return new_list

out = reverse([0,1,2,3,4,5,6,7,8,9,10,11])
print(out)