# input
n = 100 

def sum_n(n):
    return n*(n+1) / 2 # fomula for the sum of n natural number

def sum_sn(n):
    return n*(n+1)*(2*n + 1) / 6 # formula for the sum of square of n natural number

difference = (sum_n(n)**2) - sum_sn(n) 
print("The difference between the sum of the squares of the first one hundred natural numbers and "
"the square of the sum: ",difference)