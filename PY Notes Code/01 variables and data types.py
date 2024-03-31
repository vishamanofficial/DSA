# printing something
print("hello world")
print("hello world", "My name is Aman Vishwakarma")
print(69)
print(60+9)

# variables
name = "Aman Vishwakarma"
age = 22
location = 6.9
old = False
a = None

# printing the variables
print(name)
print(age)
print(location)
print(old)

print("My name is :", name)
print("My age is :", age)
print("My location is :", location)

# type of variables
print(type(name))
print(type(age))
print(type(location))
print(type(old))
print(type(a))

# print sum 
a = 60
b = 9
sum = a + b
print(sum)

#arithmetic operators
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

# relational opeartors 
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
 
# assignment operator 
num = 10
print("Num is :", num)
num = num + 10 
print("Num is :", num)
num += 10 #both are same
print("Num is :", num)
num -= 10
print("Num is :", num)
num *= 10
print("Num is :", num)
num /= 10
print("Num is :", int(num))
num %= 10
print("Num is :", num)
num **= 10
print("Num is :", num)

# logical operator 
# not operator negation print krta hai
a = 50
b = 10
print(not a > b)
# and operator do value ka comparision krke agar dono true hai to true return krta hai 
val1 = True
val2 = True
print("and operator :", val1 and val2)

val1 = True
val2 = False
print("and operator :", val1 and val2)
# OR operator agar dono me se ek bhi value true ho jaye to true return karega aur dono false ho to false return karega
val1 = True
val2 = False
print("OR operator :", val1 or val2)

val1 = False
val2 = False
print("OR operator :", val1 or val2)

print("OR operator :", (a == b) or (a > b))

# type conversion
# isme python automatic type conversion krta hai 
a = 2
b = 4.25
print(a + b)

a, b = 1, 2.0
sum = a + b
print(sum)
# type casting 
# isme hme manually khud se type conversion krna padta hai
a = 2
b = 4.25
c = int(b)
print(a + c)

a, b = 1, "2"
c = int(b)
sum = a + c
print(sum)

# input in python
name = input("Enter your name :") #is tarah se kuch bhi input denge , wo string me hi store hoga
print("Welcome ", name)
#for printing the value in integer data type
val = int(input("enter the int value :"))
print(type(val), "int value is :", val)
# for printing the value in float data type
val = float(input("enter the float value :"))
print(type(val), "float value is :", val)


# practice qus
num1 = int(input("enter first num :"))
num2 = int(input("enter second num :"))
sum = (num1 + num2)
print(sum)

#practice qus
side = float(input("enter side :"))
print("area is :", side*side)

#practice qus
num1 = int(input("enter first value :"))
num2 = int(input("enter second value :"))
avg = (num1+num2)/2
print("average is :", avg)

#practice qus
a = int(input("enter first value :"))
b = int(input("enter second value :"))
print(a>=b)
