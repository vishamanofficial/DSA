# largest element in array 

# arr = [1,2,3,6,7,8,9,10,11,12,13,14]
# largest = arr[0]
# for i in range(len(arr)):
#     if(arr[i] > largest):
#         largest = arr[i]
# print (largest)


# second largest element in array 

# Python program to find second largest
# number in a list

# list of numbers - length of 
# list should be at least 2
list1 = [10, 20, 4, 45, 99]

mx = max(list1[0], list1[1]) 
secondmax = min(list1[0], list1[1]) 
n = len(list1)
for i in range(2,n): 
	if list1[i] > mx: 
		secondmax = mx
		mx = list1[i] 
	elif list1[i] > secondmax and \
		mx != list1[i]: 
		secondmax = list1[i]
	elif mx == secondmax and \
		secondmax != list1[i]:
		secondmax = list1[i]

print("Second highest number is : ",\
	str(secondmax))




def findLargest(arr):
    secondLargest = 0
    largest = min(arr)
 
    for i in range(len(arr)):
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
        else:
            secondLargest = max(secondLargest, arr[i])
 
    # Returning second largest element
    return secondLargest
 
 
# Calling above method over this array set
print(findLargest([10, 20, 4, 45, 99]))

def second_largest(numbers):
    first = 0
    second = 0
    for n in numbers:
        if n > first:
            first, second = n, first
        elif first > n > second:
            second = n
    return second or None
print(second_largest([4,6,2,2,-2]))