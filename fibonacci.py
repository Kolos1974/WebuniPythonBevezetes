n = 6
a = 0
b = 1
for i in range(n):
    temp = b
    b = a + b
    a = temp
print(a)
