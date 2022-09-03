# Partition a array into two different subsets with min abs sub difference
# DP on Subsequences

arr = [3, 2, 7]
total = sum(arr)



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

s1 = []
for i in range(1, total+1):
    dp = [[-1] * (10**3 + 1) for i in range(10**3 + 1)]
    if subset_sum(len(arr)-1, i):
        s1.append(i)

s2 = [total - i for i in s1]
abs_diff = [abs(s1[i] - s2[i]) for i in range(len(s1))]
print(min(abs_diff))