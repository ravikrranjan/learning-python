# Python List
# a list is created by placing all the items (elements) inside square brackets [], separated by commas.

my_list = []

my_list.insert(1, 3)

print(my_list[0])

# nested list
my_list = ["mouse", [8, 4, 6], ['a']]

print(my_list)

# access elements from a list
# List Index
# The index must be an integer.

# Negative indexing

# Negative indexing in lists
my_list = ['p', 'r', 'o', 'b', 'e']

print(my_list[-1])

print(my_list[-5])

# List slicing in Python

my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']

# elements 3rd to 5th
print(my_list[2:5])

# elements beginning to 4th
print(my_list[:-5])

# elements 6th to end
print(my_list[5:])

# elements beginning to end
print(my_list[:])
# Correcting mistake values in a list
odd = [2, 4, 6, 8]

# change the 1st item
odd[0] = 1

print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]

print(odd)
# item to a list using the append() method or add several items using extend() method.
#
# Appending and Extending lists in Python
odd = [1, 3, 5]

odd.append(7)

print(odd)

odd.extend([9, 11, 13])

print(odd)

# we can insert one item at a desired location by using the method insert() or insert multiple items by squeezing it into an empty slice of a list.

# Demonstration of list insert() method
odd = [1, 9]
odd.insert(1, 3)

print(odd)

odd[2:2] = [5, 7]

print(odd)

# delete or remove elements from a list?
# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# delete one item
del my_list[2]

print(my_list)

# delete multiple items
del my_list[1:5]

print(my_list)

# delete entire list
del my_list

# Error: List not defined
print(my_list)
