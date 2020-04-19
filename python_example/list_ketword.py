# as

# as used to create alias while importing module

from math import cos
import math as mathAlias


print(mathAlias.cos(mathAlias.pi))

# Assert
# is used for debugging purpose

a = 4
# if the condition is true , nothing happen , But if the condition is false, AssertionError is raised

assert a < 5
# assert a > 5

# general
#assert condition, message
# assert a > 5, "Value is small"


# class


# class is used to define a new user-defined class in Python.

# class DemoClass:
#     def getDemo():
#         return True

#     def updateDemo():
#         ...


# def
# is used to define a user-define funtion
# Function is a block of related statements, which together does some specific task.


# del

# del is used to delete the reference to an object. Everything is object in Python. We can delete a variable reference using del


# from, import

# import keyword is used to import modules into the current namespace. from…import is used to import specific attributes or functions into the current namespace.
print(cos(90))
