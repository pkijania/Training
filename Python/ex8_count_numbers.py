# 8. Create a list with random numbers and count every number

import random
import operator

class CountNumbers:
    def __init__(self):
        print("This program creates list and counts its numbers")

    def create_list(self):
        self.list = []
        self.list_length = int(input("How many digits? "))
        for i in range(self.list_length):
            self.list.append(random.randint(0, self.list_length))
    
    def show_list(self):
        print("Your list is:", self.list)

    def create_dictionary(self):
        self.dictonary = {}
        for i in self.list:
            self.dictonary[i] = 0

    def count_numbers(self):
        for i in self.list:
            if self.dictonary[i] == 0:
                self.dictonary[i] = 1
            else:
                self.dictonary[i] = self.dictonary[i] + 1

    def get_outcome(self):
        self.sorted_dictionary = sorted(self.dictonary.items(), key = operator.itemgetter(0))
        return self.sorted_dictionary

if __name__ == "__main__":
    try:
        count_numbers = CountNumbers()
        count_numbers.create_list()
        count_numbers.create_dictionary()
        count_numbers.count_numbers()
        count_numbers.show_list()
        print("(Digit, number of digits)", count_numbers.get_outcome())
    except Exception as wrong_user:
        print(f"Error!!, program shut down due to {wrong_user}")