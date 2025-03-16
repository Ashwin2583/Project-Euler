import math 

def factor_func(n):
    factors_num = 0
    sqrt_n = int(math.sqrt(n))
    for i in range(1,sqrt_n+1):
        if n % i == 0:
            if i != n // i:
                factors_num += 2
            else:
                factors_num += 1
    return factors_num

def triangular_number(n):
    return int(n*(n+1)/2)

f_length = 0
i = 1
while True:
    t_num = triangular_number(i)
    f_length = factor_func(t_num)
    if f_length >= 500:
        print("Value of the first triangle number to have over five hundred divisors: ",t_num)
        break
    else:
        i = i + 1
