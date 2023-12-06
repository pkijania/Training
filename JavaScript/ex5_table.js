// 5. Create and display a table of n columns and n rows and count the sum of all it's elements

const prompt = require ("prompt-sync")();

function tablesum(){
        let row = parseInt(prompt("How many rows? "), 10);
        let column = parseInt(prompt("How many columns? "), 10);
        let sum = 0;
        let digit = 0;
        let list = [];
        for (let i = 0; i < row; i++){
            list[i] = [];
            digit = parseInt(prompt("Type a digit: "), 10);
            for (let j = 0; j < column; j++){
                list[i][j] = digit + "";
                sum += parseInt(list[i][j], 10);
            }
        }
        console.log(list, "\nSum of elements in a table is: " + sum)
}

tablesum()