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


    def fibonacci_rekurziv(x):
        if fibonacci_szám[x] is None:
            if x <= 1:
                fibonacci_szám[x] = x
            else:
                fibonacci_szám[x] = fibonacci_rekurziv(x-1) + fibonacci_rekurziv(x-2)
        return fibonacci_szám[x]

    # return fibonacci_rekurzió(n)

    return fibonacci_rekurziv(n)


print(fibonacci(6))   #8
print(fibonacci(35))  #9227465

for i in range(50):
    print(i, fibonacci(i))
    
