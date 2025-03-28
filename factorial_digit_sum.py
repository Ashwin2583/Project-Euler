# function to find the factorial; i know there is a built-in-function ;)
def factorial(x):
    fact = 1
    for i in range(x, 0,-1):
        fact = fact*i
    return fact

# input
num = factorial(100)

digit_arr = [int(j) for j in str(num)] # digit in an array

# summing the number in the array
sum = 0
for i in digit_arr:
    sum = sum + i

print("The sum of the digits in the number 100!: ",sum)
