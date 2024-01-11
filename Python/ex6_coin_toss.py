# 6. Create a coin toss game - predict the outcome of a coin toss

import random

class TossGame:
    def __init__(self):
        self.correct_choices = ["heads", "tails"]

    def user_choice(self):
        self.user = str(input("heads or tails?: "))
        if not self.user in self.correct_choices:
            raise Exception(f"Unrecognized side of coin provided '{self.user}'")  
             
    def computer_choice(self):
        self.computer = random.choice(self.correct_choices)

    def check_outcome(self):
        if self.user == self.computer:
            print('Correct')
        else:
            print('Wrong')

    def show_outcome(self):
        print("User choice is:", self.user)
        print("Computer choice is:", self.computer)

if __name__ == "__main__":
    try:
        toss_game = TossGame()
        toss_game.user_choice()
        toss_game.computer_choice()
        toss_game.check_outcome()
        toss_game.show_outcome()
    except Exception as wrong_user:
        print(f"Error!!, program shut down due to {wrong_user}")