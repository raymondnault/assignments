'''

Raymond Nault
Chapter 6: Dictionaries

'''

# will extend the dictionary of people by adding their favorite programming languages

people = [
    {
        'first_name': "Raymond",
        'last_name': "Nault",
        'age': 21,
        'city': "Milltown"
    },
    {
        'first_name': "Bob",
        'last_name': "Smith",
        'age': 30,
        'city': "New York"
    },
    {
        'first_name': "Alice",
        'last_name': "Johnson",
        'age': 25,
        'city': "Los Angeles"   
    }
]

# adding favorite programming languages to each person
for person in people:
    if person['first_name'] == "Raymond":
        person['favorite_language'] = "Python"
    elif person['first_name'] == "Bob":
        person['favorite_language'] = "JavaScript"
    elif person['first_name'] == "Alice":
        person['favorite_language'] = "C++"

# printing all info
for person in people:
    print(f"Information about {person['first_name']} {person['last_name']}:")
    print(f"- Age: {person['age']}")
    print(f"- City: {person['city']}")
    print(f"- Favorite Programming Language: {person['favorite_language']}")
    print()