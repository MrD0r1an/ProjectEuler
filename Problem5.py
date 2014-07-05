print(sum(range(1, 101))**2 - sum(i**2 for i in range(1, 101)))
print(sum(i*j for i in range(1,101) for j in range(1,101) if i!=j))