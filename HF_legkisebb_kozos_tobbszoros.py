def legnagy_kozos_oszto(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def legkisebb_kozos_tobbszoros(a, b):
    return (a * b) // legnagy_kozos_oszto(a, b)


print(legkisebb_kozos_tobbszoros(30, 12))
      
        
