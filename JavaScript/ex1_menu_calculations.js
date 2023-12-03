// 1. Create menu with calculations : addition, subtraction, multiply and division of n digits

const prompt = require ("prompt-sync")();

class Calculations{
    addition(){
        let number_of_digits = parseFloat(prompt("How many digits?: "), 10);
        if (number_of_digits < 0){
            console.log("\nNumber of digits must be at least 0")
        }
        else{
            console.log("Type", number_of_digits, "digit(s): ")
            let sum = 0;
            for (let i = 1; i <= number_of_digits; i++) {
                let digit = parseFloat(prompt("Type a digit: "), 10);
                sum += digit;
            }
            console.log("Sum is:", sum)
        }
    }

    subtraction(){
        let number_of_digits = parseFloat(prompt("How many digits?: "), 10);
        if (number_of_digits < 0){
            console.log("\nNumber of digits must be at least 0")
        }
        else if (number_of_digits === 1){
            let outcome = parseFloat(prompt("Type a digit: "), 10);
            console.log("\nSubtraction is: ", outcome)
        }
        else{
            let list = [];
            console.log("Type", number_of_digits, "digit(s): ")
            for (let i = 0; i < number_of_digits; i++){
                let digit = parseFloat(prompt("Type a digit: "), 10);
                list.push(digit);
            }
            let sum_of_digits = 0;
            let subtraction = 0;
            for (let i = 1; i < list.length; i++){
                sum_of_digits += list[i];
                subtraction = list[0] - sum_of_digits;
            }
            console.log("\nSubtraction is: ", subtraction)
        }
    }

    multiply(){
        let number_of_digits = parseInt(prompt("How many digits?: "), 10);
        if (number_of_digits < 0){
            console.log("\nNumber of digits must be at least 0")
        }
        else if (number_of_digits === 0){
            console.log("\nMultiply equals:", number_of_digits)
        }
        else{
            console.log("Type", number_of_digits, "digit(s): ")
            let multiply = 1;
            for (let i = 0; i < number_of_digits; i++){
                let digit = parseFloat(prompt("Type a digit: "), 10);
                multiply *= digit;
            }
            console.log("\nMultiply equals: ", multiply)
        }
    }

    division(){
        let number_of_digits = parseInt(prompt("How many digits?: "), 10);
        if (number_of_digits < 0){
            console.log("\nNumber of digits must be at least 0")
        }
        else if (number_of_digits === 0){
            console.log("\nDivision equals:", number_of_digits)
        }
        else{
            console.log("Type", number_of_digits, "digit(s): ")
            let list = [];
            for (let i = 0; i < number_of_digits; i++){
                let digit = parseFloat(prompt("Type a digit: "), 10)
                list.push(digit);
            }
            let division = 0;
            for (let i = 0; i < list.length; i++){
                if (division === 0){
                    division = list[i];                     
                }
                else {
                    division /= list[i];  
                }
            }
            console.log("\nDivision equals: ", division)
        }
    }
}

function menu(){
    const calculations = new Calculations();
    let choice = 0;
    while (choice != 5){
        console.log("\nMenu")
        console.log("1 = Addition of n digits")
        console.log("2 = Subtraction of n digits")
        console.log("3 = Multipy of n digits")
        console.log("4 = Division of n digits")
        console.log("5 = Exit the program\n")
        choice = parseInt(prompt("\nWhat would you like to do?: "), 10)
        switch (choice){
            case (1):
                calculations.addition();
                break;
            case (2):
                calculations.subtraction();
                break;
            case (3):
                calculations.multiply();
                break;
            case (4):
                calculations.division();
                break;
            case (5):
                break;
            default:
                console.log("Wrong action, choose again")
                break;
        }
        console.log("End")
    }
}

menu();