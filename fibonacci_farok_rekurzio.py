def fibonacci(n, a=0, b=1):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibonacci(n-1, b, a+b)
print(fibonacci(6))
