// 8. Create a list with random numbers and count every number

const prompt = require ("prompt-sync")();

function count_numbers(){
    let list = [];
    let dictionary = {};
    let list_length = parseInt(prompt("How many digits? "), 10);
    for (let i = 0; i < list_length; i++){
        list.push(Math.floor(Math.random() * list_length));
    }

    console.log(list)
    for (i of list){
        dictionary[i] = 0;
    }

    for (i of list){
        if (dictionary[i] === 0){
            dictionary[i] = 1;
        }
        else{
            dictionary[i] = dictionary[i] + 1;
        }
    }
    return dictionary;
}

console.log(count_numbers())