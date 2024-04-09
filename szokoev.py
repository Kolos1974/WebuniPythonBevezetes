év = 2000
print(év)
if év % 4 != 0:
    print('Nem szökőév')
elif év % 400 == 0:
    print('Szökőév')
elif év % 100 == 0:
    print('Nem szökőév')
else:
    print('Szökőév')

    
