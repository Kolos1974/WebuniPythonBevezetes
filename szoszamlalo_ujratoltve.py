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

from collections import Counter
print(Counter(szavak))

# Counter({'róka': 16, 'rege': 8, 'a': 2, 'három': 1, 'görbe': 1,
# 'legényke': 1, 'tojást': 1, 'lopott': 1, 'ebédre': 1, 'lett': 1,
# 'belőle': 1, 'rántotta': 1, 'kutya': 1, 'lerántotta': 1, 'egyik': 1,
# 'szidta': 1, 'gazdáját': 1, 'másik': 1, 'meg': 1, 'fajtáját': 1,
# 'harmadik': 1, 'az': 1, 'ükapját': 1, 'hozzávágta': 1, 'kalapját': 1})

