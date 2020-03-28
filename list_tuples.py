
dob = input("enter date of birth in the format MM-DD-YYYY: ")
# dob format = DD-MM-YYYY
months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")
dob_m = dob[3:5]

print("You are born in " + months[int(dob_m) - 1])

persons = ["Ravi", "Ranjan", "Vicky"]

new_person = input("Enter your name :")

persons.append(new_person)

print(persons)
