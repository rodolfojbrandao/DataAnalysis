n=10
memo = {}
def fib_memo(n):
    if n in memo:
        return memo[n]
    if n<=1:
        memo[n]=1
        return 1
    memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]
result= fib_memo(n)
print(result)
print(memo)