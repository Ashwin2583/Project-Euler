import math as m

# inputs 
w = 20 # width
h = 20 # height

p = m.factorial(w+h)/(m.factorial(w) * m.factorial(h)) # combinatarics
print("number of routes through a 20x20 grid: ",p)
