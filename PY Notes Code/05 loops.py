# while loop 
i = 1
while i<=5:
    print("aman", i)
    i+=1

i = 5
while i>=1:
    print(i)
    i-=1

print("print numbers from 1 to 100")
i = 1
while i <=100:
    print(i)
    i+=1

print("print numbers from 100 to 1")
i = 100
while i >=1:
    print(i)
    i-=1

print('print the mul table of a number 1')
n = 2  #int(input("enter the number you  want table of : "))
i = 1
while i <=10:
    print(n*i)
    i+=1

print('print the elemnts')
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
heros = ["ironman", "thor", 'odin', 'hulk', 'loki', 'natasha', 'aman', 'shraddheya', 'prateek', 'prafull']
idx = 0
while idx < len(nums):
     print(nums[idx])
     print(heros[idx])
     idx +=1

# Break & Continue
# Break : used to terminate the loop when encountered
# Continue : terminates execution in the current iteration & continues execution of the loop with the next iteration
print('break')  
i =1
while i <= 5:
    print(i)
    if(i==3):
        break
    i+=1

print('continue')
i =1
while i <= 5:
    # print(i)
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1

# Loops are used used for sequential traversal. For traversing list, string, tuples etc.

print('for loop')
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
for val in nums:
    print(val)
else:
    print('End')

# range( )
# range( start?, stop, step?)
# Range functions returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

# pass Statement
# pass is a null statement that does nothing. It is used as a placeholder for future code.


