# 1. Create menu with addition, subtraction and printing numbers functions

def addition():
    sum = 0
    number_of_digits = int(input("How many digits?: "))
    print("Type", number_of_digits, "digit(s): ")
    for i in range(number_of_digits):
        digit = int(input("Type a digit: "))
        sum = sum + digit
    print("Sum is: ", sum)

def subtraction():
    first_digit = int(input("Enter 1 digit: "))
    second_digit = int(input("Enter 2 digit: "))
    print("Your number is:", first_digit - second_digit)

def printing():
    print(1,2,3,4,5)

choice = 0
while choice !=4:
    print("\nMenu")
    print("1 = Addition of n digits")
    print("2 = Subtraction of 2 digits")
    print("3 = Printing 5 digits")
    print("4 = Exit the program\n")
    choice = int(input("\nWhat would you like to do?: "))
    match choice:
        case 1:
            addition()
        case 2:
            subtraction()
        case 3:
            printing()
        case 4:
            break
print("End")
