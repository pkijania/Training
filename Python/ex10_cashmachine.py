# 10. Create cashmachine that withdraws only values of 50, 20 and 10 and has a max account balance of 500

class Validators:
    def choice():
        choice = input("Choose an action: ")
        while not choice.isdigit():
            choice = input("Wrong action. Choose a correct action: ")
        return int(choice)
    
    def balance():
        balance = input("Enter an amount of account balance between 10 and 500 zł: ")
        while not balance.isdigit():
            balance = input("Wrong amount of money. Enter a correct amount of account balance between 10 and 500 zł: ")
        return int(balance)
    
    def action_deposit():
        action_deposit = input("How much money to deposit?: ")
        while not action_deposit.isdigit():
            action_deposit = input("Wrong amount of money. Enter a correct amount of money: ")
        return int(action_deposit)
    
    def action_withdraw():
        action_withdraw = input("How much money to withdraw?: ")
        while not action_withdraw.isdigit():
            action_withdraw = input("Wrong amount of money. Enter a correct amount of money: ")
        return int(action_withdraw)

class Actions:
    def print(balance):
        print("\nAccount balance is:", balance)
        return balance
    
    def deposit(balance):
        if balance >= 500:
            print("Cant deposit more money. Account balance cannot exceed 500 zł")
        else:    
            action = Validators.action_deposit()
            if (action + balance) > 500:
                print("Cant deposit more money. Account balance cannot exceed 500 zł")
            else:
                if action % 50 == 0:
                    balance += action
                elif action % 20 == 0:
                    balance += action
                elif action % 10 == 0:
                    balance += action
                else:
                    print("Cashmachine deposits only bank notes of 50, 20 and 10 zł value. Enter a different value.") 
            return balance
       
    def withdraw(balance):
        if balance <= 10:
            print("Cant pay out more money. Account balance cannot be lower than 10 zł")
        else:
            action = Validators.action_withdraw()
            if (balance - action) < 10:
                print("Cant pay out more money. Account balance be lower than 10 zł")
            else:
                if action % 50 == 0:  
                    balance -= action
                elif action % 20 == 0:
                    balance -= action
                elif action % 10 == 0:
                    balance -= action
                else:
                    print("Cashmachine pays out only bank notes of 50, 20 and 10 zł value. Enter a different value.")
            return balance
    
    def exit(balance):
        print("\nLogged out")
        print("Balance is:", balance, "zł")
        return balance

if __name__ == "__main__":
    choice = 0
    balance = 0
    while balance < 10 or balance > 500:
        balance = Validators.balance()
        if balance < 10 or balance > 500:
            print("Wrong amount of account balance")
        else:
            while True:
                print("\nMenu")
                print("1 = Show account balance")
                print("2 = Deposit money")
                print("3 = Pay out money")
                print("4 = Exit")
                choice = Validators.choice()
                match choice:
                    case 1:
                        balance = Actions.print(balance)
                    case 2:
                        balance = Actions.deposit(balance)
                    case 3:
                        balance = Actions.withdraw(balance) 
                    case 4:
                        balance = Actions.exit(balance)
                        break
                    case _:
                        print("Wrong action")