n = 1000

first = 0
second = 1
i = 2
while True:
    third = first + second
    if len(str(third)) == n:
        break
    else:
        i = i + 1
        first = second
        second = third

print("The index of the first tern in the Fibonacci sequence to contain 1000 digits: ",i)
