'''

Raymond Nault
Chapter 6: Dictionaries

'''

# adding more terms to previous glossary

glossary = {
    'variable':'A storage location in memory for storing data',
    'function':'A block of organized, reusable code that performs a single action',
    'loop':'A sequence of instructions that repeats until a certain condition is met',
    'dictionary':'A collection of key-value pairs',
    'list':'An ordered collection of items',
# new terms:
    'tuple': 'An ordered, immutable collection of items',
    'set': 'An unordered collection of unique items',
    'boolean': 'A data type that can have one of two values, either True or False',
    'slice': 'A portion of a sequence, such as a list or string',
    'string': 'A sequence of characters enclosed in quotes'
}

for word, definition in glossary.items():
    print(f"{word}: {definition}")