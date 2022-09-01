# Maximum Path Sum
# 2D DP

mat = [[1, 2, 10, 4],
       [100, 3, 2, 1],
       [1, 1, 20, 2],
       [1, 2, 2, 1]]

m, n = len(mat), len(mat[0])

maximum = 0

dp = [[-1] * (n+1) for i in range(m+1)]

def maximum_path_sum(i, j):
    if j < 0 or j >= n:
        return float('-inf')
    if i == 0:
        return mat[0][j]
    if dp[i][j] != -1:
        return dp[i][j]
    
    up = mat[i][j] + maximum_path_sum(i-1, j)
    diag_left = mat[i][j] + maximum_path_sum(i-1, j-1)
    diag_right = mat[i][j] + maximum_path_sum(i-1, j+1)

    dp[i][j] = max(up, diag_left, diag_right)

    return dp[i][j]

for col in range(n):
    maximum = max(maximum, maximum_path_sum(m-1, col))

print(maximum)
