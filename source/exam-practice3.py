#!/usr/bin/env python3

def greeting(name=""):
    print("Hello", name)


greeting()

numbers = [[1, 2, 3]]
initializer = 1

for i in range(1):
    initializer *= 10
    for j in range(1):
        numbers[i][j] *= initializer

print(numbers)

x = 0
for i in range(10):
    for j in range(-1, -10, -1):
        x += 1
print(x)

a = 0b1011
b = 0b1001
print(bin(a ^ b))

x = 100


def glob():
    global x
    x = 20


glob()
print(x)

print("Python"*2, sep=',')

if not(True):
    print("Hello, World!")
else:
    print("Python is Awesome!")

num = [1, 2, 3, 4]
num.append(5)
print(num)

s1 = "Hello Mr Smith"
print(s1.capitalize())

if 1 == 1.0:
    print("Values are the same")
else:
    print("Values are different")

t1 = (1, 2, 3)
t2 = ('apples', 'banana', 'pears')
print(t1 + t2)

num = [1, 2, 3]
for i in range(len(num)):
    num.insert(i, i+1)
print(num)

print(end='', sep='--')

i = 0
while i > 3:
    i += 1
    print("Yes")
else:
    i -= 1
    print("No")

print(10/5)

print(9 % 2 ** 4)


def my_print(*val):
    print(val)


my_print("Peter", "Piper", "Pickled", "Pepper")


def fun(a=3, b=2):
    return b ** a


print(fun(2))

marks = 55
if marks > 70 and marks < 80:
    print("First Class")
elif marks > 60 and marks < 70:
    print("Second Class")
elif marks > 50 and marks < 60:
    print("Third Class")
else:
    print("No Class")

a = 'apple'
b = 'banana'

x, y = b, a
print(x, y, sep="::")

my_list = ["apples", "bananas", ""]
my_list.remove("apples")
print(my_list)

my_tuple = tuple('Python World!')
print(my_tuple[:-7])


def my_function(num):
    if num >= 4:
        return num
    else:
        return my_function(1) * my_function(2)


print(my_function(4))

d = {'one': 2, 'two': 2}
d['one'] = 1
print(d)


def triple(num):
    def double(num):
        return num * 2
    num = double(num)
    return num * 3


print(triple(2))

print("Peter", "Piper", sep=",")

val = 5
print("less than 10") if val < 10 else print("greater than 10")


def func(num):
    while num > 0:
        num = num - 1


num = 3
func(num)

lst1 = [1, 4, 8, 16]
lst2 = [4, 16, 8, 1]

print(lst1 == lst2)
