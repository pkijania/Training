// 8. Reverse values in an array

function reverse(list){
    let new_list = [];
    while (list.length){
        new_list.push(list.pop());
    }
    return new_list;
}

console.log(reverse([1, 2, 3, 4, 5]))