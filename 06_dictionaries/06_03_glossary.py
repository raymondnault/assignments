'''

Raymond Nault
Chapter 6: Dictionaries

'''

# this program will store programming terms and their definitions into a dictionary

glossary = {
    'variable':'A storage location in memory for storing data',
    'function':'A block of organized, reusable code that performs a single action',
    'loop':'A sequence of instructions that repeats until a certain condition is met',
    'dictionary':'A collection of key-value pairs in Python',
    'list':'An ordered collection of items in Python'
}

for term, definition in glossary.items():
    print(f"{term}: {definition}")
