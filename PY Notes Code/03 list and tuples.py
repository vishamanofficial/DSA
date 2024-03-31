# arrauy me hm same type of data store karate hain pr list me hm diffrent type of data print karwa skte hain
student = ["Aman Vishwakarma", 22, 99, "vill dalhanpur post siddiqpur dist jaunpur"]
print("name of the studnet: ", student[0])
print("age of the studnet: ", student[1])
print("marks of the studnet: ", student[2])
print("address of the studnet: ", student[3])

# list in python 

marks = [ 90, 54, 45, 46, 55]
# printing marks 
print(marks)
# printing type of marks 
print("Type of marks",type(marks))
# printing length of marks 
print("Length of marks",len(marks))
# printing the value of the index 
print(marks[0])
print(marks[1])
print(marks[2])
# changing the value at index 
marks[0] = 99
print(marks[0])

# main diffrence between string and list
# string immutable (index pe value ko change nahi kr skte hain)
# list mutable (index pe value ko change kr skte hain)

# list slicing 
print(marks[2: ])

# list methods 

list = [1, 2, 3]
# append method element ko last me add kr deta hai 
list.append(4)
print(list)
# sort in ascending order 
list.sort()
print(list)
# sort in descending order
list.sort( reverse=True)
print(list)
# reverse list 
list.reverse()
print(list)
# insert element at index 
list.insert(5,5)
print(list)
# removes first occurrence of elememnt
list.remove(1)
print(list)
# remove element at index 
list.pop(3)
print(list)



# Tuples in python 
# (a built in data type that lets us create immutable swquence of values)

tup = (56, 656, 2345 , 46534)
print(type(tup), tup)
print(tup[1])
# slicing is same as list 

# tuple methods
# returns index of first occurence
tup.index(656)
print(tup)
# counts total occurance
tup.count(56)
print(tup)


