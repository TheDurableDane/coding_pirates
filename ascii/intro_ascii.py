"""
Simpelt program der introducerer ASCII.
Keywords: string, list, for-loop, conditioning/branching/if

author: Thomas Lolk Schmidt
email: thomaslolkschmidt@gmail.com
date: 04feb2017
"""

# Første opgave: Oversæt koden ved brug af ASCII-tabellen i papirudgave.
kode = [97, 98, 99, 100]
tekst = ""

for i in kode:
    if i == 97:
        tekst = tekst + 'a'
    elif i == 98:
        tekst = tekst + 'b'
    elif i == 99:
        tekst = tekst + 'c'
    elif i == 100:
        tekst = tekst + 'd'

print(tekst)


# Anden opgave: Oversæt den nye kode ved brug af indbyggede funktioner.
kode = [67, 111, 100, 105, 110, 103, 32, 80, 105, 114, 97, 116, 101, 115, 33]

tekst = ""
for i in kode:
    tekst = tekst + chr(i)
    
print(tekst)
