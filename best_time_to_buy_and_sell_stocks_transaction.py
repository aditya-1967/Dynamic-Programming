# Best time to buy and sell stocks with transaction fee
# DP on Stocks

prices = [1, 3, 2, 8, 4, 9]
n = len(prices)
fee = 2

dp = [[-1] * 2 for _ in range(n)]

def func(ind, buy):
    if ind == n:
        return 0
    if dp[ind][buy] != -1:
        return dp[ind][buy]
    
    if buy:
        profit = max(-prices[ind] + func(ind + 1, 0), func(ind + 1, 1))
        dp[ind][buy] = profit
    else:
        profit = max(prices[ind] + func(ind + 1, 1) - fee, func(ind + 1, 0))
        dp[ind][buy] = profit
    
    return dp[ind][buy]

print(func(0, 1))