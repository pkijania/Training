# 2. Heads or tails

import random
user=0
computer=0
y = str(input("heads or tails? "))
x = random.choice(["heads","tails"])
if(x==y):
 print('you guessed')
else:
 print('you didnt guess')
print("user: ",y)
print("computer: ",x)