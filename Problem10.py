def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    #print(n)
    return True

print(sum((i if isPrime(i) else 0) for i in range(2, 2000000)))
