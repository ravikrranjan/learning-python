# create a program that asks the user for his first name , his middle name and his last name. then print

firstName = input("Enter your first name: ")
middleName = input("Enter your middle name: ")
lastName = input("Enter your last name: ")

print("Your initilas are " + firstName[0] +
      " " + middleName[0] + " " + lastName[0])

productNumber = "037-00901-00027"

print("Country code: " + str(productNumber[:3]))
print("Product code: " + productNumber[4:9])
print("Batch number:" + productNumber[-5:])
