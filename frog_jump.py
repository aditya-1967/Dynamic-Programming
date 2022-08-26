# Frog Jump
# 1D DP

heights = [30, 10, 60, 10, 60, 50]

n = len(heights) - 1
dp = [-1] * (n + 1)

def frog_jump(n):
    if n == 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    left = frog_jump(n-1) + abs(heights[n] - heights[n-1])
    right = float('inf')
    if n > 1:
        right = frog_jump(n-2) + abs(heights[n] - heights[n-2])
    dp[n] = min(left, right)
    return dp[n]

print(frog_jump(n))