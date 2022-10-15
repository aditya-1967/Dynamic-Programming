# Best time to buy and sell stocks with cooldown
# DP on Stocks

prices = [4, 9, 0, 4, 10]
n = len(prices)

dp = [[-1] * 2 for _ in range(n)]

def func(ind, buy):
    if ind >= n:
        return 0
    if dp[ind][buy] != -1:
        return dp[ind][buy]
    
    if buy:
        profit = max(-prices[ind] + func(ind + 1, 0), func(ind + 1, 1))
        dp[ind][buy] = profit
    else:
        profit = max(prices[ind] + func(ind + 2, 1), func(ind + 1, 0))
        dp[ind][buy] = profit
    
    return dp[ind][buy]

print(func(0, 1))
