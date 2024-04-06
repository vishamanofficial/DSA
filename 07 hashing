# arr = [1,2,3,1,2,2,1]
# def fn(number):
#     global count 
#     count = 0
#     for i in arr:
#         if (arr[i]==number):
#             count = count + 1
#         return count
# print(count)
# fn(1) 

# n = int(input())
# arr = list(map(int, input().split()))

# # precompute
# hash = [0] * 13
# for i in range(n):
#     hash[arr[i]] += 1

# q = int(input())
# while q > 0:
#     number = int(input())
#     # fetching
#     print(hash[number])
#     q -= 1


# Count frequency of each element in the array

# def countFreq(arr, n):
#     visited = [False] * n
#     for i in range(n):
#         if (visited[i] == True):
#             continue
#         count = 1
#         for j in range(i + 1, n):
#             if (arr[i] == arr[j]):
#                 visited[j] = True
#                 count += 1
#         print(arr[i], count)


# if __name__ == "__main__":
#     arr = [10,5,10,15,10,5]
#     n = len(arr)
#     countFreq(arr, n)


import math
n=int(input())
k=(1<< int(math.log2(n))+1)-1
print(n^k)