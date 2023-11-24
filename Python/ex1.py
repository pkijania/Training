# 1. Create menu with addition, subtraction, multiply and division

class Calculations:
    def addition():
        number_of_digits = int(input("How many digits?: "))
        if number_of_digits < 0:
            print("\nNumber of digits must be at least 0")
        elif number_of_digits == 0:
            print("\nSum is: ", number_of_digits)
        else:
            print("Type", number_of_digits, "digit(s): ")
            sum = 0
            for i in range(number_of_digits):
                digit = float(input("Type a digit: "))
                sum = sum + digit
            print("\nSum is: ", sum)

    def subtraction():
        number_of_digits = int(input("How many digits?: "))
        match number_of_digits:
            case _ if number_of_digits < 0:
                print("\nNumber of digits must be at least 0")
            case _ if number_of_digits == 0:
                    print("Subtraction is: ", number_of_digits)
            case _ if number_of_digits == 1:
                    subtraction = float(input("Type a digit: "))
                    print("\nSubtraction is: ", subtraction)
            case _ if number_of_digits > 1:
                print("Type", number_of_digits, "digit(s): ")
                list = []
                for i in range (number_of_digits):
                    digit = float(input("Type a digit: "))
                    list.append(digit)
                first_digit = list[0]
                sum_of_digits = 0
                for i in range (1, len(list)):
                    sum_of_digits += list[i]
                outcome = first_digit - sum_of_digits
                print("\nSubtraction is: ", outcome)

    def multiply():
        number_of_digits = int(input("How many digits?: "))
        match number_of_digits:
            case _ if number_of_digits < 0:
                print("\nNumber of digits must be at least 0")
            case _ if number_of_digits == 0:
                print("Multiply equals: ", number_of_digits)
            case _ if number_of_digits == 1:
                multiply = float(input("Type a digit: "))
                print("\nMultiply equals: ", multiply)
            case _ if number_of_digits > 1:
                print("Type", number_of_digits, "digit(s): ")
                multiply = 1
                for i in range(number_of_digits):
                    digit = float(input("Type a digit: "))
                    multiply = multiply * digit
                print("\nMultiply equals: ", multiply)
    
    def division():
        number_of_digits = int(input("How many digits?: "))
        match number_of_digits:
            case _ if number_of_digits < 0:
                print("\nNumber of digits must be at least 0")
            case _ if number_of_digits == 0:
                print("Division equals: ", number_of_digits)
            case _ if number_of_digits == 1:
                division = float(input("Type a digit: "))
                print("\nDivision equals: ", division)
            case _ if number_of_digits > 1:
                print("Type", number_of_digits, "digit(s): ")
                list = []
                for i in range(number_of_digits):
                    digit = float(input("Type a digit: "))
                    list.append(digit)
                division = None
                for i in range(len(list) - 1):
                    division = (division + list[i]) / list[i + 1]
                print("\nDivision equals: ", division)

class Menu:
    choice = 0
    while choice != 5:
        print("\nMenu:")
        print("1 = Addition of n digits")
        print("2 = Subtraction of n digits")
        print("3 = Multiply of n digits")
        print("4 = Division of n digits")
        print("5 = Exit the program\n")
        choice = int(input("\nWhat would you like to do?: "))
        match choice:
            case 1:
                Calculations.addition()
            case 2:
                Calculations.subtraction()
            case 3:
                Calculations.multiply()
            case 4:
                Calculations.division()
            case 5:
                break
            case _ if choice < 1 or choice > 5:
                print("Wrong action, choose again")
    print("End")