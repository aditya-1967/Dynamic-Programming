x = "abcdgh"
y = "abedfhr"
m = len(x)
n = len(y)

#Recursive
def lcs(x,y,n,m):
    if n == 0 or m == 0:
        return 0
    if x[n-1] == y[m-1]:
        return 1 + lcs(x,y,n-1, m-1)
    else:
        return max(lcs(x,y,n,m-1), lcs(x,y,n-1,m))

print(lcs(x,y,m,n))

#Memoization
dp = [[-1 for j in range(n+1)]for j in range(m+1)]

def lcs(x,y,m,n):
    if n == 0 or m == 0:
        return 0
    if dp[m][n] != -1:
        return dp[m][n]
    if x[m-1] == y[n-1]:
        dp[m][n] = 1 + lcs(x,y,m-1, n-1)
        return dp[m][n]
    else:
        dp[m][n] = max(lcs(x,y,m-1,n), lcs(x,y,m,n-1))
        return dp[m][n]

lcs(x,y,m,n)
print(dp[m][n])

#Top-Down
dp = [[-1 for j in range(n+1)]for j in range(m+1)]
for i in range(m+1):
    for j in range(n+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
for i in range(1, m+1):
    for j in range(1, n+1):
        if x[i-1] == y[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[m][n])




