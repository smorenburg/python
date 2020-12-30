fruits = ["apples", "cherries"]

for fruits[-1] in fruits:
    print(fruits[-1], end="|")

print(fruits[-1])

x = 5


def fun(x):
    x = x - (x-2)
    return x


print(fun(fun(fun(x-1))))

x = 1
if x > 0:
    print("*")
    if x < 2:
        print("*")
    elif x == 1:
        print("*")
    else:
        print("*")
else:
    print("*")

tupl = ("bananas", "apples", "cherries")
print(sorted(tupl))

pi = float(3.14)
radius = int(1.0)
area = pi * radius ** 2
print(area)

address_book = {'name': "John", 'age': 23, 'city': "London"}

while address_book:
    address_book.popitem()
print(address_book)

me = "apples",
print(type(me))

high_fives = [10, 0, 5, 15]
high_fives.sort(reverse=True)
print(high_fives)

ui_elements = dict(
    [('radio_button', 2), ('text_box', 3), ('standard_button', 5)]
)
popped_element = ui_elements.popitem()
print(list(popped_element))

print("Hello", "World")
print("Hello", "World", sep=' ')
print("Hello", "World", sep=None)

count = 0
for i in range(0, 2):
    for j in range(0, 2):
        count += 1

print(count)

ones = [1]
ones_again = ones.extend([11, 111])
print(ones)
print(ones_again)


def fun2(a, b=1, c=4):
    print(a + b + c)


fun2(1, 2)
fun2(5, c=2)
fun2(c=8, a=3)

marks = [78, 89, 92, 68]


def max_marks(marks):
    return max(marks)


print(max_marks(marks))

b = 0b101010 << 2
print(bin(b))

nums = [1, 3]
for i in range(2):
    nums.insert(0, i)
print(nums)

a = 0
b = 1
while a < 1:
    while b < 2:
        print(a, b)
        a += 1
        b += 1


def add(new_value, values=[]):
    values.append(new_value)
    return values


vals = add("Toyota", ["BMW", "Merc"])
print(add("Ford", vals))


def squared(num):
    global sq
    sq = num ** 2


squared(5)
print(sq)

print("London", "Berlin", "Rome", "end=" " ")

greeting = "Hello"


def func():
    global greeting
    greeting = "Python"


func()
print(greeting)

lst = [x for x in range(3)]
print(lst)


def capitals(**val):
    for country, capital_city in val.items():
        print("{}->{}".format(country, capital_city))


capitals(UK="London", France="Paris")

name1 = name2 = name3 = "Simon"
print(name3)

fruits = ("Apples", "Oranges", "Bananas")
fruit1, fruit2, fruit3 = fruits
print(fruit3)

a = False
b = True

if a or b:
    print("True")
else:
    print("False")
