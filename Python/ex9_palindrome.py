# 9. Check if a word or a number is a palindrome

def palindrome(list):
    length = len(list)
    for i in range(0, int(length/2)):
        if list[i] != list[length - i - 1]:
            return False
    return True

out = palindrome([1, 2, 2, 1])
if out:
    print("It is a palindrome")
else:
    print("It is not a palindrome")