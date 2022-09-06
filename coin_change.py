# Ways to coin change
# DP on Subsequences

coins = [1, 2, 3]
target = 4

dp = [[-1] * (target+1) for _ in range(len(coins) + 1)]

def coin_change(index, target):
    if index == 0:
        return 1 if target % coins[0] == 0 else 0
    if dp[index][target] != -1:
        return dp[index][target]
    notTake = coin_change(index - 1, target)
    take = 0
    if coins[index] <= target:
        take = coin_change(index, target - coins[index])
    dp[index][target] = take + notTake
    return dp[index][target]

print(coin_change(len(coins) - 1, target))