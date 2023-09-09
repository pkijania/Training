# 6. Print the sum of values in array

def sum_of_values(list):
    n = len(list)
    sum = 0
    for i in range (0,n):
        sum = sum + list[i]
    return sum
a = sum_of_values([1,2,3,4,5])
print(a)