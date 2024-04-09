'''
    Nem használhatóak a ||, && oparátorok!!
    (Viszont van olyan operátor, hogy |, & ! Ezekre figyelni kell!!)

    A néggyel való oszthatóságnál nem a kiinduló évvel kell számolni, hanem a
    változással!!

    Csak a nagybetűs logikai értékeket ismeri!!
'''


def teli_olimpia(ev):
    if ev == 1940 or ev ==1944:
        return False
    elif ev>=1924 and ev<=1992 and (ev-1924)%4==0:
        return True
    elif ev>=1994 and ev<=2022 and (ev-1994)%4==0:
        return True
    else:
        return False

print(teli_olimpia(1940)) # False

print(teli_olimpia(1930)) # False
print(teli_olimpia(1932)) # True

print(teli_olimpia(2000)) # False
print(teli_olimpia(2002)) # True

print(teli_olimpia(2000)) # False
