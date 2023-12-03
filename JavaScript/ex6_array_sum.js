// 6. Print the sum of values in an array

function sum_of_values(list){
    let sum = 0;
    for (let i of list){
        sum += i;
    }
    return sum;
}

console.log(sum_of_values([1, 2, 3, 4, 5]))