számok = [3, 2, 5]
gyümölcsök = ['alma', 'körte', 'barack']
vegyes = ['alma', 5, True]

számok[2] = 7


print(számok)

for i in range(len(számok)):
  print(i, számok[i])


lista = 4 * [0]
print(lista) # [0, 0, 0, 0]

lista = [i for i in range(4)]
print(lista) # [0, 1, 2, 3]

lista = [i for i in range(8) if i % 2 == 0]
print(lista) # [0, 2, 4, 6]

lista = [2 * i for i in range(4)]
print(lista) # [0, 2, 4, 6]lista származtatás(list comprehension)

# Elem hozzáadása
számok.append(4)
print(számok) # [3, 2, 7, 4]

számok.insert(2, 8)
print(számok) # [3, 2, 8, 7, 4]

# Elem törlése
törölt = számok.pop(1)
print(számok) # [3, 8, 7, 4]
print(törölt) # 2

# Két lista összefűzése
számok.extend([1, 6, 2])
print(számok) # [3, 8, 7, 4, 1, 6, 2]

összefűzött_lista = [3, 8, 7, 4] + [1, 6, 2]
print(összefűzött_lista) # [3, 8, 7, 4, 1, 6, 2]

# Tartalmazás ellenőrzések
print(számok) # [3, 8, 7, 4, 1, 6, 2]
if 1 in számok:
    print('1 benne van a listában')
if 5 not in számok:
    print('5 nincs benne a listában')

# Rendezés
print(számok) # [3, 8, 7, 4, 1, 6, 2]
rendezett = sorted(számok)
print(számok) # [3, 8, 7, 4, 1, 6, 2]
print(rendezett) # [1, 2, 3, 4, 6, 7, 8]

print(számok) # [3, 8, 7, 4, 1, 6, 2]
számok.sort()
print(számok) # [1, 2, 3, 4, 6, 7, 8]

számok = [3, 8, 7, 4, 1, 6, 2]
számok.sort(reverse=True)
print(számok) # [8, 7, 6, 4, 3, 2, 1]





  
