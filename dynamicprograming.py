n=10

def fib_dp(n):
    dp_sols = {0:1,1:1}
    for i in range(2,n+1):
        dp_sols[i] = dp_sols[i-1] + dp_sols[i-2] 
    return dp_sols[n]

result = fib_dp(n)
print(result)