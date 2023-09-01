-- # 9. Palindrom
def palindrom(lista):
    n = len(lista)
    for i in range(0,int(n/2)):
        if lista[i] != lista[n-i-1]:
            return False
    return True
a = [1,2,2,1]
b = palindrom(a)
if (b):
    print("yes")
else:
    print("no")