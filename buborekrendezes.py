def buborékrendezés(számok):
    történt_változás = True
    while történt_változás:
        történt_változás = False
        for i in range(len(számok)-1):
            if számok[i] > számok[i+1]:
                számok[i], számok[i+1] = számok[i+1], számok[i]
                történt_változás = True

def buborékrendezés_classic(számok):
    for i in range(len(számok)-1):
        for j in range(len(számok)-i):
            if számok[i] > számok[i+j]:
                számok[i], számok[i+j] = számok[i+j], számok[i]


számok = [3, 4, 1, 2]
buborékrendezés(számok)
print(számok)

számok = [3, 4, 1, 2]
buborékrendezés_classic(számok)
print(számok)
