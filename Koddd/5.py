string = 'hello'
memory = 'world'
counter = 0
values = [0, 2, 4, 6, 8, 10]

while counter != 10:
    if counter in values:
        if 'world' not in string:
            string = string + 'world'
        memory = string
    if counter > 7:
        print(string + memory)
    counter += 1
print(string)
print(memory)
