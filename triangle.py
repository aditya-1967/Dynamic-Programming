# Triangle
# 2D DP

triangle = [[1],
            [2, 3],
            [3, 6, 7],
            [8, 9, 6, 10]]

n = len(triangle)

dp = [[-1] * (n+1) for i in range(n+1)]

def min_path_sum_traingle(i, j):
    if i == n - 1:
        return triangle[n-1][j]
    if dp[i][j] != -1:
        return dp[i][j]
    
    down = triangle[i][j] + min_path_sum_traingle(i+1, j)
    diag = triangle[i][j] + min_path_sum_traingle(i+1, j+1)

    dp[i][j] = min(down, diag)
    return dp[i][j]

print(min_path_sum_traingle(0, 0))