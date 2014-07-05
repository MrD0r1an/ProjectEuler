numbers = []
r = range(2, 101)
for a in r:
    for b in r:
        n = a ** b
        if not n in numbers:
            numbers.append(n)

print(len(numbers))