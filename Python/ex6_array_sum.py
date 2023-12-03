# 6. Print the sum of values in an array

def sum_of_values(list):
    sum = 0
    for i in range (0, len(list)):
        sum += list[i]
    return sum

print(sum_of_values([1, 2, 3, 4, 5]))