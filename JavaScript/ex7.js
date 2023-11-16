// 7. Count the amount of even and odd numbers

const prompt = require ("prompt-sync")();

function even(list){
    let even_number = 0;
    let odd_number = 0;
    for (let i of list){
        if (i % 2 === 0){
            even_number += 1;
        }
        else if (i % 2 != 0){
            odd_number += 1;
        }
    }
    console.log("number of even digits", even_number)
    console.log("number of odd digits", odd_number)
}
out = even([1, 2, 3, 4, 5, 6, 7])
console.log(out)