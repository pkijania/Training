// 1. Create menu with addition, subtraction and printing numbers functions

const prompt = require ("prompt-sync")();

function addition(){
    let sum = 0;
    let number_of_digits = parseInt(prompt("How many digits?: "), 10);
    console.log("Type", number_of_digits, "digit(s): ")
    for (let i = 1; i <= number_of_digits; i++) {
        let digit = parseInt(prompt("Type a digit: "), 10);
        sum = sum + digit;
    }
    console.log("Sum is:", sum)
}

function subtraction(){
    let first_digit = parseInt(prompt("Enter 1 digit: "))
    let second_digit = parseInt(prompt("Enter 2 digit: "))
    console.log("Your number is:", first_digit - second_digit)
}

function printing(){
    console.log(1, 2, 3, 4, 5)
}

let choice = 0;
while (choice != 4){
    console.log("\nMenu")
    console.log("1 = Addition of n digits")
    console.log("2 = Subtraction of 2 digits")
    console.log("3 = Printing 5 digits")
    console.log("4 = Exit the program")
    choice = parseInt(prompt("\nWhat would you like to do?: "), 10)
    switch (choice){
        case 1:
            addition()
            break;
        case 2:
            subtraction()
            break;
        case 3:
            printing()
            break;
        case 4:
            break;
    }
    console.log("End")
}