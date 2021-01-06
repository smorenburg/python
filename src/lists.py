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


fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    words = line.split()
    email = words[1]
    pieces = email.split('@')
    print('Domain name:', pieces[1])
