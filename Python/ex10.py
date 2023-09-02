# 10. Cashmachine - withdraws only 50,20 and 10 zł, max account balance can be 500 zł
def bankomat():
    x = 0
    balance = int(input("Podaj stan konta pomiedzy 0 a 500 zl : "))
    while(x != 4):
        print("\nMenu")
        print("1 = Wypisz stan konta:")
        print("2 = Wplac pieniadze:")
        print("3 = Wyplac pieniadze:")
        print("4 = Wyjdz:")
        x = int(input("\nWybierz akcje:"))
        if(x == 1):
            print("\nStan konta:", balance)
        elif(x == 2):
            if(balance == 500):
                print("Nie mozna wplacic wiecej pieniedzy na konto. Stan konta nie moze przekraczac 500 zl")
            else:
                action = int(input("Ile pieniędzy wplacic?:"))
                if(action % 50 == 0):
                    balance = balance + action
                elif(action % 20 == 0):
                    balance = balance + action
                elif(action % 10 == 0):
                    balance = balance + action
                else:
                    print("Bankomat przyjmuje tylko banknoty o nominalach: 50,20,10 zł. Podaj inna wartosc.")
        elif(x == 3):
            if(balance < 10):
                print("Brak srodkow na koncie")
            else:
                action = int(input("Ile pieniędzy wydać?:"))
                if(action % 50 == 0):
                    balance = balance - action
                elif(action % 20 == 0):
                    balance = balance - action
                elif(action % 10 == 0):
                    balance = balance - action
                else:
                    print("Bankomat wydaje tylko banknoty o nominalach: 50,20,10 zł. Podaj inna wartosc.")
        elif(x == 4):
            print("Wylogowano")
            break
        else:
            print("Zla akcja")
bankomat()