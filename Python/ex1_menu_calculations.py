# 1. Create menu with calculations : addition, subtraction, multiply and division of n digits

def digit(prompt, error):
    input_digit = input(prompt)
    while not input_digit.isdigit():
        input_digit = input(error)
    return int(input_digit)

class Calculations:
    def __init__(self):
        print("Program started")

    def addition(self):
        sum = 0
        number_of_digits = digit("How many digits?: ", "Wrong number of digits, please type a correct number: ")
        print("Type", number_of_digits, "digit(s): ")
        for i in range(number_of_digits):
            number = digit("Type a digit: ", "Wrong digit, please type a correct digit: ")
            sum += number
        return sum

    def subtraction(self):
        list = []
        number_of_digits = digit("How many digits?: ", "Wrong number of digits, please type a correct number: ")
        if number_of_digits == 0:
            subtraction = number_of_digits
        elif number_of_digits == 1:
            subtraction = digit("Type a digit: ", "Wrong digit, please type a correct digit: ")
        else:
            print("Type", number_of_digits, "digit(s): ")
            for i in range (number_of_digits):
                number = digit("Type a digit: ", "Wrong digit, please type a correct digit: ")
                list.append(number)
            sum_of_digits = 0
            for i in range (1, len(list)):
                sum_of_digits += list[i]
            subtraction = list[0] - sum_of_digits
        return subtraction

    def multiply(self):
        multiply = 1
        number_of_digits = digit("How many digits?: ", "Wrong number of digits, please type a correct number: ")
        if number_of_digits == 0:
            multiply = number_of_digits
        else :
            print("Type", number_of_digits, "digit(s): ")
            for i in range(number_of_digits):
                number = digit("Type a digit: ", "Wrong digit, please type a correct digit: ")
                multiply *= number
        return multiply
    
    def division(self):
        division = None
        number_of_digits = digit("How many digits?: ", "Wrong number of digits, please type a correct number: ")
        if number_of_digits == 0:
            division = number_of_digits
        else:
            print("Type", number_of_digits, "digit(s): ")
            list = []
            for i in range(number_of_digits):
                number = digit("Type a digit: ", "Wrong digit, please type a correct digit: ")
                list.append(number)
            for i in range(len(list)):
                if division is None:
                    division = list[i]
                else:
                    division /= list[i]
        return division

if __name__ == "__main__":
    try:
        while True:
            print("\nMenu:")
            print("1 = Addition of n digits")
            print("2 = Subtraction of n digits")
            print("3 = Multiply of n digits")
            print("4 = Division of n digits")
            print("5 = Exit the program\n")
            choice = digit("What would you like to do?: ", "Wrong action, choose again: ")
            calculations = Calculations()
            match choice:
                case 1:
                    print("\nSum is:", calculations.addition())
                case 2:
                    print("\nSubtraction is:", calculations.subtraction())
                case 3:
                    print("\nMultiply equals:", calculations.multiply())
                case 4:
                    print("\nDivision equals:", calculations.division())
                case 5:
                    break
                case _:
                    print("Wrong action, choose again")
        print("End")
    except Exception as wrong_user:
        print(f"Error!!, program shut down due to {wrong_user}")