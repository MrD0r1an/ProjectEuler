one = 1
two = 1
three = 0
i = 2
while three < 10**999:
    i += 1
    three = one + two
    one = two
    two = three
print(i)