# 5. Find min and max value

def MinMax():
    list = []
    number_of_digits = int(input("How many digits?: "))
    if number_of_digits <= 1:
        print("\nNumber of digits must be at least 2")
    else:
        for i in range(number_of_digits):
            digit = int(input("Type a digit: "))
            list.append(digit)
        max = list[0]
        min = list[0]
        for i in range (len(list)):
            if (list[i] < min):
                min = list[i]
            if (list[i] > max):
                max = list[i]
        print(min, "min")
        print(max, "max")

MinMax()