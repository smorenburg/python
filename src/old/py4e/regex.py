import re


handle = open('mbox-short.txt')
for line in handle:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)


handle = open('mbox-short.txt')
for line in handle:
    line = line.rstrip()
    if re.search(r'From:', line):
        print(line)


handle = open('mbox-short.txt')
for line in handle:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)


handle = open('mbox-short.txt')
for line in handle:
    line = line.rstrip()
    if re.search(r'^From:', line):
        print(line)


handle = open('mbox-short.txt')
for line in handle:
    line = line.rstrip()
    if re.search(r'^X.*:', line):
        print(line)


handle = open('mbox-short.txt')
for line in handle:
    line = line.rstrip()
    if re.search(r'^X-\S+:', line):
        print(line)


s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall(r'\S+@\S+', s)
print(lst)


x = 'My 2 favorite numbers are 19 and 42'
y = re.findall(r'[0-9]+', x)
print(y)
y = re.findall(r'[AEIOU]+', x)
print(y)


x = 'From: Using the : character'
y = re.findall(r'^F.+:', x)
print(y)


x = 'From: Using the : character'
y = re.findall(r'^F.+?:', x)
print(y)


handle = open('mbox-short.txt')
content = handle.read()
handle.close()
matches = re.findall(r'From (\S+@\S+)', content)
print(matches)


handle = open('mbox-short.txt')
content = handle.read()
handle.close()
matches = re.findall(r'^From .*@([^ ]*)', content)
print(matches)


handle = open('mbox-short.txt')
numlist = list()
for line in handle:
    line = line.rstrip()
    matches = re.findall(r'^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(matches) != 1:
        continue
    num = float(matches[0])
    numlist.append(num)
print('Maximum:', max(numlist))
