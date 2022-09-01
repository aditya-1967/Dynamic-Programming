# Cherry Pickup II
# 3D DP

mat = [[2, 3, 1, 2],
       [3, 4, 2, 2],
       [5, 6, 3, 5]]

m, n = len(mat), len(mat[0])

dp = [[[-1 for k in range(n+1)] for j in range(n+1)] for i in range(m+1)]

def cherry_pick(i, j1, j2):
    if j1 < 0 or j2 < 0 or j1 >= n or j2 >= n:
        return -10**9
    if i == m - 1:
        if j1 == j2:
            return mat[i][j1]
        else:
            return mat[i][j1] + mat[i][j2]
    if dp[i][j1][j2] != -1:
        return dp[i][j1][j2]

    maximum = 0
    for dj1 in range(-1, 2):
        for dj2 in range(-1, 2):
            if j1 == j2:
                value = mat[i][j1] + cherry_pick(i+1, j1+dj1, j2+dj2)
            else:
                value = mat[i][j1] + mat[i][j2] + cherry_pick(i+1, j1+dj1, j2+dj2)
            maximum = max(maximum, value)
    
    dp[i][j1][j2] = maximum
    return dp[i][j1][j2]

print(cherry_pick(0, 0, n-1))