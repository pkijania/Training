# 6. Replace numbers divisible by 3 with a word "Fizz", numbers divisible by 5 with a word "Buzz" and numbers divisible by 3 and 5 with a word "FizzBuzz"

def FizzBuzz():
    for i in range(1,51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

FizzBuzz()