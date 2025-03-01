
num1 = 0
num2 = 1
next_number = num2  
number = [num1,num2]

while next_number < 4000000:
    num1, num2 = num2, next_number
    next_number = num1 + num2
    number.append(next_number)

even_number = []
for i in range(len(number)):
    if number[i] % 2 == 0:
        even_number.append(number[i])

print("The sum of the even number in fibonacci series under 4 million ",sum(even_number))

