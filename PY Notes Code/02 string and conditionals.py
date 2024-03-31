# string 
str1 = "Aman"
str2 = "Vishwakarma"

# concatination of string 
name = str1 + " "+ str2
print(name)

# length of string 
print(len(name))

# indexing 
print(name[0])

# slicing [starting index : ending index]
print(name[5 : ])

# string functions
print(str2.replace("Vishwakarma","Sharma"))

print(str2.endswith("ma"))

print(name.count("a"))


name = input("enter name : ")
print(len(name))


# conditioal statement 

marks = int(input("enter marks : "))

if (marks >= 90):
    grade = "A"
elif ((marks >= 80) and (marks<90)):
    grade = "B"

print(grade)


marks = int(input("enter marks : "))
if(marks%2==0):
    print("Even")
else:
    print("Odd")
