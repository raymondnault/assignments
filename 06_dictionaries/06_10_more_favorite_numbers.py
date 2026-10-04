'''

Raymond Nault
Chapter 6: Dictionaries

'''

# this code will create a dictionary of favorite numbers for different people

favorite_numbers = {
    'Raymond': [7, 14, 21],
    'Alice': [3, 6, 9],
    'Gary': [1, 2, 3]
}

for person, numbers in favorite_numbers.items():
    print(f"{person}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")
    print()