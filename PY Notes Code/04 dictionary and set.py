# Dictionary in Python
# Dictionaries are used to store data values in key:value pairs
# “key” : value
# They are unordered, mutable(changeable) & don’t allow duplicate

student = {
    "name" : "Aman",
    "age" : 22,
    "score": {
        "chem": 97,
        "phy" : 98,
        "math" : 99
    }
}
# adding value to the dict 
student["surname"] = "Vishwakarma"
# accessing the dictionary
print(student["name"])
print(student["score"]["math"])

# Dictionary Methods
print
# student.keys( ) #returns all keys
print(student.keys())
# student.items( ) #returns all (key, val) pairs as tuples
print(student.items())
# student.update( newDict ) #inserts the specified items to the dictionary
print(student.update({"age": 22}))
# student.values( ) #returns all values
print(student.values())
# student.get( “key““ ) #returns the key according to value
print(student.get("age"))


# Set in Python
# Set is the collection of the unordered items.
# Each element in the set must be unique & immutable.

nums = { 1, 2, 3, 4 }
set2 = { 1, 2, 2, 2 }
#repeated elements stored only once so it resolved to {1, 2}

null_set = set( ) #empty set syntax

# Set Methods
set = { 1,2,3,4,5}

print(set)
# set.add( el ) #adds an element
set.add(6)
print(set)
# set.remove( el ) #removes the elem an
set.remove(6)
print(set)
# set.pop( ) #removes a random value
set.pop()
print(set)
# set.clear( ) #empties the set
set.clear()
print(set)
# set.union( set2 ) #combines both set values & returns new
set1 = {1,2,3}
set2 = {4,5,6}
print(set1.union(set2))
# set.intersection( set2 ) #combines common values & returns new 
print(set1.intersection(set2))
