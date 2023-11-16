// 8. Reverse values in an array

const prompt = require ("prompt-sync")();

function reverse(list){
    let new_list = [];
    for (let i of list){
        new_list.push(list.length -1 - i);
    }
    return new_list;
}
out = reverse([0, 1, 2, 3, 4, 5])
console.log(out)