name = input('What is your first name? ')

print(
    'Your name is as long or longer the the avarage first name'
) if len(name) >= 6 else print(
    'Your name is shorter than the avarage first name'
)

message = (
    'The first letter in your name is among the five most common'
    if name[0].lower() in ['a', 'j', 'm', 'e', 'l'] else
    'The first letter in your name is not among the five most common'
)

print(message)

for letter in name:
    print(
        f"{letter} {'is a vowel' if letter.lower() in ['a', 'e', 'i', 'o', 'u'] else 'is a constant'}"
    )
