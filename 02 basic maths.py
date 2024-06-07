# # extraction of digit or count of digit

import math

def roots(a, b, c):
    if a == 0:
        print("Invalid")
        return

    d = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(d))

    if d > 0:
        print("Roots are real and different")
        root1 = (-b + sqrt_val) / (2 * a)
        root2 = (-b - sqrt_val) / (2 * a)
        print(f"{root1}\n{root2}")
    elif d == 0:
        print("Roots are real and the same")
        root1 = -b / (2 * a)
        root2 = -b / (2 * a)
        print(f"{root1}\n{root2}")
    else:
        print("Roots are complex")
        real_part = -b / (2 * a)
        imaginary_part = sqrt_val / (2 * a)
        print(f"{real_part} + i{imaginary_part}\n{real_part} - i{imaginary_part}")

if __name__ == "__main__":
    a = 1
    b = -3
    c = -10
    roots(a, b, c)

# def evenlyDivides (N):
#         count = 0
#         while(N>0):
#             N//=10
#             count+=1
#         print(count)

# evenlyDivides(7789)


# def extract(n):
#       while(n>0):
#             ld = n%10
#             print(ld)
#             n//=10
# extract(7789)

# def count_digits(n):
#        count=0
#        x=n
#        while( x != 0 ):
#                x//=10
#                count+=1
#        return count

# n = 12345
# print("Number of digits in ",n," is ",count_digits(n)) 

# # second method simple

# count = 0
# x=7777
# while( x != 0 ):
#     x//=10
#     count+=1
# print(count)

# # reverse a number

# reverseNum = 0
# x=12345
# while( x != 0 ):
#     lastdigit = x%10
#     x//=10
#     reverseNum = reverseNum*10 + lastdigit
# print(reverseNum)

# # check palindrome

# n = 1221
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

# # armstrong numbers
      
# n = 371
# dup = n
# sum = 0
# while (n>0):
#       ld = n%10
#       sum = sum + (ld*ld*ld)
#       n//=10
# if(sum==dup):
#       print("Armstrong")
# else:
#       print("Not a Armstrong")

# # print all divisors

# n = 35
# for i in range(1,n):
#       if( n % i==0 ):
#             print(i)

# # check for prime 

# n = 5
# for i in range(2,n):
#     if (n%i==0):
#       print(" no prime number")
#       break
# else:
#       print('prime number')


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