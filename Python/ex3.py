# 3. Bubble sort

def sortowanie(lista):
    a = len(lista)
    b = False
    for i in range (a):
        for j in range (0,a-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                b = True
        if b == False: break
    return lista
print(sortowanie([1,5,2,6,3,4,12]))