def greet(name, msg):

    print('Hello ' + name + ". " + msg)


# we call a function with some values,
#  these values get assigned to the arguments according to their position
greet('ravi', 'GM')
greet('Good morning', 'Ravi')

# called using keyword arguments.
# The order (position) of the arguments can be changed.
# TypeError: greet() got multiple values for argument 'name'
# greet('Good morning', name='Ravi')

# 2 keyword arguments (out of order)
greet(msg='Good morning', name='Ravi')

# 1 positional, 1 keyword argument
greet('Ravi', msg='Good morning')

# we can mix positional arguments with keyword arguments during a function call.
# But we must keep in mind that keyword arguments must follow positional arguments.

# SyntaxError: positional argument follows keyword argument
greet(name='ravi', "Good morning")
