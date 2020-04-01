import random
peoples = []
i = 1
while i < 8:
    people = str(input("Enter people:"))
    peoples.append(people)
    i += 1

index = random.randint(0, 7)
print(peoples[index])
