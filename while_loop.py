number = 8

guess = int(input("I'm thinking a number between zero to ten, Can I gusess ? "))

while True:
    if guess == number:
        break
    else:
        guess = int(input('Nope, Try agian :'))
print("You gussed it, I was thinking about", number)
