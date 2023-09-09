# 1. Create menu with addition, subtraction and printing numbers functions

def addition():
    sum = 0
    n = int(input("How many digits?: "))
    print("Print",n, "digit(s): ")
    for i in range(n):
        c = int(input("Type a digit: "))
        sum = sum + c
    print("Sum is: ", sum)

def subtraction():
    x = int(input("Enter 1 digit: "))
    y = int(input("Enter 2 digit: "))
    print("Your number is:", x - y)

def printing(*z):
    print(1,2,3,4,5)

x = 0
while x !=4:
    print("\nMenu")
    print("1 = addition of n digits")
    print("2 = subtraction of 2 digits")
    print("3 = printing 5 digits")
    print("4 = Ending the program\n")
    x = int(input("\nWhat would you like to do?: "))
    match x:
        case 1:
            addition()
        case 2:
            subtraction()
        case 3:
            printing()
        case 4:
            break
print("End")
