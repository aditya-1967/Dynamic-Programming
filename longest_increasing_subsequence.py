# Longest Increasing Subsequence
# DP on Increasing Subsequence

arr = [10, 9, 2, 5, 3, 7, 101, 18]
n = len(arr)

dp = [[-1] * (n+1) for _ in range(n+1)]

def lis(ind, prev):
    if ind == n:
        return 0
    if dp[ind][prev + 1] != -1:
        return dp[ind][prev + 1]
    length = lis(ind + 1, prev)
    if prev == -1 or arr[ind] > arr[prev]:
        length = max(length, 1 + lis(ind + 1, ind))
    dp[ind][prev + 1] = length
    return dp[ind][prev+1]

print(lis(0, -1))  