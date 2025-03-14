import timeit
from functools import reduce

# Рекурсивно
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

# Циклічно
def factorial_loop(n):
    fact = 1
    for i in range(1, n + 1):
        fact = i * fact
    return fact

def fibonacci_loop(n):
    a = 0
    b = 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

# Reduce
def factorial_reduce(n):
    if n == 0:
        return 1
    else:
        return reduce(lambda x, y: x * y, range(1, n + 1))

def fibonacci_reduce(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    s = reduce(lambda x, _: (x[1], x[0] + x[1]), range(n - 1), (0, 1))
    return s[1]

# Вимірювання часу
def benchmark():
    ex = 10
    n_repeats = 10  # Кількість повторень

    time_factorial_rec = timeit.timeit(lambda: factorial_rec(ex), number=n_repeats)
    time_factorial_loop = timeit.timeit(lambda: factorial_loop(ex), number=n_repeats)
    time_factorial_reduce = timeit.timeit(lambda: factorial_reduce(ex), number=n_repeats)
    time_fibonacci_rec = timeit.timeit(lambda: fibonacci_rec(ex), number=n_repeats)
    time_fibonacci_loop = timeit.timeit(lambda: fibonacci_loop(ex), number=n_repeats)
    time_fibonacci_reduce = timeit.timeit(lambda: fibonacci_reduce(ex), number=n_repeats)

    print(f"Факторіал рекурсивно = {factorial_rec(ex)} (час: {time_factorial_rec} секунд)\n"
          f"Фібоначчі рекурсивно = {fibonacci_rec(ex)} (час: {time_fibonacci_rec} секунд)\n"
          f"Факторіал циклом = {factorial_loop(ex)} (час: {time_factorial_loop} секунд)\n"
          f"Фібоначчі циклом = {fibonacci_loop(ex)} (час: {time_fibonacci_loop} секунд)\n"
          f"Факторіал reduce = {factorial_reduce(ex)} (час: {time_factorial_reduce} секунд)\n"
          f"Фібоначчі reduce = {fibonacci_reduce(ex)} (час: {time_fibonacci_reduce} секунд)")

benchmark()
