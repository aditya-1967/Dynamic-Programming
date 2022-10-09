# Distinct Subsequnces
# DP on String

s1 = "babgbag"
s2 = "bag"
m, n = len(s1), len(s2)

dp = [[-1] * (n+1) for _ in range(m+1)]

def distinct(m, n):
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = 0
            if j == 0:
                dp[i][j] = 1
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[m][n]

print(distinct(m, n))