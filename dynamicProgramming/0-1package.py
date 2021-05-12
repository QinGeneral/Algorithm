def package(totalWeight, weights, values):
    def dp(curWeight, curValue, weights, values, i):
        if curWeight == 0:
            return curValue
        if i == len(weights):
            return curValue

        if curWeight < weights[i]:
            return dp(curWeight, curValue, weights, values, i + 1)
        else:
            return max(
                dp(curWeight, curValue, weights, values, i + 1),
                dp(
                    curWeight - weights[i], curValue + values[i], weights, values, i + 1
                ),
            )

    value = dp(totalWeight, 0, weights, values, 0)
    return value


def package(totalWeight, weights, values):

    weights = [0] + weights
    values = [0] + values
    dp = [[0] * (totalWeight + 1) for i in range(len(weights) + 1)]
    print(dp)
    for i in range(1, len(weights)):
        for j in range(1, totalWeight + 1):
            print(j, i)
            if j < weights[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i]] + values[i])
    return dp[len(weights) - 1][totalWeight]


print(
    package(
        5,
        [3, 2, 1],
        [5, 2, 3],
    )
)
