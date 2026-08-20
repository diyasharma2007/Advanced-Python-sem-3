# Longest Common Subsequence (LCS)
# Using Dynamic Programming - Bottom-Up Approach

def lcs(a, b):
    m = len(a)
    n = len(b)

    # Create a DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Find the LCS
    i = m
    j = n
    ans = ""

    while i > 0 and j > 0:

        if a[i - 1] == b[j - 1]:
            ans = a[i - 1] + ans
            i -= 1
            j -= 1

        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1

        else:
            j -= 1

    return ans


# Main program
a = input("Enter first sequence: ")
b = input("Enter second sequence: ")

ans = lcs(a, b)

print("Longest Common Subsequence:", ans)
print("Length of LCS:", len(ans))

