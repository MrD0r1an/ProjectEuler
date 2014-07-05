last = 0
lastdelta = 99999999
lastx = 0
lasty = 0
for x in range(2000):
    for y in range(2000):
        result = 0.25 * x * (x + 1) * y * (y + 1)
        delta = abs(2000000 - result)
        if (delta < lastdelta):
            lastdelta = delta
            lastx = x
            lasty = y
            last = result
print(lastx, lasty, last, lastdelta)