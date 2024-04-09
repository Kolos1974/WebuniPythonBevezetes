törpök = {'Tudor', 'Vidor', 'Morgó', 'Szundi', 'Szende', 'Hapci', 'Kuka'}
talált = set()
hibás = set()
while True:
    törp = input('Törpnév: ')
    if törp == '':break
    elif törp in talált: print('Helyes, de már volt.')
    elif törp in törpök: print('Helyes!'); talált.add(törp)
    else: hibás.add(törp); print('Helytelen.')

print(f'Találatok száma: {len(talált)}')
print('Eltaláltak: ' + ', '.join(talált))
print('Hibás tippek: ' + ', '.join(hibás))
print('Hiányzók: ' + ', '.join(törpök.difference(talált)))
print('Hiányzók: ' + ', '.join(törpök - talált))
