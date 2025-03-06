def is_prime(n):
    # If n is less than 2, it's not a prime number
    if n <= 1:
        return False
    
    # Check for factors from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:  # If n is divisible by i, it's not a prime number
            return False
    
    # If no factors are found, n is a prime number
    return True   

Example usage:
print(is_prime(2))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(17)) # Output: True
print(is_prime(20)) # Output: False