# 5. Find min and max value

list = [80,1,64,5,3,2,101,4,6,0,54,90]
max = list[0]
min = list[0]
for i in range (len(list)):  
  if (list[i] < min):
    min = list[i]
  if (list[i] > max):
    max = list[i]
print(min, "min")
print(max, "max")