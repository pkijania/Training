// 1. Create menu with addition, subtraction and printing numbers functions

const prompt = require ("prompt-sync")();

function addition(){
    let sum = 0;
    let number_of_digits = parseFloat(prompt("How many digits?: "), 10);
    console.log("Type", number_of_digits, "digit(s): ")
    for (let i = 1; i <= number_of_digits; i++) {
        let digit = parseFloat(prompt("Type a digit: "), 10);
        sum = sum + digit;
    }
    console.log("Sum is:", sum)
}

function subtraction(){
    list = [];
    let number_of_digits = parseFloat(prompt("How many digits?: "), 10);
    if (number_of_digits < 0){
        console.log("\nNumber of digits must be at least 0")
    }
    else if(number_of_digits === 0){
        console.log("\nSubtraction is:", number_of_digits)
    }
    else if(number_of_digits === 1){
        let subtraction = parseFloat(prompt("Type a digit: "), 10);
        console.log("\nSubtraction is: ", subtraction)
    }
    else if(number_of_digits > 0){
        console.log("Type", number_of_digits, "digit(s): ")
        for (let i = 0; i < number_of_digits; i++){
            let digit = parseFloat(prompt("Type a digit: "), 10);
            list.push(digit);
        }
        let first_digit = list[0];
        let sum_of_digits = 0;
        let outcome = 0;
        for (let i = 1; i < list.length; i++){
            sum_of_digits += list[i];
            outcome = first_digit - sum_of_digits;
        }
        console.log("\nSubtraction is: ", outcome)
    }
}

function multiply(){
    let number_of_digits = parseInt(prompt("How many digits?: "), 10);
    if (number_of_digits < 0){
        console.log("\nNumber of digits must be at least 0")
    }
    else if (number_of_digits === 0){
        console.log("\nMultiply equals:", number_of_digits)
    }
    else if (number_of_digits === 1){
        let multiply = parseFloat(prompt("Type a digit: "), 10);
        console.log("\nMultiply equals: ", multiply)
    }
    else if (number_of_digits > 1){
        console.log("Type", number_of_digits, "digit(s): ")
        let multiply = 1;
        for (let i = 1; i < number_of_digits; i++){
            let digit = parseFloat(prompt("Type a digit: "), 10);
            multiply = multiply * digit;
        }
        console.log("\nMultiply equals: ", multiply)          
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
    switch (choice){
        case 1:
            addition()
            break;
        case 2:
            subtraction()
            break;
        case 3:
            subtraction()
            break;
        case 4:
            subtraction()
            break;
        case 5:
            break;
    }
    console.log("End")
}