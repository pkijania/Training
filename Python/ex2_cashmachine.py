# 2. Create cashmachine that withdraws only values of 50, 20 and 10 and has a max account balance of 500

class Validators:
    def digit(prompt, error):
        input_digit = input(prompt)
        while not input_digit.isdigit():
            input_digit = input(error)
        return int(input_digit)

class Account:
    def __init__(self):
        self.balance = 0

    def print(self):
        print("\nAccount balance is:", self.balance)
    
    def deposit(self):
        if self.balance >= 500:
            print("Cant deposit more money. Account balance cannot exceed 500 zł")
        else:    
            action = Validators.digit("How much money to deposit?: ", "Wrong amount of money. Enter a correct amount of money: ")
            if (action + self.balance) > 500:
                print("Cant deposit more money. Account balance cannot exceed 500 zł")
            else:
                if action % 50 == 0:
                    self.balance += action
                elif action % 20 == 0:
                    self.balance += action
                elif action % 10 == 0:
                    self.balance += action
                else:
                    print("Cashmachine deposits only bank notes of 50, 20 and 10 zł value. Enter a different value.") 
       
    def withdraw(self):
        if self.balance <= 10:
            print("Cant pay out more money. Account balance cannot be lower than 10 zł")
        else:
            action = Validators.digit("How much money to withdraw?: ", "Wrong amount of money. Enter a correct amount of money: ")
            if (self.balance - action) < 10:
                print("Cant pay out more money. Account balance be lower than 10 zł")
            else:
                if action % 50 == 0:  
                    self.balance -= action
                elif action % 20 == 0:
                    self.balance -= action
                elif action % 10 == 0:
                    self.balance -= action
                else:
                    print("Cashmachine pays out only bank notes of 50, 20 and 10 zł value. Enter a different value.")
    
    def exit(self):
        print("\nLogged out")
        print("Balance is:", self.balance, "zł")

if __name__ == "__main__":
    try:
        choice = 0
        account = Account()
        while account.balance < 10 or account.balance > 500:
            account.balance = Validators.digit("Enter an amount of account balance between 10 and 500 zł: ", "Wrong amount of money. Enter a correct amount of account balance between 10 and 500 zł: ")
            if account.balance < 10 or account.balance > 500:
                print("Wrong amount of account balance")
            else:
                while True:
                    print("\nMenu")
                    print("1 = Show account balance")
                    print("2 = Deposit money")
                    print("3 = Pay out money")
                    print("4 = Exit")
                    choice = Validators.digit("Choose an action: ", "Wrong action. Choose a correct action: ")
                    match choice:
                        case 1:
                            account.print()
                        case 2:
                            account.deposit()
                        case 3:
                            account.withdraw() 
                        case 4:
                            account.exit()
                            break
                        case _:
                            print("Wrong action")
    except Exception as wrong_user:
        print(f"Error!!, program shut down due to {wrong_user}")