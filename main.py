

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(m):
    if m == 0:
        return 0
    elif m == 1:
        return 1
    else:
        return fibonacci(m - 1) + fibonacci(m-2)

n = factorial(3)
m = fibonacci(3)

print(n, m)