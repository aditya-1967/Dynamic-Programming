# Partition Equal Subset Sum
# DP on Subsequences

arr = [2, 3, 3, 3, 4, 5]

dp = [[-1] * (10**3 + 1) for i in range(10**3 + 1)]


def partition_sum(i, target):
    if target == 0:
        return True
    if i == 0:
        return arr[0] == target
    if dp[i][target] != -1:
        return dp[i][target]
    
    notPick = partition_sum(i-1, target)
    pick = False
    if target >= arr[i]:
        pick = partition_sum(i-1, target - arr[i])
    dp[i][target] = pick or notPick
    return dp[i][target]

if len(arr) % 2 != 0:
    print(False)
else:
    target = sum(arr) // 2
    print(partition_sum(len(arr)-1, target))