print(1 ** 4 // 2)

temp = True

while not temp:
    print("Temp")
else:
    print("Fixed")

tupl = ('Python', 'World') * 2
print(tupl)

a = 'python'
i = 0
while i < len(a):
    i += 1
    pass
print('Value of i :', i)

name = ""
while name:
    print("Good Morning")
else:
    print("Good Night")

name = 'John'
age = 13

print(name, type(age))

x = 1

if (x < 3):
    print("True")
else:
    print("False")

s = 0
for i in range(1, 10):
    s = s + i
    print(s)
print(s)


def fun(y, x=5):
    return x/y


print(fun(2))

for i in range(3):
    print(i, end=" ")
print(i)

d = {}
d[0] = 'Python'
d['weekends'] = ["Saturday", "Sunday"]
print(d)

dict1 = {"John": 1234, "Fruit": "Apples"}
dict2 = {"Fruit": "Apples", "John": 1234}
print(dict1 == dict2)

s1 = "Hello"
s2 = "hello"
print(s1.lower() == s2.lower())

x = 2
y = 1.0
print(x+y)


def func(num):
    if num % 2 == 0:
        return True
    else:
        return False


x = func(2)
print(not x)

p = 0b1100
q = 0b1101
print(bin(p | q))


def fun2(a, b, c):
    return a * b * c


print(fun2(c=2, a=3, b=6))


def func3(mylist):
    mylist[3] = "strawberries"


lst = ["bananas", "apples", "pears", "peas"]
func3(lst)
print(lst)

x = 30


def change_me():
    global x
    x += 30
    print(30 + x)


change_me()
print(x)

data = [1, 2, "apples", 3.14, True]
del data[:2]
print(data)

tupl1 = (-1, 0, 1)
tupl2 = ('bananas')
tupl3 = (tupl1, tupl2)
print(tupl3)

for i in range(1):
    for j in range(1):
        print(i, j)


def fun1(data, *num):
    print(data)


fun1("Earth", 2, True, "Jupiter")
