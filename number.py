
import math
num1 = 5
num2 = 4

print(num1 + num2)
print(num1 - num2)

print(type(num1))

mode = num2 % num1

power = num1 ** num2

print(mode, power)

# math module operations

print('The smallest integer greater than or equal to x: ', math.ceil(4.2))
print('the largest integer less than or equal to x: ', math.floor(4.2))
print(' factorial of 5: ', math.factorial(5))

print('Return True if x is neither an infinity nor a NaN, and False otherwise', math.isinf(5))


print('Return True if x is a NaN (not a number), and False otherwise: ',
      math.isnan(34), math.isnan(math.nan))


# Angular conversion

degree = 180

print(math.degrees(math.pi))

print(math.radians(degree))

print(math.pi)
