# 7. Create a coin toss game - predict the outcome of a coin toss

import random

def toss_game():
    user = str(input("heads or tails?: "))
    computer = random.choice(["heads", "tails"])
    if user == computer:
        print('correct')
    else:
        print('wrong')
    return user, computer

print(toss_game())