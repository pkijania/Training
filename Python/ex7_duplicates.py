# 7. Create a list with random numbers and delete duplicates

import random

class DeleteDuplicates:
    def __init__(self):
        print("This program creates a list and then deletes all duplicates")

    def create_list(self):
        self.old_list = []
        list_length = int(input("How many digits? "))
        for i in range(list_length):
            self.old_list.append(random.randint(0, list_length))

    def create_set(self):
        self.temp_set = set()
        for item in self.old_list:
            self.temp_set.add(item)
    
    def convert_to_list(self):
        self.new_list = list(self.temp_set)

    def show_outcome(self):
        if len(self.old_list) == len(self.new_list):
            print("List without duplicates:", self.new_list)
        else:
            print("List:", self.old_list, "List without duplicates:", self.new_list)

if __name__ == "__main__":
    try:
        delete_duplicates = DeleteDuplicates()
        delete_duplicates.create_list()
        delete_duplicates.create_set()
        delete_duplicates.convert_to_list()
        delete_duplicates.show_outcome()
    except Exception as error:
        print(f"Error!!, program shut down due to {error}")