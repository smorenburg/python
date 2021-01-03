string = 'Monty Python'
print(string[0:4])
print(string[6:7])
print(string[6:20])
print(string[8:])

data = 'From robin.smorenburg@linkit.nl Sat Jan'
position = data.find('@')
print(position)
space_position = data.find(' ', position)
print(space_position)
host = data[position+1:space_position]
print(host)
