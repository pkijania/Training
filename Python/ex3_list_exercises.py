# 3. Create menu with List exercises - Sort numbers , find min and max value, count the amount of even and odd numbers, reverse values, check if a word or a number is a palindrome

class Validators:
    def choice():
        choice = input("What would you like to do?: ")
        while not choice.isdigit():
            choice = input("Wrong action, choose again: ")
        return int(choice)
    
    def digit():
        digit = input("Type a digit: ")
        while not digit.isdigit():
            digit = input("Wrong digit, please type a correct digit: ")
        return int(digit)

    def length():
        length = input("How many digits?: ")
        while not length.isdigit():
            length = input("Wrong digit, please type a correct digit: ")
        return int(length)
    
    def new_list():
        list = []
        which_list = "0"
        while (which_list != "d" or "c"):
            which_list = str(input("Use default list (1, 2, 0, 2, 1) or custom list? (d/c): "))
            if which_list == "d":
                list = [1, 2, 0, 2, 1]
                break
            elif which_list == "c":
                list_length = Validators.length()
                for i in range(list_length):
                    number = Validators.digit()
                    list.append(number)
                break
            else:
                print("Wrong input. Input should be (d) or (c)")
        return list

class List_exercises:
    def sort(list):
        end = False
        for i in range (len(list)):
            for j in range (0, len(list) - 1):
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
                    end = True
            if end == False: break
        return list

    def MinMax(list):
        max = list[0]
        min = list[0]
        for i in range (len(list)):
            if list[i] < min:
                min = list[i]
            if list[i] > max:
                max = list[i]
        print(min, "min")
        print(max, "max")

    def even_odd(list):
        even = 0
        odd = 0
        for i in range(0, len(list)):
            if list[i] % 2 == 0:
                even += 1
            if list[i] % 2 != 0:
                odd += 1
        print("number of even digits", even)
        print("number of odd digits", odd)
        return even, odd

    def reverse(list):
        new_list = []
        for i in range(1, len(list) + 1):
            new_list.append(list[-i])
        return new_list

    def palindrome(list):
        length = len(list)
        outcome = True
        for i in range(0, int(length/2)):
            if list[i] != list[length - i - 1]:
                outcome = False
        if outcome:
            print("It is a palindrome")
        else:
            print("It is not a palindrome")

if __name__ == "__main__":
    list = Validators.new_list()
    while True:
        print("\nMenu:")
        print("1 = Print a list")
        print("2 = Sort a list")
        print("3 = Print max and min value from a list")
        print("4 = Print number of even and odd digits from a list")
        print("5 = Reverse a list")
        print("6 = Check if a list is a palindrome")
        print("7 = Exit")
        choice = Validators.choice()
        match choice:
            case 1:
                print("Your list is:", list)
            case 2:
                print(List_exercises.sort(list))
            case 3:
                List_exercises.MinMax(list)
            case 4:
                print(List_exercises.even_odd(list))
            case 5:
                print("Reversed list: ", List_exercises.reverse(list))
            case 6:
                List_exercises.palindrome(list)
            case 7:
                break
            case _:
                ("Wrong action")
    print("End")