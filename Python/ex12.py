# 12. Create simple calculator

def calculator():
    first_digit = int(input("Type a digit: "))
    outcome = first_digit
    while outcome != "=":
        choice = str(input("Type an operator: (+, -, *, /, =): "))
        match choice:
            case "+":
                digit = int(input("Type another digit: "))
                outcome = outcome + digit
            case "-":
                digit = int(input("Type another digit: "))
                outcome = outcome - digit
            case "*":
                digit = int(input("Type another digit: "))
                outcome = outcome * digit
            case "/":
                digit = int(input("Type another digit: "))
                outcome = outcome / digit
            case "=":
                return outcome
                break

print("Outcome =", calculator())