counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen', 'csev', 'cwen', 'robin']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)


counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen', 'csev', 'cwen', 'robin']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)


counts = {'robin': 1, 'csev': 2}
print(counts.get('kris', 0))


counts = {'chuck': 1, 'annie': 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])


counts = dict()
print('Enter a line of text:')
line = input()
words = line.split()
print('Words:', words)
print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts:', counts)


inp = {'chuck': 1, 'annie': 42, 'jan': 100}
for key, value in inp.items():
    print(key, value)


name = input('Enter file:')
handle = open(name)
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigword = None
bigcount = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
