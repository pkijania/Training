# 2. Create a coin toss game - predict the outcome of a coin toss

import random
user = str(input("heads or tails? "))
computer = random.choice(["heads","tails"])
if(user == computer):
    print('correct')
else:
    print('wrong')
print("user: ", user)
print("computer: ", computer)