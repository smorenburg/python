#!/usr/bin/env python3

ages = {
    'Keith': 30,
    'Levi': 25,
    'John': 20,
}
del ages['Keith']
print(ages)

values = ['Kevin Bacon', 60, '555-555-5555', False]
val = not values[-1]
print(val)

ages = {
    'Keith': 30,
    'Levi': 25,
    'John': 20,
}
output = [str(value) for value in ages.values()]
print(output)

names = ['Alice', 'Lance', 'Bob', 'Mike']
all_names = names
names.append('Brock')
print(sorted(all_names))

num = 12
num2 = num
num = num + 1
num2 = num2 / 2
print(num2)

for num in range(10):
    print(num)
    if num % 2 == 0:
        continue
    else:
        break

num = 15.1
num2 = num / 4
num2 //= 2
num2 + 1
print(num2)


def fizz(num):
    if num % 3 == 0 and num % 5 == 0:
        return print('FizzBuzz')
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num


fizz(15)

num = 5
message = 'Hello'
print(message, num)

names = ['Alice', 'Bob', 'Lance', 'Mike']
names[1:2] = []
print(names)

ages = {'Keith': 30, 'Levi': 25, 'John': 20}
age = ages.get('Kevin')
print(age)

num = 9
if num < 10:
    print("Less than 10")
if num > 10:
    print("Greater than 10")
else:
    print("Less than 10")


def fib(n):
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
        yield a


fib_gen = fib(1)
print(fib_gen)

val = 1 or '2'
val *= 3
print(val)

names = ['Alice', 'Bob', 'Lance', 'Mike']
names[:3]
print(names)

letter = 'a'
if letter < 'b':
    print("First")
if letter == 'b' or letter > 'c':
    print("Second")
elif letter <= 'a':
    print("Third")
else:
    print("Fourth")

num = input("Enter a float value: ")
new_num = float(num) // 100 * 1.0
print(new_num)

num = 10
if num > 20 or num >= 10:
    print("First")
elif num <= 10:
    print("Second")
else:
    print("Third")


def add_five(num1, num2=5):
    return num1 + 5


print(add_five(1, 2))
