
diction = {"name": "Ravi", "gender": "Male",
           "age": 23, "adress": "Pune", "phone": 1213124}
print(type(diction))
user_info = input(
    "What information do you want to know about person :").lower()

print(diction.get(user_info, 'invalid input'))
