n=5

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

fator = factorial(n)
print(fator)