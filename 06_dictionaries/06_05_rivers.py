'''

Raymond Nault
Chapter 6: Dictionaries

'''

# this code will create a dictionary of rivers and the countries they flow through

rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'united states',
}

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")