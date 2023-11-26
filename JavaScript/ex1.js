// 1. Create simple calculator

const prompt = require ("prompt-sync")();

class Calculations{
    addition(){
        let number_of_digits = parseFloat(prompt("How many digits?: "), 10);
        console.log("Type", number_of_digits, "digit(s): ")
        switch (true){
            case (number_of_digits < 0):
                console.log("\nNumber of digits must be at least 0")
                break;
            case (number_of_digits === 0):
                console.log("\Sum is:", number_of_digits)
                break;
            case (number_of_digits > 0):
                let sum = 0;
                for (let i = 1; i <= number_of_digits; i++) {
                    let digit = parseFloat(prompt("Type a digit: "), 10);
                    sum = sum + digit;
                }
                console.log("Sum is:", sum)
                break;
        }
    }

    subtraction(){
        let number_of_digits = parseFloat(prompt("How many digits?: "), 10);
        switch (true){
            case (number_of_digits < 0):
                console.log("\nNumber of digits must be at least 0")
                break;
            case (number_of_digits === 0):
                console.log("\nSubtraction is:", number_of_digits)
                break;
            case (number_of_digits === 1):
                let outcome = parseFloat(prompt("Type a digit: "), 10);
                console.log("\nSubtraction is: ", outcome)
                break;
            case (number_of_digits > 0):
                let list = [];
                console.log("Type", number_of_digits, "digit(s): ")
                for (let i = 0; i < number_of_digits; i++){
                    let digit = parseFloat(prompt("Type a digit: "), 10);
                    list.push(digit);
                }
                let first_digit = list[0];
                let sum_of_digits = 0;
                let subtraction = 0;
                for (let i = 1; i < list.length; i++){
                    sum_of_digits += list[i];
                    subtraction = first_digit - sum_of_digits;
                }
                console.log("\nSubtraction is: ", subtraction)
                break;
        }
    }

    multiply(){
        let number_of_digits = parseInt(prompt("How many digits?: "), 10);
        switch (true){
            case (number_of_digits < 0):
                console.log("\nNumber of digits must be at least 0")
                break;
            case (number_of_digits === 0):
                console.log("\nMultiply equals:", number_of_digits)
                break;
            case (number_of_digits === 1):
                let outcome = parseFloat(prompt("Type a digit: "), 10);
                console.log("\nMultiply equals: ", outcome)
                break;
            case (number_of_digits > 1):
                console.log("Type", number_of_digits, "digit(s): ")
                let multiply = 1;
                for (let i = 0; i < number_of_digits; i++){
                    let digit = parseFloat(prompt("Type a digit: "), 10);
                    multiply = multiply * digit;
                }
                console.log("\nMultiply equals: ", multiply)          
                break;
        }
    }

    division(){
        let number_of_digits = parseInt(prompt("How many digits?: "), 10);
        switch (true){
            case (number_of_digits < 0):
                console.log("\nNumber of digits must be at least 0")
                break;
            case (number_of_digits === 0):
                console.log("\nDivision equals:", number_of_digits)
                break;
            case (number_of_digits === 1):
                let outcome = parseFloat(prompt("Type a digit: "), 10);
                console.log("\Division equals: ", outcome)
                break;
            case (number_of_digits > 1):
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
                        division = division / list[i];  
                    }
                }
                console.log("\nDivision equals: ", division)
                break;
        }
    }
}

class Menu{
    menu(){
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
            switch (true){
                case (choice === 1):
                    calculations.addition();
                    break;
                case (choice === 2):
                    calculations.subtraction();
                    break;
                case (choice === 3):
                    calculations.multiply();
                    break;
                case (choice === 4):
                    calculations.division();
                    break;
                case (choice === 5):
                    break;
                case (choice < 1 || choice > 5):
                    console.log("Wrong action, choose again")
                    break;
            }
            console.log("End")
        }
    }
}

const e = new Menu();
e.menu();