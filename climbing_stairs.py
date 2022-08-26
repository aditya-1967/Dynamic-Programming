# Climbing Stairs
# 1D - DP

n = int(input('Enter the number of steps: '))
dp = [-1]*(n+1)

def climb(n):
    if n <= 1: 
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = climb(n-1) + climb(n-2)
    return dp[n]

print(climb(n))