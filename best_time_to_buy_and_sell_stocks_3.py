# Best time to buy and sell stocks III
# DP on Stocks

prices = [3, 3, 5, 0, 0, 3, 1, 4]
n = len(prices)
k = 2

dp = [[-1] * 2 for _ in range(n)]

def func(ind, buy, k):
    if ind == n:
        return 0
    if k == 0:
        return 0
    if dp[ind][buy] != -1:
        return dp[ind][buy]
    
    if buy:
        profit = max(-prices[ind] + func(ind + 1, 0, k), func(ind + 1, 1, k))
        dp[ind][buy] = profit
    else:
        profit = max(prices[ind] + func(ind + 1, 1, k-1), func(ind + 1, 0, k))
        dp[ind][buy] = profit
    
    return dp[ind][buy]

print(func(0, 1, 2))