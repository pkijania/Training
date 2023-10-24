# 10. Create cashmachine - withdraws only 50,20 and 10 zł, max account balance can be 500 zł

def cashmachine():
    choice = 0
    balance = int(input("Enter account balance between 0 and 500 zl : "))
    while(choice != 4):
        print("\nMenu")
        print("1 = Show account balance:")
        print("2 = Deposit money:")
        print("3 = Pay out money:")
        print("4 = Exit:")
        choice = int(input("\nChoose action:"))
        if(choice == 1):
            print("\nAccount balance:", balance)
        elif(choice == 2):
            if(balance == 500):
                print("Cant deposit more money. Account balance cannot exceed 500 zł")
            else:
                action = int(input("How much money to deposit?:"))
                if(action % 50 == 0):
                    balance = balance + action
                elif(action % 20 == 0):
                    balance = balance + action
                elif(action % 10 == 0):
                    balance = balance + action
                else:
                    print("Cashmachine depisits only bank notes of 50,20 and 10 zł value. Enter different value.")
        elif(choice == 3):
            if(balance < 10):
                print("Lack of funds on an account")
            else:
                action = int(input("How much money to pay out ?:"))
                if(action % 50 == 0):
                    balance = balance - action
                elif(action % 20 == 0):
                    balance = balance - action
                elif(action % 10 == 0):
                    balance = balance - action
                else:
                    print("Cashmachine pays out only bank notes of 50,20 and 10 zł value. Enter different value.")
        elif(choice == 4):
            print("Logged out")
            break
        else:
            print("Wrong action")
cashmachine()