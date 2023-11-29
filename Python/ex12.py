# 12. Create simple calculator

def is_digit():
    digit = input("Type a digit: ")
    while not digit.isdigit():
        digit = input("Wrong digit, please type a correct digit: ")
    return int(digit)

def calculator():
    outcome = int(input("Type a digit: "))
    while True:
        choice = str(input("Type an operator (+, -, *, /, =): "))
        match choice.strip():
            case "+":  
                outcome = outcome + is_digit()
            case "-":
                outcome = outcome - is_digit()
            case "*":
                outcome = outcome * is_digit()
            case "/":
                outcome = outcome / is_digit()
            case "=":
                return outcome
            case _:
                print("Wrong operator, please type correct operator (+, -, *, /, =): ")

print("Outcome =", calculator())