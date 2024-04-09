# Belső könyvtárak:

import math
print(math.gcd(30, 12)) # 6

from math import gcd
print(gcd(30, 12)) # 6


# Külső könyvtárak

pip install numpy

import numpy as np
tömb1 = np.array([3, 2, 5])
tömb2 = np.array([2, 4, 1])
print(tömb1 * tömb2) # [6 8 5]


