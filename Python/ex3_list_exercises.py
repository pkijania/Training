# 3. Create menu with list exercises - Sort numbers, find min and max value, count the amount of even and odd numbers, reverse values, check if a word or a number is a palindrome

def digit(prompt, error):
    input_digit = input(prompt)
    while not input_digit.isdigit():
        input_digit = input(error)
    return int(input_digit)

class ListExercises:
    def __init__(self):
        self.list = []

    def new_list(self):
        which_list = "0"
        while (which_list != "default" or "custom"):
            which_list = str(input("Use default list (1, 2, 0, 2, 1) or custom list? (default/custom): "))
            if which_list == "default":
                self.list = [1, 2, 0, 2, 1]
                break
            elif which_list == "custom":
                new_list = []
                list_length = digit("How many digits?: ", "Wrong digit, please type a correct digit: ")
                for i in range(list_length):
                    number = digit("Type a digit: ", "Wrong digit, please type a correct digit: ")
                    new_list.append(number)
                self.list = new_list
                break
            else:
                print("Wrong input. Input should be (default) or (custom)")

    def sort(self):
        end = False
        for i in range (len(self.list)):
            for j in range (0, len(self.list) - 1):
                if self.list[j] > self.list[j + 1]:
                    self.list[j], self.list[j + 1] = self.list[j + 1], self.list[j]
                    end = True
            if end == False: 
                break

    def reverse(self):
        new_list = []
        for i in range(1, len(self.list) + 1):
            new_list.append(self.list[-i])
        self.list = new_list

    def min_max(self):
        max = self.list[0]
        min = self.list[0]
        for i in range (len(self.list)):
            if self.list[i] < min:
                min = self.list[i]
            if self.list[i] > max:
                max = self.list[i]
        return min, max

    def even_odd(self):
        even = 0
        odd = 0
        for i in range(0, len(self.list)):
            if self.list[i] % 2 == 0:
                even += 1
            if self.list[i] % 2 != 0:
                odd += 1
        return even, odd

    def palindrome(self):
        length = len(self.list)
        outcome = True
        for i in range(0, int(length / 2)):
            if self.list[i] != self.list[length - i - 1]:
                outcome = False
        return outcome

if __name__ == "__main__":
    try:
        menu_first = "\nWhat would you like to do?: "
        menu_second = "Wrong action, choose again: "
        menu_third = "Your list is:"
        list_exercises = ListExercises()
        list_exercises.new_list()
        while True:
            print("\nMenu:\n1 = Show info about a list\n2 = Modify a list\n3 = Exit\n")
            print(menu_third, list_exercises.list)
            choice = digit(menu_first, menu_second)
            match choice:
                case 1:
                    while True:
                        print("\nMenu:\n1 = Print max and min value from a list\n2 = Print number of even and odd digits from a list\n3 = Check if a list is a palindrome\n4 = Go back\n")
                        print(menu_third, list_exercises.list)
                        choice_info = digit(menu_first, menu_second)
                        match choice_info:
                            case 1:
                                print("\nMin and max values are:", list_exercises.min_max())
                            case 2:
                                print("\nNumber of even and odd values is:", list_exercises.even_odd())
                            case 3:
                                if list_exercises.palindrome():
                                    print("\nIt is a palindrome")
                                else:
                                    print("\nIt is not a palindrome")
                            case 4:
                                break
                            case _:
                                print("Wrong action")
                case 2:
                    while True:
                        print("\nMenu:\n1 = Create a new list\n2 = Sort a list\n3 = Reverse a list\n4 = Go back\n")
                        print(menu_third, list_exercises.list)
                        choice_modify = digit(menu_first, menu_second)
                        match choice_modify:
                            case 1:
                                list_exercises.new_list()
                            case 2:
                                list_exercises.sort()
                            case 3:
                                list_exercises.reverse()
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