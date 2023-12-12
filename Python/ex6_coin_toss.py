# 6. Create a coin toss game - predict the outcome of a coin toss

import random

def toss_game():
    correct_choices = ["heads", "tails"]
    user = str(input("heads or tails?: "))

    if not user in correct_choices:
        raise Exception(f"Unrecognized side of coin provided '{user}'")

    computer = random.choice(correct_choices)
    if user == computer:
        print('correct')
    else:
        print('wrong')
    return user, computer

try:
    print(toss_game())
except Exception as wrong_user:
    print(f"Error!!, program shut down due to {wrong_user}")