# 1.
# x = "global"
# def foo():
#     print("x inside :", x)
# foo()
# print("x outside:", x)

# 2.
# x = 2
# def double():
#     x = x * 2
#     print(x)


# print(double())  # UnboundLocalError: local variable 'x' referenced before assignment


# 3.

# x = "global"


# def foo():
#     # global x
#     y = "local"
#     # x = x * 2
#     print(x * 2)
#     print(y * 2)


# foo()

# 4.
# Create a nonlocal variable


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
        x = x * 2
        print("double:", x)

    inner()

    print("outer:", x)


outer()
