# Best time to buy and sell stocks II
# DP on Stocks

prices = [7, 1, 5, 3, 6, 4]
n = len(prices)

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
        profit = max(prices[ind] + func(ind + 1, 1), func(ind + 1, 0))
        dp[ind][buy] = profit
    
    return dp[ind][buy]

print(func(0, 1))