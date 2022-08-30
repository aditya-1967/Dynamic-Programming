# Unique Paths
# 2D DP

mat = [[0] * 2 for i in range(2)]
m, n = len(mat), len(mat[0])

dp = [[-1] * (n+1) for i in range(m+1)]

def unique_paths(i, j):
    if i == 0 and j == 0:
        return 1
    if i < 0 or j < 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    
    up = unique_paths(i-1, j)
    left = unique_paths(i, j-1)
    dp[i][j] = up + left
    return dp[i][j]

print(unique_paths(m-1, n-1))
