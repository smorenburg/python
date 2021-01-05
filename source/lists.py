friends = ['Robin', 'Ronak']
for friend in friends:
    print('Happy new year:', friend)
print('Done')


numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)
