import math
import csv

with open("data.csv", newline= '') as f:
    reader = csv.reader(f)
    new_data = list(reader)

num = new_data[0]

def mean(num):
    n = len(num)
    total = 0
    for x in num:
        total+= int(x)

    mean = total/n
    return mean

squareList = []
for number in num:
    a = int(number) - mean(num)
    a = a**2
    squareList.append(a)

sum = 0 
for i in squareList:
    sum = sum + i

result = sum/(len(num) - 1)

stdDev = math.sqrt(result)
print(stdDev)
