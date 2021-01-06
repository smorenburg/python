#!/usr/bin/env python3

message = input('Enter a message: ')

print('Lowercase:', message.lower())
print('Uppercase:', message.upper())
print('Capitalized:', message.capitalize())
print('Title', message.title())

words = message.split()
print('Words:', words)

sorted_words = sorted(words)
print('Alphabetic first word:', sorted_words[0])
print('Alphabetic last word:', sorted_words[-1])
