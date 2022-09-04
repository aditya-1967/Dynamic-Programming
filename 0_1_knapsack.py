# 0/1 Knapsack
# DP on Subsequences

W = 8
weight = [3, 4, 5]
value = [30, 50, 60]

dp = [[-1] * (W+1) for _ in range(len(weight) + 1)]

def knapsack(i, W):
    if i == 0:
        if weight[0] <= W:
            return value[0]
        else:
            return 0
    
    if dp[i][W] != -1:
        return dp[i][W]
    
    notTake = knapsack(i - 1, W)
    take = float('-inf')
    if weight[i] <= W:
        take = value[i] + knapsack(i - 1, W - weight[i])
    
    dp[i][W] = max(take, notTake)
    return dp[i][W]

print(knapsack(len(weight) - 1, W))