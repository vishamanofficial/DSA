
# # second method simple

# count = 0
# x=7777
# while( x > 0 ):
#     x//=10
#     count+=1
# print(count)


# def evenlyDivides(N):
#         n = str(N)
#         count = 0
#         for i in n:
#             if int(i)==0:
#                 continue
#             elif N%int(i)==0:
#                 count+=1
#         return count
# print(evenlyDivides(7789))


# # reverse a number

# reverseNum = 0
# x=44100
# while( x != 0 ):
#     lastdigit = x%10
#     x//=10
#     reverseNum = reverseNum*10 + lastdigit
# print(reverseNum)

# # leetcode 
# def reverse(x):
#     # Initialize an empty string to store the reversed number and set the sign to positive
#     y = ''
#     sign = 1

#     # Iterate through each character in the string representation of the input number
#     for i in str(x):
#         if i == '-':  # If the character is a minus sign, set the sign to negative
#             sign = -1
#         else:  # Otherwise, add the character to the reversed string
#             y += i

#     # Reverse the string, convert it to an integer, and apply the sign
#     y = sign * int(y[::-1])

#     # Check for overflow and return 0 if the reversed number is out of 32-bit signed integer range
#     if y < -(2 ** 31) or y > (2 ** 31 - 1):
#         return 0

#     # Return the reversed number
#     return y

# print(reverse(123))  # Output: 321
# print(reverse(-123))  # Output: -321
# print(reverse(120))  # Output: 21


# # check palindrome

# n = 1221
# print(n)
# revNum = 0
# dup = n
# while (n>0):
#       ld = n%10
#       revNum = revNum*10 + ld
#       n = n//10
# if(dup==revNum):
#       print("Palindrome")
# else:
#       print("Not a palindrome")

# leetcode 

# def isPalindrome(x):
#     if x < 0:
#         return False
#     reversed_num = 0
#     dup = x
#     while dup != 0:
#         digit = dup % 10
#         reversed_num = reversed_num * 10 + digit
#         dup //= 10
#     return reversed_num == x
# print(isPalindrome(121))

# # armstrong numbers
      
# def armstrongNumber(n):
#     dup = n
#     sum = 0
#     while (n>0):
#         ld = n%10
#         sum = sum + (ld*ld*ld)
#         n//=10
#     if(sum==dup):
#         print("Armstrong")
#     else:
#         print("Not a Armstrong")
# armstrongNumber(371)

# # print all divisors

# n = 36
# for i in range(1,n+1):
#       if( n % i==0 ):
#             print(i)
# this has time complexity of O(n)

# import math

# def print_divisors(n):
#     divisors = []
#     for i in range(1, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             divisors.append(i)
#             if i != n // i:
#                 divisors.append(n // i)
#     divisors.sort()
#     for divisor in divisors:
#         print(divisor)

# # Example usage
# n = int(input("Enter a number: "))
# print_divisors(n)

# sum of all divisors

# def sumOfDivisors(N):
#     total_sum = 0
#     for i in range(1, N + 1):
#         sum_divisors = 0
#         for j in range(1, i + 1):
#             if i % j == 0:
#                 sum_divisors += j
#         total_sum += sum_divisors
#     return total_sum
# print(sumOfDivisors(4))


# def sumOfDivisors(N):
#     total_sum = 0
#     for i in range(1, N + 1):  
#         total_sum += i * (N // i)  # Each number i appears (N // i) times as a divisor
#     print(total_sum)
# print(sumOfDivisors(4))





# # check for prime 

n = 8
for i in range(2,n):
    if (n%i==0):
      print(" no prime number")
      break
else:
      print('prime number')

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

# Example usage:
print(is_prime(2))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(17)) # Output: True
print(is_prime(20)) # Output: False



# num = 2
# if num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#    for i in range(2,num):
#        if (num % i) == 0:
#            print(num,"is not a prime number")
#            break
#    else:
#        print(num,"is a prime number")
# else:
#    print(num,"is not a prime number")
            
# # GCD to HCF

# a = 52
# b = 10
# while (a> 0 and b> 0):
#      if a>b:
#           a = a%b
#      else:
#       b = b%a
# if a == 0:
#     print(b)
# else:
#      print(a)