# 5. Create and display a table of n columns and n rows and count the sum of all it's elements

if __name__ == "__main__":
    row = int(input("How many rows? "))
    column = int(input("How many columns? "))
    list = []
    sum = 0
    for i in range(row):
        digit = int(input("Type a digit: "))
        list.append([digit] * column)
    print("\nTable:")
    for i in range(row):
        for j in range(column):
            print(list[i][j], end = ' ')
            sum += list[i][j]
        print()
    print("\nSum of elements in a table is: " + str(sum))