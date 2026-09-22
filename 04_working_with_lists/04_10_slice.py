'''

Raymond Nault
Chapter 4: Working with Lists

'''

# this loop use slices to print items in a list by any number of items in the list

animal_list = ['dog', 'cat', 'bird', 'fish', 'hamster', 'rabbit', 'turtle']
print("The first three animals in the list are:")
for animal in animal_list[:3]:
    print(animal)

print("The middle three animals in the list are:")
for animal in animal_list[2:5]:
    print(animal)

print("The last three animals in the list are:")
for animal in animal_list[4:7]:
    print(animal)