def prime_factors(n):
    factors = []
    
    # Check for number of twos in the factorization
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Check for odd factors from 3 onwards
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    # If n is still greater than 2, it must be a prime number
    if n > 2:
        factors.append(n)
    
    return factors

# Example usage
num = int(input("Enter a number: "))
print("Prime factors:", prime_factors(num))
