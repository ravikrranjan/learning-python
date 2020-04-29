x = 30


def foo():
    global x
    x = 20

    def bar():

        # nonlocal x
        x = 25

    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)


foo()
print("x in main: ", x)
