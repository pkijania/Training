# 7. Count the amount of even and odd numbers

def even_odd(list):
    length = len(list)
    even = 0
    odd = 0
    for i in range(0, length):
        if list[i] % 2 == 0:
            even += 1
        if list[i] % 2 != 0:
            odd += 1
    print("number of even digits", even)
    print("number of odd digits", odd)
    return (even, odd)
 
print(even_odd([1,2,3,4,5,67]))