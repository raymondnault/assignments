'''

Raymond Nault
Chapter 7: User Inputs and While Loops

'''

# This program will ask the user for pizza toppings until they indicate they are done.

pizzas = True
while pizzas:
    topping = input('What topping would you like on your pizza?')
    if topping == 'quit':
        pizzas = False
    else:
        print(f'Adding {topping} to your pizza.')
