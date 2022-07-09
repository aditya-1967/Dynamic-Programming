def subsetsum(arr, total):
  dp = [[None for j in range(total+1)] for i in range(len(arr)+1)]
  for i in range(len(arr)+1):
    for j in range(total+1):
      if i == 0:
        dp[i][j] = False
      if j == 0:
        dp[i][j] = True
  for i in range(1, len(arr)+1):
    for j in range(1, total+1):
      if arr[i-1] <= j:
        dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
      else:
        dp[i][j] = dp[i-1][j]
  return dp[len(arr)][total]
