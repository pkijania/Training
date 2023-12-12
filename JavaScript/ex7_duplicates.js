// 7. Create a list with random numbers and delete duplicates

const prompt = require ("prompt-sync")();

function duplicates(){
    let old_list = [];
    let list_length = parseInt(prompt("How many digits? "), 10);
    for (let i = 0; i < list_length; i++){
        old_list.push(Math.floor(Math.random() * list_length));
    }
    const temp_set = new Set();

    for (let item of old_list){
        temp_set.add(item);
    }
    let new_list = Array.from(temp_set);
    
    if (old_list.length === new_list.length){
        console.log("List without duplicates:", new_list)
    }
    else{
        console.log("List:", old_list, "List without duplicates:", new_list)
    }
}

duplicates()