// 11. Class containing some of previous exercises and two simple methods for creating tables

const prompt = require ("prompt-sync")();

class Lists_exercises{
    
    constructor(list){
        this.list = list;
    }

    // Min and max in a list
    minmax(list){
        let min = list[0];
        let max = list[0];
        for (let i of list){
            if (i > max){
                max = i;
            }
            if (i < min){
                min = i;
            }
        }
        return "Min is " + min + "\n" + "Max is " + max;
    }

    // Sorting elements in a list
    sort(list){
        let length = list.length;
        let end = false;
        for (let i = 0; i <= length; i++){
            for (let j = 0; j <= length - 1; j++){
                if (list[j] > list[j + 1]){
                    let temp = list[j];
                    list[j] = list[j + 1];
                    list[j + 1] = temp;
                    end = true;
                }
            }
            if (end === false){
                break;
            }
        }
        return "Sorted list: " + list;
    }

    // Sum of 2 elements
    sum(){
        let first_number = parseInt(prompt("Type a number: "), 10);
        let second_number = parseInt(prompt("Type a 2 number: "), 10);
        return first_number + second_number;
    }

    // Sum of 2 elements
    sum_1(first, second){
        return parseInt(first + second, 10);
    }

    // Addition of n number of elements
    sum_list(){
        let length = parseInt(prompt("How many digits? "), 10);
        let sum = 0;
        for (let i = 1; i <= length; i++){
            let digit = parseInt(prompt("Type a digit: "), 10);
            sum += digit;
        }
        return sum;
    }

    // Check if a word or a number is a palindrome
    palindrome(list){
        for (let i = 0; i < list.length/2; i++){
            if (list[i] != list[list.length - 1 - i]){
                return false;
            }
        }
        return true;
    }
}

class Table_exercise extends Lists_exercises{

    // Display reversed list
    reverse(list){
        let new_list = [];
        while (list.length){
            new_list.push(list.pop());
        }
        return new_list;
    }

    // Create and display a table of 4 columns and 3 rows and count the sum of all it's elements
    tablesum(){
        let row = 3;
        let column = 4;
        let word = "";
        let list = [];
        for (let i = 0; i < row; i++){
            list[i] = [];
        }
        for (let i = 0; i < row; i++){
            for (let j = 0; j < column; j++){
                list[i][j] = 10 + "";
            }
        }

        for (let i = 0; i < row; i++){
            for (let j = 0; j < column; j++){
                word += list[i][j];
            }
        }
        console.log(list)
        let sum = 0;
        for (let i = 0; i < row; i++){
            for (let j = 0; j < column; j++){
                sum = sum + parseInt(list[i][j], 10);
            }
        }
        console.log("Sum of elements in a table is: " + sum)
    }
}

let out = new Table_exercise();
console.log(out.tablesum())

let out = new Table_exercise([1, 2, 3, 4, 5]);
console.log(out.reverse([1, 2, 3, 4, 5]))

let out = new Lists_exercises([1, 2, 3, 4, 0, 6]);
console.log(out.minmax([1, 2, 3, 4, 0, 6]))

let out_2 = new Lists_exercises([1, 23, 13, 4, 0, 6]);
console.log(out_2.sort([1, 23, 13, 4, 0, 6]))