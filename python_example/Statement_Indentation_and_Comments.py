# The end of a statement is marked by a newline character.

# a statement extend over multiple lines with the line continuation character(\)
a = 1 + 2 + 3 +\
    4 + 5 + 6 + 7 +\
    8 + 9 + 10

print(a)


# ine continuation is implied inside
#  parentheses ( ),
# brackets [ ], and braces { }

colors = ['red',
          'blue',
          'green']
print(colors
      )

for c in colors:
    print(c)


a = 1
b = 2
c = 3

#  Python Indentation


# A code block(body of a function, loop, etc.)
# starts with indentation and ends with the first unindented line.

for i in range(0, 20, 4):
    print(i)
    if i == 8:
        break


print("Docstrings in Python")
# Docstrings in Python
# A docstring is short for documentation string.

'''Python docstrings(documentation strings) are the string literals that appear right after the definition of a function, method, class, or module.'''


def double(a):
    """ Funtion do double value """
    return a * 2


print(double(5))
print(double.__doc__)
