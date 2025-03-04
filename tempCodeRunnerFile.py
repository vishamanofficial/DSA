import math

def print_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    
    divisors.sort()
    for divisor in divisors:
        print(divisor)

# Example usage
n = int(input("Enter a number: "))
print_divisors(n)