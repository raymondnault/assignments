'''

Raymond Nault
Chapter 4: Working with Lists

'''

# these loops will print out my favorite foods

my_foods = ['pizza', 'tacos', 'pasta', 'ice cream', 'sushi']
for food in my_foods:
    print(food)

friends_foods = my_foods[:]
friends_foods.append('burgers')
print("\nMy friend's favorite foods are:")
for food in friends_foods:
    print(food)