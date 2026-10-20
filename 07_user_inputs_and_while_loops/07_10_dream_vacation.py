'''

Raymond Nault
Chapter 7: User Inputs and While Loops

'''

# dream vacation survery

responses = {}

while True:
    name = input("What is your name? ")
    if name.lower() == 'quit':
        break
    vacation = input("If you could visit one place in the world, where would you go? ")
    responses[name] = vacation

print("\n--- Dream Vacation Survey Results ---")
for name, vacation in responses.items():
    print(f"{name} would like to visit {vacation}.")
print("Thank you for participating in the survey!")