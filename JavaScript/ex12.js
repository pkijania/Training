// 12. Create simple calculator

const prompt = require ("prompt-sync")();

function calculator(){
    let first_digit = parseInt(prompt("Type a digit: "), 10);
    let outcome = first_digit;
    let digit = 0;
    let prompt_text = "Type another digit: ";
    while (true){
        let choice = String(prompt("Type an operator (+, -, *, /, =): "), 10);
        let choice_trimmed = choice.trim();
        let is_digit = Number.isInteger(choice);
        if (Number.isInteger(+choice)){
            console.log("You typed a digit, please type an operator (+, -, *, /, =): ")
        }
        else {
            switch (choice_trimmed){
                case ("+"):
                    digit = parseInt(prompt(prompt_text), 10);
                    outcome = outcome + digit;
                    break;
                case ("-"):
                    digit = parseInt(prompt(prompt_text), 10);
                    outcome = outcome - digit;
                    break;
                case ("*"):
                    digit = parseInt(prompt(prompt_text), 10);
                    outcome = outcome * digit;
                    break;
                case ("/"):
                    digit = parseInt(prompt(prompt_text), 10);
                    outcome = outcome / digit;
                    break;
                case ("="):
                    return outcome;
            }
        }
    }
}

console.log("Outcome =", calculator())