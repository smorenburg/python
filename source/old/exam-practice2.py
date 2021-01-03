#!/usr/bin/env python3

lst1 = [0, 1]
lst2 = [1, 0]
for x in lst1:
    for y in lst2:
        print(x, y)


def oddoreven(num):
    if (num % 2 == 0):
        print('even')
    else:
        print("odd")


oddoreven(13)


def sum(a, b):
    return a * b
    return a + b


print(sum(2, 3))

print("Hello", "\nPython!")

full_name = "john-smith williamson"
print(full_name.title())

milk_left = "None"
if milk_left:
    print("Groceries trip pending!")
else:
    print("Let's enjoy a bowl of cereals")

age = 19
print(not age > 18 and age < 20)

Dict = dict({1: 'Python', 2: 'Dictionaries'})
print(Dict)


def put(x):
    return [6]


val = [0, 1, 2, 3, 4, 5]
y = put(val)
print(y)

num = [1, 2, 3, 4, 5, 6, 7]
print(num[::-1])

num = 4,
print(type(num))

print("Hello", "World", "Python", sep="#")

print(5//4)

tup1 = (1, 3, 5)
tup2 = (2, 4)

tup1 = tup1+tup2
print(tup1)

a = 'wi'
b = 'fi'
print(a + b * 3)

if x != 10:
    print("#")
    if x < 8:
        print("#")
    elif x == 10:
        print("#")
    else:
        print("#")
else:
    print("#"*3)

programming_language = "Python 3"
print(programming_language[-1])

i = 0
while i < 1:
    print('Hello', end=", ")
    i += 1
else:
    print("World")

for num in range(1, 10, 2):
    print(num, end=",")

var = ['Python', 'Tuple']
print(tuple(var))


def swap(x, y):
    z = x
    x = y
    y = z


x = 5
y = 10
swap(x, y)
print(x, y)

print(9 ** 3 ** 0 ** 1)

name = 'john'
print(name == "John")

fruits = ["Apples", "Oranges", "Mangoes"]
for fruit in fruits:
    if fruit != "Apples":
        print(fruit, end=" ")


def default(x, y=5):
    print(y, x)


default(1)


def put1(x):
    x[-1] = 6


val = [0, 1, 2, 3, 4, 5]
put1(val)
print(val)

Dict = {'Name': 'Python', 1: [1, 2, 3, 4], 2: "hi"}
print(Dict)

dict1 = {1: "One", 2: "Two"}
dict1[2] = "One"
print(dict1)

if x != 10:
    print("#")
    if x < 8:
        print("#")
    elif x == 10:
        print("#")
    else:
        print("#")
else:
    print("#"*3)
