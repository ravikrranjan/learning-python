
diction = {"name": "Ravi", "gender": "Male",
           "age": 23, "adress": "Pune", "phone": 1213124}

user_info = input("Give person :")

print(diction.get(user_info, 'invalid input'))
