"""
Hangman

author: Thomas Lolk Schmidt
email: thomaslolkschmidt@gmail.com
date: 09mar2017
"""

import time


def findIndices(word, character):
    indices = []
    for i in range(len(word)):
        if word[i] == character:
            indices.append(i)

    return indices


# Ordet der skal gættes
kodeord = 'Kodeord'

# Antal gange man må gætte forkert
liv = 1

# Initialisér variable
kodeord = list(kodeord.lower())
bogstaver_forkert = []
bogstaver_korrekt = []
for b in kodeord:
    bogstaver_korrekt.append('x')

# Let the game begin!
while bogstaver_korrekt != kodeord and liv > 0:
    # Print start
    print("\nGæt ordet: ", ' '.join(bogstaver_korrekt))
    gaet = input("\nGæt et bogstav og tryk <enter>: ").lower()

    # Tag højde for fejl-input
    if len(gaet) == 1:
        # Find ud af om bogstavet er korrekt eller forkert
        if gaet in kodeord:
            idx = findIndices(kodeord, gaet)
            for i in idx:
                bogstaver_korrekt[i] = gaet
            print("Korrekt!")
        else:
            bogstaver_forkert += gaet
            liv -= 1
            print("Forkert, din n00b!")

        # Print spillets nuværende score
        antal_forkerte_str = str(len(bogstaver_forkert))
        print(antal_forkerte_str, "forkert(e) gæt: ", ', '.join(bogstaver_forkert))
        print("Tilbageværende liv: ", str(liv), '\n')

    # Hvis længden af input-strengen er forkert:
    else:
        print("Gæt kun ét bogstav ad gangen.")

    time.sleep(2)

# Print afgørelsen
if liv < 1:
    print("n00b! Du tabte. Ordet er: ", ''.join(kodeord))
else:
    print("Tillykke, du vandt! Ordet er: ", ''.join(kodeord))
