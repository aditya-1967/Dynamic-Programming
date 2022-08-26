# Frog Jump with k distance
# 1D DP

heights = [30, 10, 60, 10, 60, 50]
k = 5

n = len(heights) - 1
dp = [-1] * (n + 1)

def frog_jump_k(n):
    if n == 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    min_steps = float('inf')
    for i in range(1, k+1):
        if n > 0:
            jump = frog_jump_k(n - i) + abs(heights[n] - heights[n-i])
            min_steps = min(min_steps, jump)
    dp[n] = min_steps
    return dp[n]

print(frog_jump_k(n))
     