# 0-1 Knapsack
wt = [1,3,4,5]
val = [1,4,5,7]
W = 7
n = len(wt)

#Recursive
def knapsack(wt, val, W, n):
    if n == 0 or W == 0:
        return 0
    if wt[n-1] <= W:
        return max(val[n-1] + knapsack(wt, val, W-wt[n-1], n-1), knapsack(wt, val, W, n-1))
    if wt[n-1] > W:
        return knapsack(wt, val, W, n-1)

      
#Memoization
dp = [[-1]*(W+1) for i in range(n+1)]
def knapsack(wt, val, W, n):
    if n == 0 or W == 0:
        return 0
    if dp[n][W] != -1:
        return dp[n][W]
    if wt[n-1] <= W:
        dp[n][W] = max(val[n-1] + knapsack(wt, val, W-wt[n-1], n-1), knapsack(wt, val, W, n-1))
        return dp[n][W]
    if wt[n-1] > W:
        dp[n][W] = knapsack(wt, val, W, n-1)
        return dp[n][W]
    
    
#Top-Down
for i in range(n+1):
    for j in range(W+1):
        if i == 0 or j == 0:
            dp[i][j] == 0
for i in range(1, n+1):
    for j in range(1, W+1):
        if wt[i-1] <= j:
            dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][W])

print(knapsack(wt, val, W, n))
print(dp)

