# 贪心算法


def getMinCoinCountHelper(total, values):
    rest = total
    count = 0

    for value in values:
        curCount = rest // value
        rest -= curCount * value
        count += curCount

        if rest == 0:
            return count

    return -1


def getMinCoinCount():
    values = [5, 3]
    total = 11
    return getMinCoinCountHelper(total, values)


print(getMinCoinCount())


# 回溯算法


def getMinCoinCountHelper(coins, total, values, i):
    print(i, coins, total, values)
    if total == 0:
        return True
    if i == len(values):
        return False
    if total < values[i]:
        if getMinCoinCountHelper(coins, total, values, i + 1):
            return True

        value = coins.pop()
        return getMinCoinCountHelper(coins, total + value, values, i)
    else:
        coins.append(values[i])
        return getMinCoinCountHelper(coins, total - values[i], values, i)


def getMinCoinCount():
    values = [5, 3]
    total = 11
    coins = []
    if getMinCoinCountHelper(coins, total, values, 0):
        print(coins)
        return len(coins)
    return -1


print(getMinCoinCount())


# 动态规划


def getMinCounts(k, values):
    memo = [k + 1] * (k + 1)
    memo[0] = 0

    for i in range(1, k + 1):
        print(memo)
        for coin in values:
            if i - coin < 0:
                continue
            memo[i] = min(memo[i], memo[i - coin] + 1)

    return -1 if memo[k] == k + 1 else memo[k]


def getMinCountsDPSolAdvance():
    values = [3, 5]
    total = 22
    return getMinCounts(total, values)


print("-----------------")
print(getMinCountsDPSolAdvance())