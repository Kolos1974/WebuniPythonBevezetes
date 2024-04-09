def fibonacci(n):

    '''
    fibonacci_szám = []
    for i in range(n+1):
        fibonacci_szám.append(None)
    '''

    fibonacci_szám = (n+1) * [None]

        
    def fibonacci_rekurzió(x):
        if fibonacci_szám[x] is not None:
            return fibonacci_szám[x]
        if x <= 1:
            eredmény = x
        else:
            eredmény = fibonacci_rekurzió(x-1) + fibonacci_rekurzió(x-2)
        fibonacci_szám[x] = eredmény
        return eredmény
    return fibonacci_rekurzió(n)

print(fibonacci(6))  #8

