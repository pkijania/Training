# 2. Heads or tails

import random
user=0
computer=0
y = str(input("orzeł czy reszka? "))
x = random.choice(["orzeł","reszka"])
if(x==y):
 print('zgadłeś')
else:
 print('nie zgadłeś')
print("użytkownik: ",y)
print("komuter: ",x)