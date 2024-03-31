# it start a infinite loop and then stack overflow happens

# def Print(n):
#     print("aman",n)
#     print("backchodi")
#     Print(0) 
# Print(1)


# The selected code defines a function called greet(). This function has a loop that increments the variable i by 1 and prints "hello" followed by the current value of i. Then, it calls the greet() function again, repeating the process.

# The sys.setrecursionlimit(200) function sets the maximum recursion depth for the interpreter. In this case, it is set to 200.

# The sys.getrecursionlimit() function returns the current recursion limit.

# In the main function, the greet() function is called recursively, which leads to an infinite loop and a stack overflow error. This is because the Python interpreter runs out of stack space when it tries to recursively call the greet() function.

# To fix this, you can increase the recursion limit by calling sys.setrecursionlimit(n) where n is the desired recursion limit. In this case, increasing the recursion limit to 10000 should fix the stack overflow error.

import sys 
sys.setrecursionlimit(200)

i = 0
def greet():
    global i
    i += 1
    print('hello', i)
#     greet()

# greet()
    