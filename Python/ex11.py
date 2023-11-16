# 11. Class containing some of previous exercises and two simple methods for creating tables

class Lists_exercises:
    
    def __init__(self, list):
        self.list = list

    # Min and max in a list
    def MinMax(self, list):
        min = 0
        max = 0
        length = len(list)
        for i in range(0, length):
            if list[i] > max or max == 0:
                max = list[i]
            if list[i] < min or min == 0:
                min = list[i]
        return "Min is " + str(min), "max is " + str(max)
    
    # Sorting elements in a list
    def Sort(self, list):
        length = len(list)
        for j in range(0, length):
            for i in range(0, length - 1):
                if list[i] > list[i+1]:
                    list[i],list[i+1] = list[i+1],list[i]
        return "Sorted list: " + str(list)

    # Sum of 2 elements
    def Sum(self):
        first_number = int(input("Type a number: "))
        second_number = int(input("Type a 2 number: "))
        return first_number + second_number

    # Sum of 2 elements
    def Sum_1(self, first, second):
        return first + second

    # Addition of n number of elements
    def Sum_list(self):
        length = int(input("how many digits? "))
        sum = int(0)
        for i in range(0, length):
            x = int(input("Type a digit: "))
            sum = sum + x
        return sum

    # Check if a word or a number is a palindrome
    def Palindrome(self, list):
        length = len(list)
        for i in range(0,int(length/2)):
            if list[i] != list[length-i-1]:
                return False
        return True

# Inheritance
class Table_exercise(Lists_exercises):

    # Display reversed list
    def Reverse(self, list):
        length = len(list)
        new_list = []
        for i in range(1, length+1):
            new_list.append(list[-i])
        return "Old list is " + str(list), "new list is " + str(new_list)

    # Create and display a table of 4 columns and 3 rows and count the sum of all it's elements
    def TableSum(self):
        row, column = 3, 4
        list = []
        for i in range(row):
            list.append([10] * column)
        
        print("Table:")
        for i in range(len(list)):
            for j in range(len(list) + 1):
                print(list[i][j], end = ' ')
            print()

        print()
        sum = 0
        for i in range(0, column):
            for j in range(0,row):
                sum = sum + list[i-1][j-1]
        print("Sum of elements in a table is: " + str(sum))

var = Lists_exercises([1,2,3,4])
print(var.MinMax([1,2,3,4]))

print()

var_2 = Lists_exercises([1,3,2,5,4])
print(var_2.Sort([1,3,2,5,4]))

print()

var3 = Table_exercise([1,2,3,4])
print(var3.Reverse([1,2,3,4]))

print()

var_4 = Table_exercise([1,2,3,4])
print(var_4.TableSum())