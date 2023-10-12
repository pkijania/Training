class Lists_exercices:
    def __init__(self, list):
        self.list = list

    # Display reversed list
    def Reverse(self, list):
        n = len(list)
        new_list = []
        for i in range(1,n+1):
            new_list.append(list[-i])
        return "Old list is " + str(list), "new list is " + str(new_list)

    # Min and max in a list
    def MinMax(self, list):
        min = 0
        max = 0
        n = len(list)
        for i in range(0,n):
            if list[i] > max or max == 0:
                max = list[i]
            if list[i] < min or min == 0:
                min = list[i]
        return "Min is " + str(min), "max is " + str(max)
    
    # Sorting elements in a list
    def Sort(self, list):
        n = len(list)
        for j in range(0,n):
            for i in range(0,n-1):
                if list[i] > list[i+1]:
                    list[i],list[i+1] = list[i+1],list[i]
        return "Sorted list: " + str(list)

    # Sum of 2 elements
    def Sum(self):
        x = int(input("Type a number: "))
        y = int(input("Type a 2 number: "))
        return x + y

    # Sum of 2 elements
    def Sum_1(self, x, y):
        return x + y

    # Addition of n number of elements
    def Sum_list(self):
        n = int(input("how many digits? "))
        sum = int(0)
        for i in range(0,n):
            x = int(input("Type a digit: "))
            sum = sum + x
        return sum

    # Check if a word or a number is a palindrome
    def Palindrome(self, list):
        n = len(list)
        for i in range(0,int(n/2)):
            if list[i] != list[n-i-1]:
                return False
        return True
    
    # Create and display a table of 4 columns and 3 rows and count the sum of all it's elements
    def TableSum(self):
        n, m = 3, 4
        list = []
        for i in range(n):
            list.append([10] * m)
        
        print("Table:")
        for i in range(len(list)):
            for j in range(len(list) + 1):
                print(list[i][j], end = ' ')
            print()

        print()
        sum = 0
        for i in range(0,m):
            for j in range(0,n):
                sum = sum + list[i-1][j-1]
        print("Sum of elements in a table is: " + str(sum))

var = Lists_exercices([1,2,3,4])
print(var.Reverse([1,2,3,4]))

print()

var_2 = Lists_exercices([1,2,3,4])
print(var_2.MinMax([1,2,3,4]))

print()

var_3 = Lists_exercices([1,3,2,5,4])
print(var_3.Sort([1,3,2,5,4]))

print()

var_4 = Lists_exercices([1,2,3,4])
print(var_4.TableSum())
