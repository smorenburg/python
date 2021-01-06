import urllib.request
import urllib.parse
import urllib.error


handle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in handle:
    print(line.decode().strip())


handle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in handle:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
