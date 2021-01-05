d = {'a': 10, 'b': 1, 'c': 22, 'e': 25, 'd': 2}
t = sorted(d.items())
for k, v in sorted(d.items()):
    print(k, v)


d = {'a': 10, 'b': 1, 'c': 22, 'e': 25, 'd': 2}
tmp = list()
for k, v in d.items():
    tmp.append((v, k))
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)


handle = open('mbox-short.txt')
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for k, v in counts.items():
    tmp = (v, k)
    lst.append(tmp)

lst = sorted(lst, reverse=True)

for v, k in lst[:10]:
    print(k, v)


d = {'a': 10, 'b': 1, 'c': 22, 'e': 25, 'd': 2}
print(sorted([(v, k) for k, v in d.items()], reverse=True))
