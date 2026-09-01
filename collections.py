# TUPLES, LISTS, SETS AND DICTIONARIES

# TUPLES

# tuples are Immutable = cannot be changed after creation.
tuples = (1, 2, 3, 4, 5)
print(tuples)
# (1, 2, 3, 4, 5)


# LISTS

# lists are Mutable = can be changed after creation.
num=[5, 10, 15, 20]
print(num)
num[0] = 50
print(num)
# [5, 10, 15, 20]
# [50, 10, 15, 20]



# SETS

# Sets are Mutable = can be changed after creation.
# does not allow duplicate values and does not maintain order.
sets = {1, 2, 3, 4, 5}
print(sets)
# {1, 2, 3, 4, 5}


# DICTIONARIES

# dictionaries are Mutable = can be changed after creation.
# does not allow duplicate keys and does not maintain order.
# holds key-value pairs.

student = {
    "name": "Alice",
    "age": 20,
    "marks": 85
}

print(student)
# {'name': 'Alice', 'age': 20, 'marks': 85}

print(student["name"])
# Alice