for a in range(1, 333): # iterating a where a<b<c
    for b in range(a+1,500): # iterating b where b > a
        c = 1000 - (a + b) 
        if a**2 + b**2 == c**2: # checking for pythagorean relation
            print("The product abc: ",a*b*c)
