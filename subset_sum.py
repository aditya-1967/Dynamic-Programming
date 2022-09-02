# Subset Sum Equal to Target
# DP on Subsequences

arr = [2, 3, 1, 1]
target = 4

dp = [[-1] * (10**3 + 1) for i in range(10**3 + 1)]

def subset_sum(i, target):
    if target == 0:
        return True
    if i == 0:
        return arr[0] == target
    if dp[i][target] != -1:
        return dp[i][target]
    
    notPick = subset_sum(i-1, target)
    pick = False
    if target >= arr[i]:
        pick = subset_sum(i-1, target - arr[i])
    dp[i][target] = pick or notPick
    return dp[i][target]


print(subset_sum(len(arr)-1, target))