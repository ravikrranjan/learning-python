for i in range(1, 11):
    print(i)


my_integers = [1, 2, 3, 4, 5]

my_integers = [5, 7, 1, 3, 4]
print(my_integers[0])  # 5
print(my_integers[1])  # 7
print(my_integers[4])  # 4

relatives_names = [
    "Toshiaki",
    "Juliana",
    "Yuji",
    "Bruno",
    "Kaio"
]

print(relatives_names[4], relatives_names[3])  # Kaio

blog_posts = ['', "Python fucntion",  "CLoudWatch put metric",
              "dynamodb update", "angular upgrade", ""]

for post in blog_posts:
    if post == "":
        continue
    else:
        print(post)
print('--------------------------------------------------------------------')
mystring = "This is test string"

for char in mystring:
    print(char)


print('--------------------------------------------------------------------')

for x in range(1, 20):
    print(x)

print('--------------------------------------------------------------------')
persons = {'name': 'Ravi', 'age': '45', 'gender': 'Male'}

for key in persons:
    print(key, ":", persons[key])
