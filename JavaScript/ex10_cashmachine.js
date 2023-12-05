// 10. Create cashmachine - withdraws only 50, 20 and 10 zł, account balance cannot exceed 500 zł or be lower than 10 zł

const prompt = require ("prompt-sync")();

class Validators{
    action_balance(){
        let action_balance = prompt("Enter an amount of account balance between 10 and 500 zł: ");
        while (Number.isInteger(+action_balance) !== true){
            action_balance = prompt("Wrong amount of money. Enter a correct amount of account balance between 10 and 500 zł: ");
        }
        return parseInt(action_balance, 10);
    }

    action_choice(){
        let action_choice = prompt("Choose an action: ");
        while (Number.isInteger(+action_choice) !== true){
            action_choice = prompt("Wrong action. Choose a correct action: ");
        }
        return parseInt(action_choice, 10);
    }

    action_deposit(){
        let action_deposit = prompt("How much money to deposit?: ");
        while (Number.isInteger(+action_deposit) !== true){
            action_deposit = prompt("Wrong amount of money. Enter a correct amount of money: ");
        }
        return parseInt(action_deposit, 10);
    }

    action_withdraw(){
        let action_withdraw = prompt("How much money to withdraw?: ");
        while (Number.isInteger(+action_withdraw) !== true){
            action_withdraw = prompt("Wrong amount of money. Enter a correct amount of money: ");
        }
        return parseInt(action_withdraw, 10);
    }   
}

class Actions{
    print(balance){
        console.log("\nAccount balance:", balance)
        return parseInt(balance, 10);
    }

    deposit(balance){
        const validators = new Validators();
        let action = 0;
        if (balance >= 500){
            console.log("Cant deposit more money. Account balance cannot exceed 500 zł")
        }
        else{
            action = validators.action_deposit();
            if ((action + balance) > 500){
                console.log("Account balance cannot exceed 500 zł");
            }
            else {
                if (action % 50 === 0){
                    balance += action;
                }
                else if (action % 20 === 0){
                    balance += action;
                }
                else if (action % 10 === 0 ){
                    balance += action;
                }
                else {
                    console.log("Cashmachine deposits only bank notes of 50, 20 and 10 zł value. Enter a different value.")
                }
            }
        }
        return parseInt(balance, 10);
    }

    withdraw(balance){
        const validators = new Validators();
        let action = 0;
        if (balance <= 10){
            console.log("Cant pay out more money. Account balance cannot be lower than 10 zł")
        }
        else{
            action = validators.action_withdraw();
            if ((balance - action) < 10){
                console.log("Account balance be lower than 10 zł");
            }
            else {
                if (action % 50 === 0){
                    balance -= action;
                }
                else if (action % 20 === 0){
                    balance -= action;
                }
                else if (action % 10 === 0 ){
                    balance -= action;
                }
                else {
                    console.log("Cashmachine pays out only bank notes of 50, 20 and 10 zł value. Enter a different value.")
                }
            }
        }
        return parseInt(balance, 10);
    }

    exit(balance){
        console.log("\nLogged out")
        console.log("Balance is:", balance, "zł")
        return parseInt(balance, 10);
    }
}

if (require.main === module){
    const validators = new Validators();
    const actions = new Actions();
    let choice = 0;
    let balance = 0;
    while (balance < 10 || balance > 500){
        balance = validators.action_balance();
        if (balance < 10 || balance > 500){
            console.log("Wrong amount of account balance");
        }
        else {
            while (true){
                console.log("\nMenu");
                console.log("1 = Show account balance:");
                console.log("2 = Deposit money:");
                console.log("3 = Pay out money:");
                console.log("4 = Exit:");
                choice = validators.action_choice();
                switch (choice){
                    case (1):
                        balance = actions.print(balance);
                        break;
                    case (2):
                        balance = actions.deposit(balance);
                        break;
                    case (3):
                        balance = actions.withdraw(balance);
                        break;
                    case (4):
                        balance = actions.exit(balance);
                        return balance;
                    default:
                        console.log("Wrong action");
                        break;                    
                }
            }
        }
    }
}