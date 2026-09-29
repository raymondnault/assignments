'''

Raymond Nault
Chapter 5: If Statements

'''

# series of statements to check for favorite fruits

favorite_fruits = ['apple', 'banana', 'blueberries', 'strawberries']
for fruit in favorite_fruits:
    print(f"I really like {fruit}.")
    if fruit == 'apple':
        print("Apple are my favorite fruit.")
    elif fruit == 'banana':
        print("Bananas are also great!")
    elif fruit == 'blueberries':
        print("Blueberries are delicious!")
    elif fruit == 'strawberries':
        print("Strawberries are tasty!")