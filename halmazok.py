számhalmaz = {3, 2, 5}
print(számhalmaz) # {2, 3, 5}

for elem in számhalmaz:
    print(elem)
# 2
# 3
# 5

üres_halmaz = set()

# Elem hozzáadása:

print(számhalmaz) # {2, 3, 5}
számhalmaz.add(4)
print(számhalmaz) # {2, 3, 4, 5}

számhalmaz.add(2)
print(számhalmaz) # {2, 3, 4, 5}

számhalmaz.update({1, 7})
print(számhalmaz) # {1, 2, 3, 4, 5, 7}

# Elem törlése:

számhalmaz.add(9)
számhalmaz.update({2, 8})
print(számhalmaz) # {1, 2, 3, 4, 5, 7, 8, 9}
számhalmaz.remove(9)
print(számhalmaz) # {1, 2, 3, 4, 5, 7, 8}


'számhalmaz.remove(6)'
# KeyError: 6

számhalmaz.discard(6)
print(számhalmaz) # {1, 2, 3, 4, 5, 7, 8}

elem = számhalmaz.pop()
print(elem) # 1
print(számhalmaz) # {2, 3, 4, 5, 7, 8}

# Tartalmazási vizsgálat
print(számhalmaz) # {2, 3, 4, 5, 7, 8}
if 3 in számhalmaz:
    print('A 3 benne van a halmazban.')
if 6 not in számhalmaz:
    print('A 6 nincs benne a halmazban.')

    





