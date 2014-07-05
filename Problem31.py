coins = [1, 2, 5, 10, 20, 50, 100, 200]
count = 0

def addCoin(combination, missing, used):
    if missing == 0:
        global count
        count += 1
    elif missing > 0:
        for coin in coins:
            if coin >= used:
                combination.append(coin)
                addCoin(combination, missing - coin, coin)
                combination.pop()

addCoin([], 200, 1)

print(count)