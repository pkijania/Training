// 6. Create a coin toss game - predict the outcome of a coin toss

const prompt = require ("prompt-sync")();

function heads_or_tails(){
    let user = prompt("heads or tails? ");
    let computer = ["heads", "tails"];
    let computer_random = Math.floor(Math.random() * computer.length);
    let computer_choice = computer[computer_random];
    if (user === computer_choice){
        console.log("correct")
    }
    else{
        console.log("wrong")
    }
    console.log("user: ", user)
    console.log("computer: ", computer_choice)   
}

heads_or_tails();