'''

Raymond Nault
Chapter 6: Dictionaries

'''

# this code will create a dictionary of favorite places for different people

favorite_places = {
    'Raymond': ["Mexico City", "New York", "Paris"],
    'Alice': ["London", "Tokyo", "Berlin"],
    'Gary': ["Sydney", "Toronto", "Rome"]
}

for person, places in favorite_places.items():
    print(f"{person}'s favorite places are:")
    for place in places:
        print(f"- {place}")
    print()