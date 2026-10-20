'''

Raymond Nault
Chapter 7: User Inputs and While Loops

'''

# this code will ask for your age to determine how much your movie ticket will cost.

tickets = True
while tickets:
    age = input('How old are you?')
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print('Your ticket is free.')
        elif age < 12:
            print('Your ticket is $10.')
        else:
            print('Your ticket is $15.')