# arr = [1, 2, 3, 1, 2, 2, 1]
# def fn(number):
#     count = 0
#     for i in arr:
#         if i == number:
#             count += 1
#     return count
# print(fn(1))


# n = int(input())
# arr = list(map(int, input().split()))
# arr = [1, 2, 2, 3, 1]
# n = len(arr)

# # precompute
# hash = [0] * 13
# for i in range(n):
#     hash[arr[i]] += 1
# # queries
# q = int(input("Kitni queries karni hain? "))
# while q > 0:
#     number = int(input("Kaunsa number check karna hai? "))
#     print(f"{number} occurs {hash[number]} times")
#     q -= 1


# s = input("String daalo: ")  # e.g., aabchb

# # precompute
# hash = [0] * 256  # covers all ASCII characters
# for ch in s:
#     hash[ord(ch)] += 1

# # queries
# q = int(input("Kitni queries karni hain? "))
# for i in range(q):
#     ch = input("Kaunsa character check karna hai? ")[0]  # first character only
#     print(hash[ord(ch)])



# python dict 
arr = [1, 2, 2, 3, 1]
n = len(arr)

# precompute
mpp = {}
for num in arr:
    if num in mpp:
        mpp[num] += 1
    else:
        mpp[num] = 1

# print frequency map (optional, jaise C++ mein print kiya tha)
for key in mpp:
    print(f"{key} -> {mpp[key]}")

# handle queries
q = int(input("Kitni queries karni hain? "))
for _ in range(q):
    number = int(input("Kaunsa number check karna hai? "))
    print(f"{number} occurs {mpp.get(number, 0)} times")




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


# import math
# n=int(input())
# k=(1<< int(math.log2(n))+1)-1
# print(n^k)
