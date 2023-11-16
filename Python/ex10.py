# 10. Create cashmachine - withdraws only 50, 20 and 10 zł, account balance cannot exceed 500 zł or be lower than 10 zł

def cashmachine():
    choice = 0
    balance = 0
    while (balance < 10 or balance > 500):
            balance = int(input("Enter an amount of account balance between 10 and 500 zł: "))
            if (balance < 10 or balance > 500):
                print ("Wrong amount of account balance")
            else:
                while (choice != 4):

                    print("\nMenu")
                    print("1 = Show account balance:")
                    print("2 = Deposit money:")
                    print("3 = Pay out money:")
                    print("4 = Exit:")
                    choice = int(input("\nChoose action:"))

                    if (choice == 1):
                        print("\nAccount balance:", balance)

                    elif (choice == 2):
                        if (balance >= 500):
                            print("Cant deposit more money. Account balance cannot exceed 500 zł")
                        else:
                            action = int(input("How much money to deposit?: "))
                            if ((action + balance) > 500):
                                print("Account balance cannot exceed 500 zł")
                            else:
                                if (action % 50 == 0):
                                    balance = balance + action
                                elif (action % 20 == 0):
                                    balance = balance + action
                                elif (action % 10 == 0):
                                    balance = balance + action
                                else:
                                    print("Cashmachine deposits only bank notes of 50, 20 and 10 zł value. Enter a different value.")

                    elif (choice == 3):
                        if (balance <= 10):
                            print("Cant pay out more money. Account balance cannot be lower than 10 zł")
                        else:
                            action = int(input("How much money to pay out ?: "))
                            if ((balance - action) < 10):
                                print("Account balance be lower than 10 zł")
                            else:
                                if (action % 50 == 0):  
                                    balance = balance - action
                                elif (action % 20 == 0):
                                    balance = balance - action
                                elif (action % 10 == 0):
                                    balance = balance - action
                                else:
                                    print("Cashmachine pays out only bank notes of 50, 20 and 10 zł value. Enter a different value.")
                    elif (choice == 4):

                        print("Logged out")
                        break
                    else:
                        print("Wrong action")
cashmachine()