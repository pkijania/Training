# 12. Create simple calculator

def calculator():
    first_digit = int(input("Type a digit: "))
    outcome = first_digit
    prompt_text = "Type another digit: "
    while True:
        choice = str(input("Type an operator (+, -, *, /, =): "))
        choice_trimmed = choice.strip()
        is_digit = choice.isdigit()
        if is_digit:
            print("You typed a digit, please type an operator (+, -, *, /, =): ")
        else:
            match choice_trimmed:
                case "+":
                    digit = int(input(prompt_text))
                    outcome = outcome + digit
                case "-":
                    digit = int(input(prompt_text))
                    outcome = outcome - digit
                case "*":
                    digit = int(input(prompt_text))
                    outcome = outcome * digit
                case "/":
                    digit = int(input(prompt_text))
                    outcome = outcome / digit
                case "=":
                    return outcome

print("Outcome =", calculator())