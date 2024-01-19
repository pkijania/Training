// 6. Create a coin toss game - predict the outcome of a coin toss

const prompt = require ("prompt-sync")();

class TossGame{
    constructor(){
        this.correct_choices = ["heads", "tails"];
    }

    users_choice(){
        this.user = prompt("heads or tails? ");
    }

    computers_choice(){
        this.computer_random = Math.floor(Math.random() * this.correct_choices.length);
        this.computer_choice = this.correct_choices[this.computer_random];
    }

    check_outcome(){
        if (this.user === this.computer_choice){
            console.log("correct")
        }
        else{
            console.log("wrong")
        }
    }

    show_outcome(){
        console.log("user: ", this.user)
        console.log("computer: ", this.computer_choice)
    }
}

if (require.main === module){
    try {
        let toss_game = new TossGame();
        toss_game.users_choice();
        toss_game.computers_choice();
        toss_game.check_outcome();
        toss_game.show_outcome();
    }
    catch (error) {
        console.error(error)
    }
}