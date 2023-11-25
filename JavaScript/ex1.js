// 1. Create simple calculator

const prompt = require ("prompt-sync")();

function addition(){
    let sum = 0;
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
            for (let i = 1; i <= number_of_digits; i++) {
                let digit = parseFloat(prompt("Type a digit: "), 10);
                sum = sum + digit;
            }
            console.log("Sum is:", sum)
            break;
    }
}

function subtraction(){
    list = [];
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

function multiply(){
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

function division(){
    let number_of_digits = parseInt(prompt("How many digits?: "), 10);
    if (number_of_digits < 0){
        console.log("\nNumber of digits must be at least 0")
    }
    else if (number_of_digits === 0){
        console.log("\nMultiply equals:", number_of_digits)
    }
    else if (number_of_digits === 1){
        let division = parseFloat(prompt("Type a digit: "), 10);
        console.log("\nMultiply equals: ", division)
    }
    else if (number_of_digits > 1){
        console.log("Type", number_of_digits, "digit(s): ")
        let list = [];
        for (let i = 1; i < number_of_digits; i++){
            let digit = parseFloatfloat(input("Type a digit: "))
            list.push(digit);
        }
        let outcome = undefined;
        for (let i = 1; i < number_of_digits; i++){
            let division = list[i] / list[i + 1];
            outcome += division;
        }
        console.log("\nDivision equals: ", division)
    }
}

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
            addition()
            break;
        case (choice === 2):
            subtraction()
            break;
        case (choice === 3):
            multiply()
            break;
        case (choice === 4):
            division()
            break;
        case (choice === 5):
            break;
        case (choice < 1 || choice > 5):
            console.log("Wrong action, choose again")
            break;
    }
    console.log("End")
}