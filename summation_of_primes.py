import math

# input
n = 2000000

# checking for prime refer the 10001st_prime.py
def prime_check(x):
    if x <= 1:
        return False
    else:
        is_prime = True
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                is_prime = False
                break
        return is_prime

total = 0
i = 2
if n == 2:
    print(total)
else:
    while i < n:
        if prime_check(i):
            total = total + i
        i = i + 1

print("The sum of all the primes below 2 million: ",total)

