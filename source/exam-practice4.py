fruits = ["apples", "bananas"]

for i in range(1, 2):
    for fruit in fruits:
        print(i, fruit)

vowels = ["a", "e", "i", "o", "u"]
all = list(range(-2)) + vowels
print(all)


def func(x):
    x = [1, 2, 3]
    return x


x = [4, 5, 6, 7]
y = func(x)
print(x, y)

print(5 % 4 ** 2 // 2)

for i in range(10, 12, 2):
    if i % 2 != 1:
        print("No")
    else:
        print("Yes")


def my_func(val1=2, val2=4):
    print(val1 + val2)


my_func(val2=3)

lst = [1, 2] * 5
print(len(lst))

a = 'Python'
i = 0
while i < len(a):
    i += 1
print(i)


def area_square(side):
    return side ** 2


print(area_square(10))

tuple_one = (1, 2, 3)
tuple_two = ("Apples", "Bananas")
tuple_three = (tuple_one + tuple_two)
print(tuple_three)

greeting = "Knowledge Is Power"
print(greeting[::])


str = "Betty Bought A Bit Of Bitter Butter"
print('Butter' in str)

x = []
y = ""
z = -1

print(bool(x), bool(y), bool(z))

p = 10
q = 10
print(p is q)

a = int(3)
b = 'Python'
print(a * b)

greeting = "Good Morning"

for ch in greeting:
    if ch == 'o':
        break
    print(ch)
else:
    print("Good Night")


def fun(*val):
    print(type(val))


lst = [1, 2, 3, 4, 5]
number = 400
fun(lst, number)

languages = {
    'lang1': {1: 'Python'},
    'lang2': {2: 'Java'}
}
print(languages['lang1'][1])

num = [1, 2, 3, 4, 5, 6, 7]
print(num[::-5])


a = 1
b = 1
while a < 2:
    while b < 2:
        print(a, ":", b)
        b += 1
        a += 1

x = 0b101
y = 0b110
print(bin(x & y))
