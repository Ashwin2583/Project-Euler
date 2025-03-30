import math

num = ['0','1','2']

p = math.factorial(len(num))

for i in range(0,p):
    print(num)
    first = num[0]
    last = num[len(num) - 1]
    num[0] = last
    num[len(num) - 1] = first

