'''

Raymond Nault
Chapter 6: Dictionaries

'''

# this code will create a dictionary of people and their information

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

for person in people:
    print(person['first_name'])
    print(person['last_name'])
    print(person['age'])
    print(person['city'])