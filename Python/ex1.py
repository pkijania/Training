# 1. Create menu with addition and subtraction

class AdditionSubtraction:
    def addition():
        sum = 0
        number_of_digits = int(input("How many digits?: "))
        if(number_of_digits < 0):
            print("\nNumber of digits must be at least 0")
        else:
            print("Type", number_of_digits, "digit(s): ")
            for i in range(number_of_digits):
                digit = int(input("Type a digit: "))
                sum = sum + digit
            print("\nSum is: ", sum)

    def subtraction():
        list = []
        number_of_digits = int(input("How many digits?: "))
        match number_of_digits:
            case _ if number_of_digits < 0:
                print("\nNumber of digits must be at least 0")
            case _ if number_of_digits == 0:
                    print("Subtraction is: ", number_of_digits)
            case _ if number_of_digits == 1:
                    subtraction = int(input("Type a digit: "))
                    print("\nSubtraction is: ", subtraction)
            case _ if number_of_digits > 1:
                print("Type", number_of_digits, "digit(s): ")
                for i in range (number_of_digits):
                    digit = int(input("Type a digit: "))
                    list.append(digit)
                first_digit = list[0]
                sum_of_digits = 0
                for i in range (1, len(list)):
                    sum_of_digits += list[i]
                outcome = first_digit - sum_of_digits
                print("\nSubtraction is: ", outcome)

class Menu:
    choice = 0
    while choice != 3:
        print("\nMenu:")
        print("1 = Addition of n digits")
        print("2 = Subtraction of n digits")
        print("3 = Exit the program\n")
        choice = int(input("\nWhat would you like to do?: "))
        match choice:
            case 1:
                AdditionSubtraction.addition()
            case 2:
                AdditionSubtraction.subtraction()
            case 3:
                break
    print("End")