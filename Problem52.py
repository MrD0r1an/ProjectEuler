n = 0
found = False
while not found:
    n += 1
    sn = str(n)
    sn2 = str(n * 2)
    sn3 = str(n * 3)
    sn4 = str(n * 4)
    sn5 = str(n * 5)
    sn6 = str(n * 6)
    if sorted(sn) == sorted(sn2) == sorted(sn3) == sorted(sn4) == sorted(sn5) == sorted(sn6):
        found = True
        print(sn, sn2, sn3, sn4, sn5, sn6)