# 2. Create a coin toss game - predict the outcome of a coin toss

import random
y = str(input("heads or tails? "))
x = random.choice(["heads","tails"])
if(x==y):
    print('you guessed')
else:
    print('you didnt guess')
print("user: ",y)
print("computer: ",x)