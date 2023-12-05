# 4. Create simple calculator

def digit():
    number = input("Type a digit: ")
    while not number.isdigit():
        number = input("Wrong digit, please type a correct digit: ")
    return int(number)

if __name__ == "__main__":
    outcome = digit()
    while True:
        choice = str(input("Type an operator (+, -, *, /, =): "))
        match choice.strip():
            case "+":  
                outcome += digit()
            case "-":
                outcome -= digit()
            case "*":
                outcome *= digit()
            case "/":
                outcome /= digit()
            case "=":
                print("Outcome =", outcome)
                break
            case _:
                print("Wrong operator")