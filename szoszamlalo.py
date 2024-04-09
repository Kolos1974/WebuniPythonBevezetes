szöveg = '''
Három görbe legényke, róka rege róka,
Tojást lopott ebédre, róka rege róka,
Lett belőle rántotta, róka rege róka,
A kutya lerántotta, róka rege róka.
Egyik szidta gazdáját, róka rege róka,
Másik meg a fajtáját, róka rege róka,
Harmadik az ükapját, róka rege róka,
Hozzávágta kalapját, róka rege róka.'''

szavak = szöveg.lower().replace(',', '').replace('.', '').split()
# print(szavak)

# ['három', 'görbe', 'legényke', 'róka', 'rege', 'róka', 'tojást',
# 'lopott', 'ebédre', 'róka', 'rege', 'róka', 'lett', 'belőle',
# 'rántotta', 'róka', 'rege', 'róka', 'a', 'kutya', 'lerántotta',
# 'róka', 'rege', 'róka', 'egyik', 'szidta', 'gazdáját', 'róka',
# 'rege', 'róka', 'másik', 'meg', 'a', 'fajtáját', 'róka', 'rege',
# 'róka', 'harmadik', 'az', 'ükapját', 'róka', 'rege', 'róka',
# 'hozzávágta', 'kalapját', 'róka', 'rege', 'róka']

szavak_száma = {}

for szó in szavak:
    if szó not in szavak_száma:
        szavak_száma[szó] = 1
    else:
        szavak_száma[szó] = szavak_száma[szó] + 1

print(szavak_száma)

# {'három': 1, 'görbe': 1, 'legényke': 1, 'róka': 16, 'rege': 8,
# 'tojást': 1, 'lopott': 1, 'ebédre': 1, 'lett': 1, 'belőle': 1,
# 'rántotta': 1, 'a': 2, 'kutya': 1, 'lerántotta': 1, 'egyik': 1,
# 'szidta': 1, 'gazdáját': 1, 'másik': 1, 'meg': 1, 'fajtáját': 1,
# 'harmadik': 1, 'az': 1, 'ükapját': 1, 'hozzávágta': 1, 'kalapját': 1}


szavak_száma_rendezett = sorted(szavak_száma.items(), key=lambda x: x[1], reverse=True)
for szó_szám in szavak_száma_rendezett:
    if szó_szám[1] > 1:
        print(szó_szám[0], szó_szám[1])

# róka 16
# rege 8
# a 2





