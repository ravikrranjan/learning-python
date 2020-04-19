print(type(None))
# <class 'NoneType' >
# >> >
# >> >
# >> >
print(None == True)
# False
print(None == False)
# False
print(None == 0)
# False
print(None == [])
# False
print("None == None")
print(None == None)
print("\n")
# True
# print(None > None)
# Traceback(most recent call last):
#     File "<stdin>", line 1, in < module >
# TypeError: '>' not supported between instances of 'NoneType' and 'NoneType'

X = None
Y = None
print(X == Y)
# True

# None is a special constant in Python that represents the absence of a value or a null value.

# Void functions that do not return anything will return a None object automatically.
#  None is also returned by functions in which the program flow does not encounter a return statement.


def a_void_function():
    a = 1
    b = 2
    c = a + b


X = a_void_function()
print(' a_void_funtion return :', X)


def improper_return_functions(a):
    if (a % 2) == 0:
        return True


x = improper_return_functions(4)
print('Return function :', x)
