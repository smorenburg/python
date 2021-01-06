name, phone, location = "John", 123455667, "London"
print(name, phone, location)

area = 25.6
area = int(area)
print(area)

print(2 % 5 ** 2)

p = 10
q = 20
r = 30

if p > 10 and q > 20 and r > 30:
    print("True")
else:
    print("False")

val1 = 0b111
val2 = val1 << 2

print(bin(val2))

lst1 = [2, 4, 6]
lst2 = [2, 4, 6]

print(lst1 is lst2)
print(lst1 == lst2)

str = "Hello Python!"
str = str[-7:len(str)]
print(str)

fruits = ("Apples", "Oranges", "Bananas")
a, b, c = fruits
print(b)

tupl1 = (1., 2., 3.)
tupl2 = ("Earth", "Mars", "Jupiter")
x = (tupl1 + tupl2)[-3]
print(x)

groceries_list1 = ["Milk", "Cheese"]
groceries_list2 = ["Bread", "Butter"]
groceries_list1.extend(groceries_list2)
print(groceries_list1)

capitals1 = ["London", "New York", "Rome"]
capitals2 = capitals1
capitals2.remove("New York")
print(capitals1)

dict = {1: "iOS"}
dict[2] = 'Android'
print(dict)

cities = {"UK": "London", "France": "Paris", "Germany": "Berlin"}

for city in cities.items():
    print(city)

val = 7
print("hi") if val < 15 else print("bye")

for i in range(1, 3):
    print(i)
else:
    print("hi")

for i in range(1, 4):
    print(i)
    break
else:
    print("hi")

i = 0
while i < 4:
    i += 1
    print(i)
    break
else:
    print("Break")

i = 0
while i < 4:
    i += 1
    print(i)
else:
    print("Break")


def fun(x=4, y=5):
    y -= 1
    return x * y * 1


print(fun())


def fun4(x):
    x[-1] = "c"


val = ["a", "b", "c", "d"]
fun4(val)
print(val)


def fun6(x):
    return ["Tea"]


coffees = ["Cappuccino", "Latte", "Macchiato"]
tea = fun6(coffees)
print(tea)


def fact(num):
    if num == 1:
        return 1
    return fact(num - 1) * num


print(fact(4))


def grades(param1, param2, *grades):
    print(param2)


print(grades("Grace", "London", ["A", "A*", "B+"]))


def fun7(**names):
    for key, value in names.items():
        print(key, value, end=" ", sep=":")


fun7(NAME="John", AGE=29, CITY="London")
