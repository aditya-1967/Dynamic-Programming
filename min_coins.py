# Min Coins
# DP on Subsequences

coins = [1, 2, 3]
target = 7

dp = [[-1] * (target+1) for _ in range(len(coins) + 1)]

def min_coins(i, target):
    if i == 0:
        if target % coins[i] == 0:
            return target // coins[i]
        else:
            return float('inf')
    if dp[i][target] != -1:
        return dp[i][target]
        
    notTake = min_coins(i - 1, target)
    take = float('inf')
    if coins[i] <= target:
        take = 1 + min_coins(i, target - coins[i])
    
    dp[i][target] = min(notTake, take)
    return dp[i][target]

print(min_coins(len(coins) - 1, target))