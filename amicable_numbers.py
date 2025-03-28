# function to get sum of proper divisors of n
def d(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum = sum + i
    return sum

# function to find the amicable pair
def amicable(x):
    b = d(x)
    a = d(b)
    if a == x and a != b:
        return True
    else:
        return False

sum_amicable = 0
for j in range(1,10000):
    if amicable(j):
        sum_amicable = sum_amicable + j

print("The sum of all the amicable numbers under 10000: ",sum_amicable)


