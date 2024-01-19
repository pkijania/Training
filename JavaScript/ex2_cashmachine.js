// 2. Create cashmachine that withdraws only values of 50, 20 and 10 and has a max account balance of 500

const prompt = require ("prompt-sync")();

function digit(prompt_text, error){
    let input_digit = prompt(prompt_text);
    while (Number.isInteger(+input_digit) !== true){
        input_digit = prompt(error);
    }
    return parseInt(input_digit, 10);
}

class Account{
    constructor(){
        this.balance = 0;
    }

    print(){
        console.log("\nAccount balance:", this.balance)
    }

    deposit(){
        let action = 0;
        if (this.balance >= 500){
            console.log("Cant deposit more money. Account balance cannot exceed 500 zł")
        }
        else{
            action = digit("How much money to deposit?: ", "Wrong amount of money. Enter a correct amount of money: ");
            if ((action + this.balance) > 500){
                console.log("Account balance cannot exceed 500 zł");
            }
            else {
                if (action % 50 === 0){
                    this.balance += action;
                }
                else if (action % 20 === 0){
                    this.balance += action;
                }
                else if (action % 10 === 0 ){
                    this.balance += action;
                }
                else {
                    console.log("Cashmachine deposits only bank notes of 50, 20 and 10 zł value. Enter a different value.")
                }
            }
        }
    }

    withdraw(){
        let action = 0;
        if (this.balance <= 10){
            console.log("Cant pay out more money. Account balance cannot be lower than 10 zł")
        }
        else{
            action = digit("How much money to withdraw?: ", "Wrong amount of money. Enter a correct amount of money: ");
            if ((this.balance - action) < 10){
                console.log("Account balance be lower than 10 zł");
            }
            else {
                if (action % 50 === 0){
                    this.balance -= action;
                }
                else if (action % 20 === 0){
                    this.balance -= action;
                }
                else if (action % 10 === 0 ){
                    this.balance -= action;
                }
                else {
                    console.log("Cashmachine pays out only bank notes of 50, 20 and 10 zł value. Enter a different value.")
                }
            }
        }
    }

    exit(){
        console.log("\nLogged out")
        console.log("Balance is:", this.balance, "zł")
    }
}

if (require.main === module){
    try {
        const account = new Account();
        let choice = 0;
        while (account.balance < 10 || account.balance > 500){
            account.balance = digit("Enter an amount of account balance between 10 and 500 zł: ", "Wrong amount of money. Enter a correct amount of account balance between 10 and 500 zł: ");
            if (account.balance < 10 || account.balance > 500){
                console.log("Wrong amount of account balance");
            }
            else {
                while (true){
                    console.log("\nMenu");
                    console.log("1 = Show account balance:");
                    console.log("2 = Deposit money:");
                    console.log("3 = Pay out money:");
                    console.log("4 = Exit:");
                    choice = digit("Choose an action: ", "Wrong action. Choose a correct action: ");
                    switch (choice){
                        case (1):
                            account.print();
                            break;
                        case (2):
                            account.deposit();
                            break;
                        case (3):
                            account.withdraw();
                            break;
                        case (4):
                            account.exit();
                            return account.balance;
                        default:
                            console.log("Wrong action");
                            break;                    
                    }
                }
            }
        }
    }
    catch (error) {
        console.error(error)
    }
}