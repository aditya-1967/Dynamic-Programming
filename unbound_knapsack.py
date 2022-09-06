# Unbounded Knapsack
# DP on Subsequences

W = 10
weight = [2, 4, 6]
value = [5, 11, 13]

dp = [[-1] * (W+1) for _ in range(len(weight) + 1)]

def unbounded_knapsack(index, W):
    if index == 0:
        return (W // weight[0]) * value[0]
    if dp[index][W] != -1:
        return dp[index][W]

    notTake = unbounded_knapsack(index - 1, W)
    take = float('-inf')
    if weight[index] <= W:
        take = value[index] + unbounded_knapsack(index, W - weight[index])
    
    dp[index][W] = max(take, notTake)

    return dp[index][W]

print(unbounded_knapsack(len(weight) - 1, W))