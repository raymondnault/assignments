'''

Raymond Nault
Chapter 6: Dictionaries

'''

# this code will create a dictionary of people and their favorite programming languages

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'java',
    
}

people_to_poll = ['jen', 'sarah', 'edward', 'phil', 'raymond', 'tommy']
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you for taking the poll, {person.title()}!")
    else:
        print(f"{person.title()}, please take our poll!")
