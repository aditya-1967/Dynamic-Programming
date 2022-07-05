
# Online Python - IDE, Editor, Compiler, Interpreter

n = int(input("Enter a number: "))
dp = [-1]*(n+1)
def fibo(n):
    if n <= 1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]

print(fibo(n))
