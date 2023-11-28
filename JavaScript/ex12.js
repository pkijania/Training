// 12. Create simple calculator

const prompt = require ("prompt-sync")();

function calculator(){
    let first_digit = parseInt(prompt("Type a digit: "), 10);
    let outcome = first_digit;
    let digit = 0;
    while (outcome != "="){
        let choice = String(prompt("Type an operator: (+, -, *, /, =): "), 10);
        switch (choice){
            case ("+"):
                digit = parseInt(prompt("Type another digit: "), 10);
                outcome = outcome + digit;
                break;
            case ("-"):
                digit = parseInt(prompt("Type another digit: "), 10);
                outcome = outcome - digit;
                break;
            case ("*"):
                digit = parseInt(prompt("Type another digit: "), 10);
                outcome = outcome * digit;
                break;
            case ("/"):
                digit = parseInt(prompt("Type another digit: "), 10);
                outcome = outcome / digit;
                break;
            case ("="):
                return outcome;
                break;
        }
    }
}

console.log("Outcome =", calculator())