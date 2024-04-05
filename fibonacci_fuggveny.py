def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a

for i in range(1, 10):
    print(i, fibonacci(i))
    
# 1 1
# 2 1
# 3 2
# 4 3
# 5 5
# 6 8
# 7 13
# 8 21
# 9 34
