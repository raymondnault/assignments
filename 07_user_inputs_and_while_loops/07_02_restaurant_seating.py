'''

Raymond Nault
Chapter 7: User Inputs and While Loops

'''

# this code will determine if a dinner group has to wait for a bigger table based on how many people are in the group

number_of_people = int(input('How many people are in your dinner group?'))

if (number_of_people) > 8:
    print('You will need to wait for a larger table.')
else:
    print('Your table is ready.')
