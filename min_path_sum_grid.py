# Minimum Path Sum in Grid
# 2D DP

mat = [[5, 9, 6], 
       [11, 5, 2]]

m, n = len(mat), len(mat[0])

dp = [[-1] * (n+1) for i in range(m+1)]

def min_path_sum_grid(i, j):
    if i == 0 and j == 0:
        return mat[0][0]
    if i < 0 or j < 0:
        return float('inf')
    if dp[i][j] != -1:
        return dp[i][j]
    up = mat[i][j] + min_path_sum_grid(i-1, j)
    left = mat[i][j] + min_path_sum_grid(i, j-1)
    dp[i][j] = min(up, left)
    return dp[i][j]

print(min_path_sum_grid(m-1, n-1))