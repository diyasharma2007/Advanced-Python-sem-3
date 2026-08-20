# 0/1 Knapsack using Dynamic Programming

# Bottom-Up Approach
def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Top-Down Approach
def knapsack_top_down(weights, values, capacity, n, dp):

    if n == 0 or capacity == 0:
        return 0

    if dp[n][capacity] != -1:
        return dp[n][capacity]

    if weights[n - 1] <= capacity:

        include = values[n - 1] + knapsack_top_down(
            weights, values, capacity - weights[n - 1], n - 1, dp
        )

        exclude = knapsack_top_down(
            weights, values, capacity, n - 1, dp
        )

        dp[n][capacity] = max(include, exclude)

    else:
        dp[n][capacity] = knapsack_top_down(
            weights, values, capacity, n - 1, dp
        )

    return dp[n][capacity]


# Main Program
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

# Bottom-Up result
bottom_up_result = knapsack_bottom_up(weights, values, capacity)

# Top-Down result
n = len(weights)
dp = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]

top_down_result = knapsack_top_down(
    weights, values, capacity, n, dp
)

print("Bottom-Up Maximum Value:", bottom_up_result)
print("Top-Down Maximum Value:", top_down_result)