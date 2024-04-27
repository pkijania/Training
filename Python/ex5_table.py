# 5. Create a table of n columns and n rows and count the sum of all it's elements. Paste all data into a file and print them in terminal

class Table:
    def __init__(self):
        self.table = self.file_table = []
        self.sum = 0
        self.path = r"D:\Programy\Github\Training\Python\Files_for_python_exercises\table.txt"

    def type_data(self):
        self.row = int(input("How many rows? "))
        self.column = int(input("How many columns? "))

    def create_table(self):
        for i in range(self.row):
            digit = int(input("Type a digit: "))
            self.table.append([digit] * self.column)

    def sum_of_elements(self):
        for i in range(self.row):
            for j in range(self.column):
                self.sum += self.table[i][j]

    def write_data_into_file(self):
        self.outfile = open(self.path, 'w')
        self.outfile.write(str(self.table) + "\nSum of elements in a table is: " + str(self.sum))
        self.outfile.close()

    def print_data_from_file(self):
        self.infile = open(self.path, 'r')
        with open(self.path) as file:
            self.file_table = eval(file.readline())
            self.file_sum = file.readline()
        print("\nData from a 'table.txt' file:")
        for i in range(self.row):
            for j in range(self.column):
                print(self.file_table[i][j], "", end = "")
            print()
        print("\nSum of elements in a table is: " + str(self.file_sum))
        
if __name__ == "__main__":
    try:
        table = Table()
        table.type_data()
        table.create_table()
        table.sum_of_elements()
        table.write_data_into_file()
        table.print_data_from_file()
    except Exception as error:
        print(f"Error!!, program shut down due to {error}")