# squares = [i ** 2 for i in range(1, 1000000)]
# n = 10**12
# while 1:
#     b = 0.5 + (0.25 + 0.5 * (n**2 - n))**0.5
#     if (b == int(b)):
#         print(b, n)
#         break
#     n += 1

n = 120
while 1:
    q = n**2 - n
    if q % 2 == 0 and q == int(q**0.5)**2:
        print(0.5 + (0.25 + 0.5 * (n**2 - n))**0.5, n)
        break
    n += 1