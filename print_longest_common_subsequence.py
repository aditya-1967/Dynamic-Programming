# Print Longest Commom Sunsequence
# DP on Strings

s1 = "adebc"
s2 = "dcadb"
m, n = len(s1), len(s2)

dp = [[-1] * (n+1) for _ in range(m+1)]

def lcs(m, n):
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

length = lcs(m, n)

i, j = m, n
res = []
index = length - 1

for l in range(length):
    res.append('$')

while i > 0 and j > 0:
    if s1[i-1] == s2[j-1]:
        res[index] = s1[i-1]
        index -= 1
        i -= 1
        j -= 1
    elif dp[i-1][j] > dp[i][j-1]:
        i -= 1
    else:
        j -= 1

print("".join(res))