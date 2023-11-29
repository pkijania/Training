// 12. Create simple calculator

const prompt = require ("prompt-sync")();

function digit(){
    let number = parseInt(prompt("Type a digit: ", 10));
    while (Number.isInteger(+number) !== true){
        number = parseInt(prompt("Wrong digit, please type a correct digit: ", 10));
    }
    return number;
}

function calculator(){
    let outcome = digit();
    while (true){
        let choice = String(prompt("Type an operator (+, -, *, /, =): "), 10);
        switch (choice.trim()){
            case ("+"):
                outcome = outcome + digit();
                break;
            case ("-"):
                outcome = outcome - digit();
                break;
            case ("*"):
                outcome = outcome * digit();
                break;
            case ("/"):
                outcome = outcome / digit();
                break;
            case ("="):
                return outcome;
            default:
                console.log("Wrong operator")
                break;
        }
    }
}

console.log("Outcome =", calculator())