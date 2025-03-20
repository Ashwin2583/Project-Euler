n = 2
mult = 1
for i in range(1000):
    mult = n*mult

arr = [int(i) for i in str(mult)]

sum = 0
for j in arr:
    sum = sum + j

print("The sum of the digits of the number 2^1000: ",sum)

