# 7. Count the amount of even and odd numbers

def even(list):
    n = len(list)
    p = 0
    np = 0
    for i in range(0,n):
        if list[i] % 2 == 0:
            p += 1
        if list[i] % 2 != 0:
            np += 1
    return (p,np)
    print("number of even digits", p)
    print("number of odd digits", np)
a = even([1,2,3,4,5,67])
print(a)