def count_end_states(n, k):
    # Initialize a 2D DP table with all zeros
    dp = [[0] * (k + 1) for _ in range(n * n + 1)]

    # Base case: If no stones to place, there is one valid end state
    dp[0][0] = 1

    # Iterate through all cells in the board
    for i in range(1, n * n + 1):
        # Iterate through all possible numbers of stones placed
        for j in range(1, min(k, i) + 1):
            # If we place a stone in this cell, consider all possible previous states
            # where j-1 stones were placed in the previous i-1 cells
            dp[i][j] = dp[i - 1][j - 1] * (i - j + 1)
            # Add to it the case where we don't place a stone in this cell
            dp[i][j] += dp[i - 1][j]

    # The answer is the sum of all valid end states in the last cell
    return sum(dp[-1])


# Example usage:
n, k = map(int, input().split())
print(count_end_states(n, k))
