# 6. Sum of values in array
def sumowanie(lista):
    n = len(lista)
    suma = 0
    for i in range (0,n):
        suma = suma + lista[i]
    return suma
a = sumowanie([1,2,3,4,5])
print(a)