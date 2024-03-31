# function : block of statement that performs the specific operation or task

# defining function
def calc_result(a,b):
    sum = a + b
    print(sum)
    return sum
# calling function
calc_result(60, 9)
calc_result(1, 68)

def calc_sum(a , b):
    return (a + b)
sum = calc_sum(60, 9)
print(sum)

# Recursion
# a function calles itself

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)
show(69)

# printing factorial using Recursion

print("printing factorial")

def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))   
print(factorial(5))

