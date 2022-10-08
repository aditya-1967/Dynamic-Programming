# Longest Commom Substring
# DP on Strings

s1 = "abcjk"
s2 = "acjkp"
m, n = len(s1), len(s2)

dp = [[-1] * (n+1) for _ in range(m+1)]

def lcs(m, n):
    ans = 0
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                ans = max(ans, dp[i][j])
            else:
                dp[i][j] = 0
    
    return ans

print(lcs(m, n))