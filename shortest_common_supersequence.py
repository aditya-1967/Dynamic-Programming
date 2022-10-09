# Shortest Common Supersequence
# DP on Strings

s1 = "brute"
s2 = "groot"

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

print(m + n - lcs(m, n))

# printing shortest common supersequence

length = lcs(m, n)
i, j = m, n
res = ""


while i > 0 and j > 0:
    if s1[i-1] == s2[j-1]:
        res += s1[i-1]
        i -= 1
        j -= 1
    elif dp[i-1][j] > dp[i][j-1]:
        res += s1[i-1]
        i -= 1
    else:
        res += s2[j-1]
        j -= 1

while i > 0:
    res += s1[i-1]
    i -= 1

while j > 0:
    res += s2[j-1]
    j -= 1

print(res[::-1])