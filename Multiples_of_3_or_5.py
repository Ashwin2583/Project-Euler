
# inputing the number 
num = int(input("Enter the number: "))

# funtion to find the arithmetic sum
def arithmetic_sum(n,a,l):
    S_n = (n/2)*(a + l)
    return S_n

# function to generate the multiples
def multiples(x,m):
    mult = []
    i = 1
    while i < x:
        if i % m == 0:
            mult.append(i)
        i = i + 1
    return mult

M_3 = multiples(num,3) # list of multiples of 3 below num
M_5 = multiples(num,5) # list of multiples of 5 below num
M_15 = multiples(num,15) # list of multiples of 15 below num
s_3 = arithmetic_sum((num-1)//3,M_3[0],M_3[len(M_3)-1])
s_5 = arithmetic_sum((num-1)//5,M_5[0],M_5[len(M_5)-1])
s_15 = arithmetic_sum((num-1)//15,M_15[0],M_15[len(M_15)-1])

S = s_3 + s_5 - s_15
print("The Sum of all the multiples of 3 or 5 below 1000 ", S)


