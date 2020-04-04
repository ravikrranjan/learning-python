# write to file
#f = open("test.txt", "w")

# append to file
f = open("test.txt", "a")
f.write("\n This will write to file")

# read to file
f = open("test.txt", "r")

# read file and print in output
print(f.read())
