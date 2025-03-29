alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def alpha_val(arr):
    sum = 0
    for i in arr:
        pos = alphabets.index(i)
        sum = sum + (pos + 1)
    return sum

path = r"C:\Users\ashwi\Downloads\0022_names.txt" # input the path of the file here

with open(path, "r", encoding= 'utf-8') as file:
    text = file.read().strip()


name_list = text.replace('"','').split(',')
name_list.sort()

total = 0
for j in name_list:
    al_val = alpha_val(j)
    total = total + al_val*(name_list.index(j) + 1)

print("The total of all the name scores in the file: ",total)







