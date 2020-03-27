myName = "Ravi"

print(type(myName))  # Result: <class 'str'>

str1 = 'Ravi'
print(type(str1))  # Result:  <class 'str'>

# String should always be inside quotation marks event if you pass a number inside quotations marks

mystring = "33"

print(type(mystring))

# every string is a sequence of character
myString = 'meet at 5pm'

print(myString[0])

# minus index read string from last
print(myString[-1], '----', myString[:-2:1])


# Get lenght of string by len function

ln = len(myString)

print(ln)

# get last character of string using its length

myString = "Ravi"
ln = len(myString)
print(myString[ln - 1])

# bank ifsc code
ifscCode = "SBIN0003456"

# get bank name

print(ifscCode[0:3])

# bank ifsc code
ifscCode = "0003456SBI"

# get bank name
# read from -3 to last index of string
print(ifscCode[-3:])

# begining of string

print(myString[:2])


# concatenate string

print("Hello" + " " + "ravi")
print("Learing days: " + str(2))
