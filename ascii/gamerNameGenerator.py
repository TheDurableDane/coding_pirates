"""
Gamer Name Generator

author: Thomas Lolk Schmidt
email: thomaslolkschmidt@gmail.com
date: 29jan2017
"""

gamer_first_list = ['Dark', 'Bright', 'Stormy', 'Fallen', 'Exalted', 'Fiery',
                    'Icy', 'Blaze', 'Frost', 'Evil', 'Pure', 'Sweet', 'Fresh',
                    'Old', 'New', 'Vile', 'Devine', 'Foul', 'Shine', 'Dead',
                    'Dull', 'Holy', 'Grim', 'Cheer', 'Thunder', 'Wicked']
                    
gamer_last_list = ['Lily', 'Rose', 'Star', 'Dawn', 'Demon', 'Dragon', 'One',
                   'Twin', 'Bunny', 'Griffon', 'Slayer', 'Sky', 'Fiend',
                   'Lord', 'Skull', 'Rain', 'Flash', 'Dread', 'Doom', 'Smoke',
                   'Fist', 'Hammer', 'Maul', 'Rock', 'Child', 'Rage']

first_name = input("What is your firstname? ")
last_name = input("What is your lastname? ")

first_initial = first_name[0].lower()
last_initial = last_name[0].lower()

gamer_first = gamer_first_list[ord(first_initial) - 97]     # Look up ASCII conversion to find the reason behind 97
gamer_last = gamer_last_list[ord(last_initial) - 97]

print("\nYour gamer name is: ", gamer_first, gamer_last)
