import keyword

# Keywords are the reserved words in Python.
# #We cannot use a keyword as variable name, function name or any other identifier.
print(keyword.iskeyword)

# Result : <built-in method __contains__ of frozenset object at 0x1033f8580 >

# keyword list
print(keyword.kwlist)

# Result :
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
#    'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
