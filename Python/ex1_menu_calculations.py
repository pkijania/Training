# 1. Create menu with calculations : addition, subtraction, multiply and division of n digits

class Validators:
    def number_of_digits():
        digit = input("How many digits?: ")
        while not digit.isdigit():
            digit = input("Wrong number of digits, please type a correct number: ")
        return int(digit)
    
    def digit():
        number = input("Type a digit: ")
        while not number.isdigit():
            number = input("Wrong digit, please type a correct digit: ")
        return int(number)
    
    def choice():
        choice = input("What would you like to do?: ")
        while not choice.isdigit():
            choice = input("Wrong action, choose again: ")
        return int(choice)

class Calculations:
    def addition():
        number_of_digits = Validators.number_of_digits()
        if number_of_digits < 0:
            print("\nNumber of digits must be at least 0")
        else:
            print("Type", number_of_digits, "digit(s): ")
            sum = 0
            for i in range(number_of_digits):
                digit = Validators.digit()
                sum += digit
            return sum

    def subtraction():
        number_of_digits = Validators.number_of_digits()
        if number_of_digits < 0:
            print("\nNumber of digits must be at least 0")
        elif number_of_digits == 1:
            subtraction = float(input("Type a digit: "))
            print("\nMultiply equals:", subtraction)
        else:
            print("Type", number_of_digits, "digit(s): ")
            list = []
            for i in range (number_of_digits):
                digit = Validators.digit()
                list.append(digit)
            sum_of_digits = 0
            for i in range (1, len(list)):
                sum_of_digits += list[i]
            subtraction = list[0] - sum_of_digits
            return subtraction

    def multiply():
        number_of_digits = Validators.number_of_digits()
        if number_of_digits < 0:
            print("\nNumber of digits must be at least 0")
        elif number_of_digits == 0:
            print("Multiply equals:", number_of_digits)
        else :
            print("Type", number_of_digits, "digit(s): ")
            multiply = 1
            for i in range(number_of_digits):
                digit = Validators.digit()
                multiply *= digit
            return multiply
    
    def division():
        number_of_digits = Validators.number_of_digits()
        if number_of_digits < 0:
            print("\nNumber of digits must be at least 0")
        elif number_of_digits == 0:
            print("Division equals:", number_of_digits)
        else:
            print("Type", number_of_digits, "digit(s): ")
            list = []
            for i in range(number_of_digits):
                digit = Validators.digit()
                list.append(digit)
            division = None
            for i in range(len(list)):
                if division is None:
                    division = list[i]
                else:
                    division /= list[i]
            return division

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1 = Addition of n digits")
        print("2 = Subtraction of n digits")
        print("3 = Multiply of n digits")
        print("4 = Division of n digits")
        print("5 = Exit the program\n")
        choice = Validators.choice()
        match choice:
            case 1:
                print("\nSum is:", Calculations.addition())
            case 2:
                print("\nSubtraction is:", Calculations.subtraction())
            case 3:
                print("\nMultiply equals:", Calculations.multiply())
            case 4:
                print("\nDivision equals:", Calculations.division())
            case 5:
                break
            case _:
                print("Wrong action, choose again")
    print("End")