# Matrix Chain Multiplication

matrix = [10, 30, 5, 60]
n = len(matrix)  #total number of matrices is n - 1

dp = [[-1] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            dp[i][j] = 0

for i in range(n-1, 0, -1):
    for j in range(i+1, n):
        mini = float('inf')
        for k in range(i, j):
            steps = matrix[i-1] * matrix[k] * matrix[j] + dp[i][k] + dp[k+1][j]
        if steps < mini:
            mini = steps
        dp[i][j] = mini

print(dp[1][n-1])