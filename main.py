

def factorial_rec(n):
    if n == 0:
        return 1
    else:
        return n * factorial_rec(n-1)

def fibonacci_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n-2)

def factorial_loop(n):
    fact = 1
    for i in range(1,n + 1):
        fact = i *fact
    return fact

def fibonacci_loop(n):
    a = 0
    b = 1
    for i in range(2,n + 1):
        a, b = b, a + b
    return b


ex = 5
print(f"Факторіал рекурсивно = {factorial_rec(ex)},\n"
      f"Фібоначчі рекурсивно = {fibonacci_rec(ex)},\n"
      f"Факторіал циклом = {factorial_loop(ex)},\n"
      f"Фібоначчі циклом = {fibonacci_loop(ex)}")