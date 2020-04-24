

# def duble x:  x * 2

def bouble(x): return x * 2


print(bouble(5))

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x % 2 == 0), my_list))
# Program to filter out only the even items from a list
print(new_list)

new_list = list(map(lambda x: x * 2, my_list))

print(new_list)
