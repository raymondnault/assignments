'''

Raymond Nault
Chapter 7: User Inputs and While Loops

'''

# deli orders

sandwich_orders = ("turkey", "ham", "roast beef", "italian", "meatball")
finished_sandwiches = []
orders = []

for sandwich in sandwich_orders:
    print(f"Making sandwich: {sandwich}")
    finished_sandwiches.append(sandwich)

print("I made your sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
print("All sandwiches are ready!")