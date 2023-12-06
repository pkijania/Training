// 1. Create menu with calculations : addition, subtraction, multiply and division of n digits

const prompt = require ("prompt-sync")();

class Validators{
    digit(prompt_text, error){
        let input_digit = prompt(prompt_text);
        while (Number.isInteger(+input_digit) !== true){
            input_digit = prompt(error);
        }
        return parseInt(input_digit, 10);
    }
}

class Calculations{
    addition(){
        const validators = new Validators();
        let sum = 0;
        let number_of_digits = validators.digit("How many digits?: ", "Wrong number of digits, please type a correct number: ");
        if (number_of_digits < 0){
            console.log("\nNumber of digits must be at least 0")
        }
        else{
            console.log("Type", number_of_digits, "digit(s): ")
            for (let i = 1; i <= number_of_digits; i++){
                let digit = validators.digit("Type a digit: ", "Wrong digit, please type a correct digit: ");
                sum += digit;
            }
        }
        return sum;
    }

    subtraction(){
        const validators = new Validators();
        let sum_of_digits = 0;
        let subtraction = 0;
        let list = [];
        let number_of_digits = validators.digit("How many digits?: ", "Wrong number of digits, please type a correct number: ");
        if (number_of_digits < 0){
            console.log("\nNumber of digits must be at least 0")
        }
        else if (number_of_digits === 1){
            subtraction = validators.digit("Type a digit: ", "Wrong digit, please type a correct digit: ");
        }
        else{
            console.log("Type", number_of_digits, "digit(s): ")
            for (let i = 0; i < number_of_digits; i++){
                let digit = validators.digit("Type a digit: ", "Wrong digit, please type a correct digit: ");
                list.push(digit);
            }
            for (let i = 1; i < list.length; i++){
                sum_of_digits += list[i];
                subtraction = list[0] - sum_of_digits;
            }
        }
        return subtraction;
    }

    multiply(){
        let multiply = 0;
        const validators = new Validators();
        let number_of_digits = validators.digit("How many digits?: ", "Wrong number of digits, please type a correct number: ");
        if (number_of_digits < 0){
            console.log("\nNumber of digits must be at least 0")
        }
        else if (number_of_digits === 0){
            multiply = number_of_digits;
        }
        else{
            multiply = 1;
            console.log("Type", number_of_digits, "digit(s): ")
            for (let i = 0; i < number_of_digits; i++){
                let digit = validators.digit("Type a digit: ", "Wrong digit, please type a correct digit: ");
                multiply *= digit;
            }
        }
        return multiply;
    }

    division(){
        const validators = new Validators();
        let division = 0;
        let list = [];
        let number_of_digits = validators.digit("How many digits?: ", "Wrong number of digits, please type a correct number: ");
        if (number_of_digits < 0){
            console.log("\nNumber of digits must be at least 0")
        }
        else if (number_of_digits === 0){
            division = number_of_digits;
        }
        else{
            console.log("Type", number_of_digits, "digit(s): ")
            for (let i = 0; i < number_of_digits; i++){
                let digit = validators.digit("Type a digit: ", "Wrong digit, please type a correct digit: ");
                list.push(digit);
            }
            for (let i = 0; i < list.length; i++){
                if (division === 0){
                    division = list[i];                     
                }
                else {
                    division /= list[i];  
                }
            }
        }
        return division;
    }
}

if (require.main === module){
    const calculations = new Calculations();
    let choice = 0;
    while (true){
        console.log("\nMenu")
        console.log("1 = Addition of n digits")
        console.log("2 = Subtraction of n digits")
        console.log("3 = Multipy of n digits")
        console.log("4 = Division of n digits")
        console.log("5 = Exit the program\n")
        choice = parseInt(prompt("\nWhat would you like to do?: "), 10)
        switch (choice){
            case (1):
                console.log("\nSum is:", calculations.addition())
                break;
            case (2):
                console.log("\nSubtraction is:", calculations.subtraction())
                break;
            case (3):
                console.log("\nMultiply equals:", calculations.multiply())
                break;
            case (4):
                console.log("\nDivision equals:", calculations.division())
                break;
            case (5):
                return;
            default:
                console.log("Wrong action, choose again")
                break;
        }
        console.log("End")
    }
}