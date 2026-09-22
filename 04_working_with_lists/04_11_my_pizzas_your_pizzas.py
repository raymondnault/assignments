'''

Raymond Nault
Chapter 4: Working with Lists

'''

# this loop will use slices to loop through my favorite pizzas and your favorite pizzas and print them out

pizzas = ['pepperoni', 'cheese', 'buffalo chicken', 'margherita']
friends_pizzas = pizzas[:3] + ['bbq chicken']
print("My favorite pizzas are:")
for pizza in pizzas[:]:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friends_pizzas[:]:
    print(pizza)