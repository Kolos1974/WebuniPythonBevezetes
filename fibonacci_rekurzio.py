def faktoriális(n):
    if n <= 1:
        return 1
    else:
        return n * faktoriális(n-1)
print(faktoriális(5))
