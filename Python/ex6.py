# 6. Print the sum of values in an array

def sum_of_values(list):
    length = len(list)
    sum = 0
    for i in range (0, length):
        sum = sum + list[i]
    return sum

out = sum_of_values([1,2,3,4,5])
print(out)