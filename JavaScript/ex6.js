// 6. Print the sum of values in array

const prompt = require ("prompt-sync")();

function sum_of_values(list){
    let sum = 0;
    for (let i of list){
        sum += i;
    }
    return sum;
}

out = sum_of_values([1, 2, 3, 4, 5])
console.log(out)