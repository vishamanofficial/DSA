# File I/O in Python
# Python can be used to perform operations on a file. (read & write data)

f = open("data.txt", 'r')
data  = f.read()
print(data)
print(type(data))
f.close()
