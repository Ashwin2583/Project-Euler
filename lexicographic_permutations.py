import math

num = ['0','1','2','3','4','5','6','7','8','9']
pos = 1000000

t = pos - 1
permutation = []
for i in range(len(num)-1,-1,-1):
    fact = math.factorial(i)
    index = t // fact
    t %= fact

    permutation.append(num.pop(index))

print("The millionth lexicographic permutation of the digits 0,1,2,3,4,5,6,7,8 and 9: ",permutation)



        


