gyümölcs_szótár = {
    'alma': 'apple',
    'banán': 'banana',
    'narancs': 'orange',
}

üres_szótár = {}


üres_szótár = dict()


# Lekérdezés

print(gyümölcs_szótár['alma']) # apple

for gyümölcs in gyümölcs_szótár:
    print(gyümölcs, gyümölcs_szótár[gyümölcs])

# alma apple
# banán banana
# narancs orange


# Módosítás

gyümölcs_szótár['ananász'] = 'ananas'

gyümölcs_szótár['ananász'] = 'pineapple'

print(gyümölcs_szótár.pop('alma')) # apple


# Tartalmazás vizsgálat

if 'banán' in gyümölcs_szótár:
    print('A banán benne van a szótárban')
if'alma'not in gyümölcs_szótár:
    print('Az alma nincs benne a szótárban')

# Rendezés érték szerint

épületek = {
    'Burdzs Kalifa': 828,
    'Eiffel-torony': 325,
    'Lakihegyi rádiótorony': 314,
    'One World Trade Center': 541,
    'Petronas-ikertorony': 452,
}
rendezett = dict(sorted(épületek.items(), key=lambda épület: épület[1], reverse=True))
print(rendezett)
# {
#     'Burdzs Kalifa': 828,
#     'One World Trade Center': 541,
#     'Petronas-ikertorony': 452,
#     'Eiffel-torony': 325,
#     'Lakihegyi rádiótorony': 314
# }











