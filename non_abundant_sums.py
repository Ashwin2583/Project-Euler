import math

# to check if the number is abundant or not
def abundant(x):
    sum = 1
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            sum = sum + i
            if i != x // i:
                sum = sum + x//i
    if sum > x:
        return True
    else:
        return False
    
# to get all the abundant numbers under 28123
abundant_numbers = []
num = 28123 # the limit
for j in range(1, num+1):
    if abundant(j):
        abundant_numbers.append(j)

# to get all the abundant numbers which can be expressed as the sum of 2 abundant numbers
final_val = set()
for l in abundant_numbers:
    for m in abundant_numbers:
        s = l + m
        if s > 28123:
            break
        final_val.add(s)

# to get the numbers which cannot be set as a sum
non_abundant_sum = 0
for k in range(1,num):
    if k not in final_val:
        non_abundant_sum = non_abundant_sum + k

print("The sum of all the positive integers which cannot be written as the "
"sum of two abundant numbers: ",non_abundant_sum)


    

