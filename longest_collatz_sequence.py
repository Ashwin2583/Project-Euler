
largest_initial = 0
temp = 0
initial = 13

while initial < 1000000:
    temp_initial = initial
    seq_len = 0
    while True:
        if temp_initial == 1:
            seq_len = seq_len + 1
            break
        seq_len = seq_len + 1
        if temp_initial % 2 == 0:
            temp_initial = temp_initial//2
        else:
            temp_initial = 3*temp_initial + 1
    if seq_len > temp:
        temp = seq_len
        largest_initial = initial
    initial = initial + 1

print("The starting number under one million which produces the longest chain: ",largest_initial)


