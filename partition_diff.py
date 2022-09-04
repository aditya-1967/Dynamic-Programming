# Count Partition with given difference
# DP on Subsequences

arr = [5, 2, 6, 4]
diff = 3

dp = [[-1] * (10**3 + 1) for i in range(10**3 + 1)]

def subset_count(index, target):
    if target == 0:
        return 1
    if index == 0:
        return 1 if arr[index] == target else 0
    if dp[index][target] != -1:
        return dp[index][target]

    notPick = subset_count(index - 1, target)
    pick = 0
    if arr[index] <= target:
        pick = subset_count(index - 1, target - arr[index])
    
    dp[index][target] = pick + notPick
    return dp[index][target]

if (sum(arr) - diff) < 0 or (sum(arr) - diff) % 2 != 0:
    print(0)
    
else:
    target = (sum(arr) - diff) // 2
    print(subset_count(len(arr) - 1, target))