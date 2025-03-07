n = 2 #input is 3

# the product of 2 n-digit number lies in the range of these below
lower_lim = 10**(n - 1)
upper_lim = 10**n - 1

# function to check if the values is palindrome
def palindrome_check(x):
    rev = 0
    copy = x
    while (x != 0):
        digit = x % 10
        rev = (rev * 10) + digit
        x = x//10
    if rev == copy:
        return True
    else:
        return False

# iteration for changing p and q and checking 
# if it is palindrome or not within the bounds 
pali = []
for p in range(upper_lim,lower_lim,-1):
    for q in range(p,lower_lim,-1):
        pro = p*q
        if palindrome_check(pro):
            pali.append(pro)

print("The largest palindrome made form the product of two 3-digit numbers: ",pali[0])

