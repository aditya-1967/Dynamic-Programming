# Rod Cutting Problem
# DP on Subsequences

length = 5
price = [2, 5, 7, 8, 10]

dp = [[-1] * (length+1) for _ in range(len(price) + 1)]

def rod_cutting(index, l):
    if index == 0:
        return l * price[0]
    if dp[index][l] != -1:
        return dp[index][l]
    
    notCut = rod_cutting(index - 1, l)
    cut = float('-inf')
    if index + 1 <= l:
        cut = price[index] + rod_cutting(index, l - (index + 1))
    
    dp[index][l] = max(cut, notCut)
    
    return dp[index][l]

print(rod_cutting(len(price) - 1, length))