def fib_num(n):
    if (n == 0) or (n == 1):
        return n
    return fib_num(n-1) + fib_num(n-2)
