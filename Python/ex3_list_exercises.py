# 3. Create menu with list exercises - Sort numbers, find min and max value, count the amount of even and odd numbers, reverse values, check if a word or a number is a palindrome

class Validators:
    def digit(prompt, error):
        input_digit = input(prompt)
        while not input_digit.isdigit():
            input_digit = input(error)
        return int(input_digit)

    def new_list():
        list = []
        which_list = "0"
        while (which_list != "default" or "custom"):
            which_list = str(input("Use default list (1, 2, 0, 2, 1) or custom list? (default/custom): "))
            if which_list == "default":
                list = [1, 2, 0, 2, 1]
                break
            elif which_list == "custom":
                list_length = Validators.digit("How many digits?: ", "Wrong digit, please type a correct digit: ")
                for i in range(list_length):
                    number = Validators.digit("Type a digit: ", "Wrong digit, please type a correct digit: ")
                    list.append(number)
                break
            else:
                print("Wrong input. Input should be (default) or (custom)")
        return list

class List_exercises:
    def sort(list):
        end = False
        for i in range (len(list)):
            for j in range (0, len(list) - 1):
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
                    end = True
            if end == False: 
                break
        return list

    def min_max(list):
        max = list[0]
        min = list[0]
        for i in range (len(list)):
            if list[i] < min:
                min = list[i]
            if list[i] > max:
                max = list[i]
        return min, max

    def even_odd(list):
        even = 0
        odd = 0
        for i in range(0, len(list)):
            if list[i] % 2 == 0:
                even += 1
            if list[i] % 2 != 0:
                odd += 1
        return even, odd

    def reverse(list):
        new_list = []
        for i in range(1, len(list) + 1):
            new_list.append(list[-i])
        return new_list

    def palindrome(list):
        length = len(list)
        outcome = True
        for i in range(0, int(length / 2)):
            if list[i] != list[length - i - 1]:
                outcome = False
        return outcome

if __name__ == "__main__":
    try:
        menu_first = "\nWhat would you like to do?: "
        menu_second = "Wrong action, choose again: "
        menu_third = "Your list is:"
        list = Validators.new_list()
        while True:
            print("\nMenu:")
            print("1 = Show info about a list")
            print("2 = Modify a list")
            print("3 = Exit\n")
            print(menu_third, list)
            choice = Validators.digit(menu_first, menu_second)
            match choice:
                case 1:
                    while True:
                        print("\nMenu:")
                        print("1 = Print max and min value from a list")
                        print("2 = Print number of even and odd digits from a list")
                        print("3 = Check if a list is a palindrome")
                        print("4 = Go back\n")
                        print(menu_third, list)
                        choice_info = Validators.digit(menu_first, menu_second)
                        match choice_info:
                            case 1:
                                print("\nMin and max values are:", List_exercises.min_max(list))
                            case 2:
                                print("\nNumber of even and odd values is:", List_exercises.even_odd(list))
                            case 3:
                                if List_exercises.palindrome(list):
                                    print("\nIt is a palindrome")
                                else:
                                    print("\nIt is not a palindrome")
                            case 4:
                                break
                            case _:
                                print("Wrong action")
                case 2:
                    while True:
                        print("\nMenu:")
                        print("1 = Create a new list")
                        print("2 = Sort a list")
                        print("3 = Reverse a list")
                        print("4 = Go back\n")
                        print(menu_third, list)
                        choice_modify = Validators.digit(menu_first, menu_second)
                        match choice_modify:
                            case 1:
                                list = Validators.new_list()
                            case 2:
                                list = List_exercises.sort(list)
                            case 3:
                                list = List_exercises.reverse(list)
                            case 4:
                                break
                            case _:
                                print("Wrong action")
                case 3:
                    break
                case _:
                    print("Wrong action")
        print("End")
    except Exception as wrong_user:
        print(f"Error!!, program shut down due to {wrong_user}")