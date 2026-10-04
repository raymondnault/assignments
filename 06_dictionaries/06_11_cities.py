'''

Raymond Nault
Chapter 6: Dictionaries

'''

# this code will create a dictionary of cities and their information

cities = {
    'Mexico City': {
        'country': 'Mexico',
        'population': 8918653,
        'fact': 'It is the largest city in North America.'
    },
    'New York': {
        'country': 'USA',
        'population': 8419600,
        'fact': 'It is known as the "Big Apple".'
    },
    'Paris': {
        'country': 'France',
        'population': 2140526,
        'fact': 'It is known as the "City of Light".'
    }
 }

for city, info in cities.items():
    print(f"Information about {city}:")
    print(f"- Country: {info['country']}")
    print(f"- Population: {info['population']}")
    print(f"- Fact: {info['fact']}")
    print()