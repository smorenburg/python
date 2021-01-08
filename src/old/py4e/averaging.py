count = 0
total = 0
print('Before', count, total)

for value in [9, 41, 12, 3, 74, 15]:
    count += 1
    total += value
    print(count, total, value)

average = total / count
average_formatted = '{:.2f}'.format(average)

print('After', count, total, average_formatted)
