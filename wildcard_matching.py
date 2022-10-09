# Wildcard Matching
# DP on Strings

s1 = '?ay'
s2 = 'ray'
m, n = len(s1), len(s2)

dp = [[False] * (n + 1) for _ in range(m+1)]

def wildcard(m, n):
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 and j == 0:
                dp[i][j] = True
            if i == 0 and j > 0:
                dp[i][j] = False
            if j == 0 and i > 0:
                flag = True
                for k in range(i):
                    if s1[k-1] != '*':
                        flag = False
                        break
                dp[i][j] = flag
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1] or s1[i-1] == '?':
                dp[i][j] = dp[i-1][j-1]
            elif s1[i-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
            else:
                dp[i][j] = False
    
    return dp[m][n]

print(wildcard(m, n))