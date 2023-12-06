// 4. Create simple calculator

const prompt = require ("prompt-sync")();

function digit(){
    let number = prompt("Type a digit: ");
    while (Number.isInteger(+number) !== true){
        number = prompt("Wrong digit, please type a correct digit: ");
    }
    return parseInt(number, 10);
}

function calculator(){
    let outcome = digit();
    while (true){
        let choice = String(prompt("Type an operator (+, -, *, /, =): "));
        switch (choice.trim()){
            case ("+"):
                outcome += digit();
                break;
            case ("-"):
                outcome -= digit();
                break;
            case ("*"):
                outcome *= digit();
                break;
            case ("/"):
                outcome /= digit();
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