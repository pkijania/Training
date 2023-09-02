# 7. Sum of even and odd numbers
def parzysta(lista):
    n = len(lista)
    p = 0
    np = 0
    for i in range(0,n):
        if lista[i] % 2 == 0:
            p += 1
        if lista[i] % 2 != 0:
            np += 1
    return (p,np)
    print("ilosc liczb parzystych", p)
    print("ilosc liczb nieparzystych", np)
parzysta([1,2,3,4,5,67])