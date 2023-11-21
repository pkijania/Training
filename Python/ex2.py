# 2. Create a coin toss game - predict the outcome of a coin toss

import random

def toss_game():
    user = str(input("heads or tails? "))
    computer = random.choice(["heads","tails"])
    if(user == computer):
        print('correct')
    else:
        print('wrong')
    return user, computer

out = toss_game()
print(out)