def max_value_knapsack(n, W, pears):
    # dp array to store the maximum value for each weight
    dp = [0] * (W + 1)

    for weight, value in pears:
        # Traverse the dp array from back to front
        for w in range(W, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)

    return dp[W]


# Reading input
n, W = map(int, input().split())
pears = [tuple(map(int, input().split())) for _ in range(n)]

# Getting the result
result = max_value_knapsack(n, W, pears)
print(result)
