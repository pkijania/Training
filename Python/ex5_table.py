# 5. Create and display a table of n columns and n rows and count the sum of all it's elements

class Table:
    def __init__(self):
        self.list = []
        self.sum = 0

    def type_data(self):
        self.row = int(input("How many rows? "))
        self.column = int(input("How many columns? "))

    def create_table(self):
        for i in range(self.row):
            digit = int(input("Type a digit: "))
            self.list.append([digit] * self.column)
        print("\nTable:")

    def sum_of_elements(self):
        for i in range(self.row):
            for j in range(self.column):
                print(self.list[i][j], end = ' ')
                self.sum += self.list[i][j]
            print()
        print("\nSum of elements in a table is: " + str(self.sum))

if __name__ == "__main__":
    try:
        table = Table()
        table.type_data()
        table.create_table()
        table.sum_of_elements()
    except Exception as wrong_user:
        print(f"Error!!, program shut down due to {wrong_user}")