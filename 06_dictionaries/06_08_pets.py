'''

Raymond Nault
Chapter 6: Dictionaries

'''

# this code will create a dictionary of pets and their information

from unicodedata import name


pets = [
    {
        'name': "ButterCup",
        'species': "Dog",
        'pet age': 10,
        'owner': "Raymond"
    },
    {
        'name': "Mittens",
        'species': "Cat",
        'pet age': 3,
        'owner': "Alice"
    },
    {
        'name': "Goldie",
        'species': "Fish",
        'pet age': 1,
        'owner': "Gary"
    }
]

for pet in pets:
    print(pet['name'])
    print(pet['species'])
    print(pet['pet age'])
    print(pet['owner'])
    