# Lottósorsolás

def faktorialis(n):
    if n <= 1:
        return 1
    else:
        return n * faktorialis(n-1)


def ismetles_nelkuli_kombinacio(n, k):
    return (faktorialis(n)//faktorialis(k)*faktorialis(n-k))

print(ismetles_nelkuli_kombinacio(90, 5))

print('')
print("---")
print(faktorialis(5))
print("---")
print(faktorialis(85))
print("---")
print(faktorialis(90))
print("---")
print(faktorialis(90)//faktorialis(5)*faktorialis(85))
