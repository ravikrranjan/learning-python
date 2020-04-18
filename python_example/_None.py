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
