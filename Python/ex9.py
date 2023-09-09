# 9. Check if a word or a number is a palindrome

def palindrome(list):
    n = len(list)
    for i in range(0,int(n/2)):
        if list[i] != list[n-i-1]:
            return False
    return True
a = [1,2,2,1]
b = palindrome(a)
if (b):
    print("yes")
else:
    print("no")