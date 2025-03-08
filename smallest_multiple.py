import math


# inputs
num = range(1,20)

# iteration to calculate the LCM using gcd
lcm = 1
for i in num:
    lcm = lcm*i // math.gcd(lcm, i)

print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20: ", lcm)
