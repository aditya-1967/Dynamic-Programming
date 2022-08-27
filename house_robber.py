# House Robber
# Max sum of non-adjacent elements

house = [2,1,4,9]

dp = [-1] * (len(house) + 1)

def house_robber(n):
    if n == 0:
        return house[n]
    if n < 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    pick = house[n] + house_robber(n-2)
    not_pick = house_robber(n-1)
    dp[n] = max(pick, not_pick)
    return dp[n]

print(house_robber(len(house) - 1))
