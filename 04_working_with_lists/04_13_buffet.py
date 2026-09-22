'''

Raymond Nault
Chapter 4: Working with Lists

'''

# this loop will lists simple foods available at a buffet and then prints them

dimensions = ['chicken', 'steak', 'salad', 'pasta', 'pizza']
sizes = ['small', 'medium', 'large']
for food in dimensions:
    print(f"{food.title()} is available at the buffet.")
for size in sizes:
    print(f"{size.title()} portions are available.")

modified_dimensions = ['chicken', 'steak', 'salad', 'cookies', 'fillet mignon']
for food in modified_dimensions:
    print(f"{food.title()} is available at the buffet.")