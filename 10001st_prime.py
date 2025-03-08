import math

# input 
n = 10001

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

prime = 2
if n == 1:
    print(prime)
else:
    temp = 1
    k = 0
    while k < n:
        temp = temp + 1
        if prime_check(temp):
            k = k + 1

print("The 10001st prime number is: ",temp)



