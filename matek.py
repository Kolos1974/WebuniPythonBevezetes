# matek.py

def kerekített_összead(a, b):
    c = a + b
    if round(c, 6) == round(c, 9):
        return round(c, 6)
    else:return c

