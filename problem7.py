def isPrime(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True

i = 0
n = 2
while i < 10001:
    if isPrime(n):
        print(n, i)
        i += 1
    n += 1