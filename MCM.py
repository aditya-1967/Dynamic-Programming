#Recursive

arr = [40, 20, 30, 10, 30]

i, j = 1, len(arr) - 1

def solve(arr, i, j):
    if i >= j:
        return 0
    mini = float("inf")
    for k in range(i, j):
        temp_ans = solve(arr, i, k) + solve(arr, k+1, j) + (arr[i-1]*arr[k]*arr[j])
        if temp_ans < mini:
            mini = temp_ans
    return mini

print(solve(arr, i, j))

#Memoization


dp = [[-1 for j in range(len(arr)+1)]for i in range(len(arr)+1)]

def solve(arr, i, j):
    if i >= j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    mini = float("inf")
    for k in range(i, j):
        temp_ans = solve(arr, i, k) + solve(arr, k+1, j) + (arr[i-1]*arr[k]*arr[j])
        if temp_ans < mini:
            mini = temp_ans
    dp[i][j] = mini
    return dp[i][j]



print(solve(arr, i, j))
