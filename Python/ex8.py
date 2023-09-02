# 8. Reverse of values in an array

def zamiana_miejsc(lista):
    n = len(lista)
    new_list = []
    for i in range(1,n+1):
        new_list.append(lista[-i])
    return new_list
out = zamiana_miejsc([0,1,2,3,4,5,6,7,8,9,10,11])
print(out)