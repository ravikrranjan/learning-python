

def getName():
    pass
    # return "Ravi"


print(getName())  # None


def getName():
    pass
    return "Ravi"


print(getName())  # Ravi


def greet(name):
    """ 
    This function greets to the person passed
    is as a parameter
    """
    print("Hello", name, ". Good morning!")


greet("Ravi")
print(greet("Ravi"), sep="====", end="///", flush=False)


# print() with file parameter

sourceFile = open("print_output.txt", "w")
print("Ravi", file=sourceFile)
sourceFile.close()
