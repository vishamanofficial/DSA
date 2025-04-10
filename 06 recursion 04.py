# reverse an array

# marks = [ 90, 54, 45, 46, 55]
# def fn(i):
#     if(i>=len(marks)/2):
#         return
#     marks[i], marks[len(marks)-i-1] = marks[len(marks)-i-1], marks[i]
#     fn(len(marks) + 1 )
# fn(0)

# print(marks)

# marks = [ 90, 54, 45, 46, 55]
# def fn(l ,r ):
#     if ( l >= r ): return
#     marks[l], marks[r] = marks[r], marks[l]
#     fn(l+1, r-1)
# fn(0, len(marks)-1)

# print(marks)

# string palindrome 

# str = 'madsm'
# def fn(i):
#     if(i>=len(str)/2):
#         return
#     if (str[i] != str[len(str)-i-1]):
#         print("string is not palindrome")
#     fn(i + 1 )
# fn(0)

# print(str)

# leetcode sol

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         newStr = []
#         for c in s:
#             if c.isalnum():
#                 newStr += c.lower()
#         return newStr == newStr[::-1]


# class Solution(object):
#     newArray = {}
#     def fib(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n == 0: return 0
#         if n == 1: return 1
#         if n in self.newArray:return self.newArray[n]
#         result = self.fib(n-1) + self.fib(n-2)
#         self.newArray[n] = result
#         return result
