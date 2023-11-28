// 10. Create cashmachine - withdraws only 50, 20 and 10 zł, account balance cannot exceed 500 zł or be lower than 10 zł

const prompt = require ("prompt-sync")();

function cashmachine(){
    let choice = 0;
    let balance = 0;
    let action = 0;
    while (balance < 10 || balance > 500){
        balance = parseInt(prompt("Enter account balance between 10 and 500 zł: "), 10);
        if (balance < 10 || balance > 500){
            console.log("Wrong amount of account balance");
        }
        else {
            while (choice != 4){

                console.log("\nMenu");
                console.log("1 = Show account balance:");
                console.log("2 = Deposit money:");
                console.log("3 = Pay out money:");
                console.log("4 = Exit:");
                choice = parseInt(prompt("\nChoose action:"), 10);
        
                if (choice === 1){
                    console.log("\nAccount balance:", balance);
                }
        
                else if (choice === 2){
                    if (balance >= 500){
                        console.log("Cant deposit more money. Account balance cannot exceed 500 zł")
                    }
                    else {
                        action = parseInt(prompt("How much money to deposit?: "), 10);
                        if ((action + balance) > 500){
                            console.log("Account balance cannot exceed 500 zł");
                        }
                        else {
                            if (action % 50 === 0){
                                balance = balance + action;
                            }
                            else if (action % 20 === 0){
                                balance = balance + action;
                            }
                            else if (action % 10 === 0 ){
                                balance = balance + action;
                            }
                            else {
                                console.log("Cashmachine deposits only bank notes of 50, 20 and 10 zł value. Enter a different value.")
                            }
                        }
                    }
                }
        
                else if (choice === 3){
                    if (balance <= 10){
                        console.log("Cant pay out more money. Account balance cannot be lower than 10 zł")
                    }
                    else {
                        action = parseInt(prompt("How much money to pay out?: "), 10)
                        if ((balance - action) < 10){
                            console.log("Account balance be lower than 10 zł");
                        }
                        else {
                            if (action % 50 === 0){
                                balance = balance - action;
                            }
                            else if (action % 20 === 0){
                                balance = balance - action;
                            }
                            else if (action % 10 === 0 ){
                                balance = balance - action;
                            }
                            else {
                                console.log("Cashmachine pays out only bank notes of 50, 20 and 10 zł value. Enter a different value.")
                            }
                        }
                    }
                }
        
                else if (choice === 4){
                    console.log("Logged out");
                    break;
                }
                else {
                    console.log("Wrong action");
                }
            }
        }
    }
}

cashmachine()