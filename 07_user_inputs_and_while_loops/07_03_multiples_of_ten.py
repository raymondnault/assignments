'''

Raymond Nault
Chapter 7: User Inputs and While Loops

'''

# This program will ask the user for a number and will determine if it's a multiple of 10.

while True:
    chosen_number = input("What's your chosen number?")
    yes_or_no = int(chosen_number) % 10
    if yes_or_no ==0:
        print(f'{chosen_number} is a multiple of ten!')
    else:
        print(f'{chosen_number} is not a multiple of ten.')