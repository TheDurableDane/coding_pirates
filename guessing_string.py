"""
Randomly guessing a string

author: Thomas Lolk Schmidt
email: thomaslolkschmidt@gmail.com
date: 11mar2017
"""

import string
import random
import time

# Streng der skal gættes
hemmelig_streng = list('Jeg er en pirat. Arrr!')

# Mulige tegn i streng der skal gættes
mulige_tegn = list(string.ascii_letters + string.punctuation + ' ')

# Initialisér variable
min_streng = ['']*len(hemmelig_streng)
iterationer = 0

while min_streng != hemmelig_streng:
    for i in range(len(hemmelig_streng)):
        if min_streng[i] != hemmelig_streng[i]:
            min_streng[i] = mulige_tegn[random.randint(0, len(mulige_tegn)-1)]

    print(''.join(min_streng))
    time.sleep(0.5)
    iterationer += 1

time.sleep(2)
print("\nDen korrekte streng blev gættet i løbet af %i iterationer." %iterationer)
