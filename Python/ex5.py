# 5. Min and max value

max=0
min=0
for i in lista:
 if (min == 0 or i < min):
   min = i
 if (max == 0 or i > max):
   max = i
print(min,"min")
print(max,"max")