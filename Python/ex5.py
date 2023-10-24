# 5. Find min and max value

list = [80,1,64,5,3,2,101,4,6,0,54,90]
length = len(list)
max = 0
min = 0
for i in range (length):  
  if (min == 0 or i < min):
    min = i
  if (max == 0 or i > max):
    max = i
print(min,"min")
print(max,"max")