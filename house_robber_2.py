# House Robber II

house = [2,1,4,9]

dp1 = [-1] * (len(house)-1)
dp2 = [-1] * (len(house)-1)

def house_robber_2(n, arr, dp):
    if n == 0:
        return arr[n]
    if n < 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    pick = arr[n] + house_robber_2(n-2, arr, dp)
    not_pick = house_robber_2(n-1, arr, dp)
    dp[n] = max(pick, not_pick)
    return dp[n]

first = house[:len(house)-1]
second = house[1:]

first_ans, second_ans = house_robber_2(len(first)-1, first, dp1), house_robber_2(len(second)-1, second, dp2)

print(max(first_ans, second_ans))

