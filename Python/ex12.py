# 12. Create simple calculator

def digit():
    number = input("Type a digit: ")
    while not number.isdigit():
        number = input("Wrong digit, please type a correct digit: ")
    return int(number)

def calculator():
    outcome = digit()
    while True:
        choice = str(input("Type an operator (+, -, *, /, =): "))
        match choice.strip():
            case "+":  
                outcome = outcome + digit()
            case "-":
                outcome = outcome - digit()
            case "*":
                outcome = outcome * digit()
            case "/":
                outcome = outcome / digit()
            case "=":
                return outcome
            case _:
                print("Wrong operator")

print("Outcome =", calculator())