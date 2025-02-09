# n=5
# for i in range(n):
#     for j in range(n): 
#         print("*", end=' ')
#     print()

n=5
for i in range(n):
    for j in range(i):
        print("*", end=" ")
    print()

n=5
for i in range(n):
    for j in range(i):
        print(j+1, end=" ")
    print()