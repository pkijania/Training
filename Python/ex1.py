-- # 1. Menu with addition, subtraction and printing numbers functions
def dodawanie():
    sum = 0
    n = int(input("Ile liczb?: "))
    print("Wpisz",n, "liczb(y): ")
    for i in range(n):
        c = int(input("Wpisz liczbę: "))
        sum = sum + c
    print("Suma to: ", sum)

def odejmowanie():
    x = int(input("Wpisz 1 liczbę: "))
    y = int(input("Wpisz 2 liczbę: "))
    print("twoja liczba to:", x - y)

def wypisywanie(*z):
    print(1,2,3,4,5)

x = 0
while x !=4:
    print("\nMenu")
    print("1 = dodanie n liczb")
    print("2 = odejmowanie 2 liczb")
    print("3 = wypisywanie 5 liczb")
    print("4 = wyjście z menu\n")
    x = int(input("\nCo chcesz zrobić?: "))
    match x:
        case 1:
            dodawanie()
        case 2:
            odejmowanie()
        case 3:
            wypisywanie()
        case 4:
            break
print("Koniec")
