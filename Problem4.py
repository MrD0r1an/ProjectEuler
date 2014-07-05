def isPalendrome(n):
    s = str(n)
    s1 = "".join(list(reversed(str(n))))
    return s1 == s

for i in range(100, 999):
    for j in range (100, 999):
        if isPalendrome(i * j):
            print(i, j, i * j)