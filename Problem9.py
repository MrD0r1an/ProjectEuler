def run():
    for u in range(2, 200):
        for v in range(2, u):
            x = u**2 - v**2
            y = 2 * u * v
            z = u**2 + v**2
            if x + y + z == 1000:
                print(x, y, z)
                return

run()

print(375**2 + 200**2, 425**2)