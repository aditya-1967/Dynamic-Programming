# Best time to buy and sell stocks
# DP on Stocks

arr = [7, 1, 5, 3, 6, 4]

minimum = arr[0]
profit = 0 

for i in range(1, len(arr)):
    cost = arr[i] - minimum
    profit = max(profit, cost)
    minimum = min(arr[i], minimum)

print(profit)