# Unique Paths II
# 2D DP

mat =[[0, 0, 0], 
      [0, 1, 0],
      [0, 0, 0]]

m, n = len(mat), len(mat[0])

dp = [[-1] * (n+1) for i in range(m+1)]

def unique_paths_2(i, j):
    if i >= 0 and j >= 0 and mat[i][j] == 1:
        return 0
    if i == 0 and j == 0:
        return 1
    if i < 0 or j < 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    
    up = unique_paths_2(i-1, j)
    left = unique_paths_2(i, j-1)
    dp[i][j] = up + left
    return dp[i][j]

print(unique_paths_2(m-1, n-1))