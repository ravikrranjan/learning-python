

# we do not know in advance
# the number of arguments that will be passed into a function.
def Food(*name):
    """
    use an asterisk (*) before the
     parameter name to denote this kind of
      argument.
    """
    print(type(name))
    print(name)
    for i in name:
        print(i)


# 3we have called the function with multiple arguments.
# These arguments get wrapped up into a tuple before being passed into the function.
Food([1, 3, 4, 5, 6, 7, 432], {2342, 24234})


print(Food.__doc__)
